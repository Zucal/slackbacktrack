from slackclient import SlackClient
import time
import sys
import logging

# define our file_message_count function
def file_message_count(for_channel):
    """
    For a given channel (provided by the argument `for_channel`), read our temporary
    file for holding messages and find out how many messages it currently has.

    Args:
        for_channel: A channel to find a file for ("general", "stuff", etc)

    Returns:
        An integer, of how many messages are in the current temporary file.
    """

def record_message(message):
    """
    For a given message (provided by the argument `message`), record it to
    its appropriate temporary file.

    Args:
        message: The message to append at the bottom of the file.
    """


# define our archive function
def archive_messages(channel, slack):
    """
    Posts the current messages holding file for a particular channel into slack,
    then empties the file.

    Args:
        channel: A specific channel within the Slack team.
        slack: Passing through our slack variable.
    """

    # Submit string to slack.
    slack.api_call("files.upload", content=output, filetype="html",
                filename="test.html", title="test", channels="messages")


# define our main function
def main():
    """
    Sets up the application.
    """

    # setup logging
    logging.basicConfig(filename='slackbacktrack.log')

    # setup slack API token and create a client.
    api_token = sys.argv[1]
    slack = SlackClient(api_token)

    # create a connection with Slack.
    has_connected = False
    while not has_connected:
        connection_outcome = slack.rtm_connect()

        if connection_outcome:
            has_connected = True
        else:
            logging.error("{} Fatal error: {}".format(time.strftime("%Y-%m-%d %H:%M:%S"), "Could not connect"))

    # loop inside this forever.
    while True:
        # read the events that slack has sent us.
        events = slack.rtm_read()

        for event in events:
            print(event)

            # Wanna make sure the event type is a message. We don't want to record
            # silly things like typing statuses.
            if event['type'] == "message":

                # Record the message in its correct file
                record_message(event)

                # If the message count of the file exceeds 10, we should archive
                # it to slack.
                if file_message_count(event['channel']) == 10:
                    archive_messages(event['channel'])

            # We should attempt to reconnect if we get this message
            if event['type'] == "goodbye":
                pass

        # wait one second.
        time.sleep(1)


# Fancy way of running our program, which now begins here.
if __name__ == "__main__":
    main()
