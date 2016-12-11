from slackclient import SlackClient
import time
import sys


# define our archive function
def archive(messages, channel, slack):
    """
    Archives the provided messages into an HTML file, formatting them correctly,
    which is then posted to slack into the #archives channel.

    Args:
        messages: A list of messages to archive.
        channel: A specific channel within the Slack team.
        slack: Passing through our slack variable.
    """
    # Append each message's text to a string.
    output = ""
    for message in messages:
        output += message['text']

    # Submit string to slack.
    slack.api_call("files.upload", content=output, filetype="html",
                filename="test.html", title="test", channels="messages")


# define our main function
def main():
    """
    Sets up the application.
    """

    # setup slack API token and create a client.
    api_token = sys.argv[1]
    slack = SlackClient(api_token)

    # create a connection with Slack.
    slack.rtm_connect()

    # create a list of messages.
    messages = []

    # loop inside this forever.
    while True:
        # read the events that slack has sent us.
        events = slack.rtm_read()
        print('tick')

        for event in events:
            print(event)

            # Wanna make sure the event type is correct, we should probably also
            # record message edits and deletes too.
            if event['type'] == "message":

                # if the number of messages is below 10,000 store it,
                # if the number of messages is above 10,000, archive the file.
                if len(messages) < 2:
                    print("appending...")
                    # append the event to our messages list.
                    messages.append(event)

                else:
                    print("archiving...")
                    # write to file and post to archives channel
                    archive(messages, '#general', slack)

        # wait one second.
        time.sleep(1)


# Fancy way of running our program, which now begins here.
if __name__ == "__main__":
    main()
