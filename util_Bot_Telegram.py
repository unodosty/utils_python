import telegram

telgm_token = ''

bot = telegram.Bot(token = telgm_token)

chat_id=''

bot.sendMessage(chat_id = chat_id, text="안녕하세요 GGCoding 채봇입니다.")
bot.send_photo(chat_id=chat_id, photo='https://telegram.org/img/t_logo.png')
bot.send_photo(chat_id=chat_id, photo=open('tests/test.png', 'rb'))


# https://blog.cosmosfarm.com/archives/1070/%ED%85%94%EB%A0%88%EA%B7%B8%EB%9E%A8-%EB%B4%87-telegram-bot-%EB%A7%8C%EB%93%A4%EA%B8%B0/
# https://vmpo.tistory.com/85
