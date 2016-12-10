from slackclient import SlackClient

# setup slack API token and create a client.
api_token = "foo"
slack = SlackClient(api_token)

# create a connection with Slack.
slack.rtm_connect()

# message counter

# loop inside this forever.
while True:
    # read the events that slack has sent us.

    # for each event increment our message counter.

    # if the message counter is below 10,000, add it to a file.

    # if the message counter is above 10,000, archive the file.

    # wait one second.
