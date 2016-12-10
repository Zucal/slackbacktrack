from slackclient import SlackClient
import time

# setup slack API token and create a client.
api_token = "foo"
slack = SlackClient(api_token)

# create a connection with Slack.
slack.rtm_connect()

# message counter
mesage_counter = 0
# loop inside this forever.
while True:
    # read the events that slack has sent us.
    events = slack.rtm_read()
    for event in events:
        if event['type']  == "message":
        # for each event increment our message counter.

        # if the message counter is below 10,000, add it to a file.

    # if the message counter is above 10,000, archive the file.

    # wait one second.
    time.sleep(1)
