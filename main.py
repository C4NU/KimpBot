import telegram_module as MessageModule

# 메인 함수
def main():
    # initialize bot class
    bot = MessageModule.TelegramBot(
    	'2039263005:AAF_KVYVpcBHvBEbRPvlwtsj_njNRtpEE0E', 305295334)
    # initialize bot functions
    bot.HandlerInitialize()
    # bot start updates
    bot.updater.start_polling()
    bot.updater.idle()

if __name__ == '__main__':
    main()