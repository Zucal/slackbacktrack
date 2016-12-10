from slackclient import SlackClient
import time

# setup slack API token and create a client.
api_token = "foo"
slack = SlackClient(api_token)

# create a connection with Slack.
slack.rtm_connect()

# create a list of messages.
messages = []

# loop inside this forever.
while True:
    # read the events that slack has sent us.
    events = slack.rtm_read()

    for event in events:

        # Wanna make sure the event type is correct, we should probably also
        # record message edits and deletes too.
        if event['type']  == "message":

        # if the number of messages is below 10,000 store it,
        # if the number of messages is above 10,000, archive the file.
            if len(messages) < 10:
                # store

            else:
                # write to file and post to archives channel


    # wait one second.
    time.sleep(1)
