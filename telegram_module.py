import telegram
from telegram.ext import Updater, dispatcher
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters

import premium_module as PremiumModule
class TelegramBot:
	# 클래스 생성자
	def __init__(self, _token, _chatID):
		self.bot = telegram.Bot(token=_token)
		self.chatID = _chatID
		self.updater = Updater(token=_token, use_context=True)
		self.dispatcher = self.updater.dispatcher
    # 메시지 전송 함수
	def SendTelegramMessage(self, _description):
		self.bot.sendMessage(chat_id=self.chatID, text=_description)
	# 봇 시작 함수
	def StartBot(self, update, context):
		self.SendTelegramMessage("봇 작동 시작.")
	# 봇 정지 함수
	def StopBot(self, update, context):
		self.SendTelegramMessage("봇 작동 종료.")
	# 리플 김프 구해오는 함수
	def GetXRPPremium(self):
		pass
	# 스텔라 김프 구해오는 함수
	def GetXLMPremium(self):
		pass
	# 이오스 김프 구해오는 함수
	def GetEOSPremium(self):
		pass
	# 트론 김프 구해오는 함수
	def GetTRXPremium(self):
		pass
	# 폴카닷 김프 구해오는 함수
	def GetDOTPremium(self):
		pass
    # CommandHandler 생성 함수
	def HandlerInitialize(self):
		self.startHandler = CommandHandler('start', self.StartBot)
		self.stopHandler = CommandHandler('stop', self.StopBot)
		self.dispatcher.add_handler(self.startHandler)
		self.dispatcher.add_handler(self.stopHandler)

# 클래스 테스트 용 메인 함수
def main():
	Bot=TelegramBot('2039263005:AAF_KVYVpcBHvBEbRPvlwtsj_njNRtpEE0E',305295334)
	Bot.HandlerInitialize()

	Bot.updater.start_polling()
	Bot.updater.idle()
    
if __name__ == '__main__':
	main()