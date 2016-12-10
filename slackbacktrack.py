from slackclient import SlackClient
api_token = "foo"
slack = SlackClient(api_token)
#create a connection with Slack
slack.rtm_connect()
