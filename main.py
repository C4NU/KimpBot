import json

import telegram # 텔레그램 키 읽어올 json 패키지
import telegram_module as MessageModule # 텔레그렘 봇 모듈

# 메인 함수
def main():
    with open("keys_sample.json") as f:
            data = json.load(f)
    # initialize bot class
    bot = MessageModule.TelegramBot(
    	data["telegram"]["token"], data["telegram"]["chatID"])
    # initialize bot functions
    bot.HandlerInitialize()
    # bot start updates
    bot.updater.start_polling()
    bot.updater.idle()

if __name__ == '__main__':
    main()