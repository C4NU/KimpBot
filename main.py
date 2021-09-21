from typing import Text
from selenium import webdriver
from selenium.webdriver import ActionChains
from os import path
from requests_html import HTMLSession
import time

import telegram_module as MessageModule
import premium_module as Premium
# 메인 함수
def main():
    # initialize class
    bot = MessageModule.TelegramBot(
    	'2039263005:AAF_KVYVpcBHvBEbRPvlwtsj_njNRtpEE0E', 305295334)
    collection = Premium.Kimp()
    # initialize bot functions
    bot.HandlerInitialize()
    bot.updater.start_polling()
    bot.updater.idle()

    counter = 0
    # main logic
    #bot.SendTelegramMessage(collection.CalcPremiumPercentage(350.0,0.2793,1178.5))



if __name__ == '__main__':
    main()