import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

class TelegramBot:
	# 클래스 생성자
	def __init__(self, token, chatID):
		self.bot = telegram.Bot(token=token)
		self.chatID = chatID
		self.updates = self.bot.getUpdates()
	# 메시지 전송 함수
	def SendTelegramMessage(self, _description):
		self.bot.sendMessage(chat_id=self.chatID, text=_description)
    # 메시지 