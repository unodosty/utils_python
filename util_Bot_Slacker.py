from slacker import Slacker

token = 'Slack API Token'
slack = Slacker(token)
slack.chat.post_message('#general', 'Bot test message')
