import collections
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
		self.collection = PremiumModule.Kimp()
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
	def GetXRPPremium(self, update, context):
		result = self.collection.CalcPremiumPercentage('XRP')
		self.SendTelegramMessage("리플의 현재 김프: "+str(result)+"%\n"
		+"리플 원화: "+str(self.collection.GetUpbitPrice("XRP"))+"\n"
		+"리플 달러: "+str(self.collection.GetBinancePrice("XRP"))+"\n"
		+"USD/KRW 환율: "+str(self.collection.GetUSDPrice()))
	# 스텔라 김프 구해오는 함수
	def GetXLMPremium(self, update, context):
		result = self.collection.CalcPremiumPercentage('XLM')
		self.SendTelegramMessage("스텔라의 현재 김프: "+str(result)+"%\n"
		+"스텔라 원화: "+str(self.collection.GetUpbitPrice("XLM"))+"\n"
		+"스텔라 달러: "+str(self.collection.GetBinancePrice("XLM"))+"\n"
		+"USD/KRW 환율: "+str(self.collection.GetUSDPrice()))
	# 이오스 김프 구해오는 함수
	def GetEOSPremium(self, update, context):
		result = self.collection.CalcPremiumPercentage('EOS')
		self.SendTelegramMessage("이오스의 현재 김프: "+str(result)+"%\n"
		+"이오스 원화: "+str(self.collection.GetUpbitPrice("EOS"))+"\n"
		+"이오스 달러: "+str(self.collection.GetBinancePrice("EOS"))+"\n"
		+"USD/KRW 환율: "+str(self.collection.GetUSDPrice()))
	# 트론 김프 구해오는 함수
	def GetTRXPremium(self, update, context):
		result = self.collection.CalcPremiumPercentage('TRX')
		self.SendTelegramMessage("트론의 현재 김프: "+str(result)+"%\n"
		+"트론 원화: "+str(self.collection.GetUpbitPrice("TRX"))+"\n"
		+"트론 달러: "+str(self.collection.GetBinancePrice("TRX"))+"\n"
		+"USD/KRW 환율: "+str(self.collection.GetUSDPrice()))
	# 폴카닷 김프 구해오는 함수
	def GetDOTPremium(self, update, context):
		result = self.collection.CalcPremiumPercentage('DOT')
		self.SendTelegramMessage("폴카닷의 현재 김프: "+str(result)+"%\n"
		+"폴카닷 원화: "+str(self.collection.GetUpbitPrice("DOT"))+"\n"
		+"폴카닷 달러: "+str(self.collection.GetBinancePrice("DOT"))+"\n"
		+"USD/KRW 환율: "+str(self.collection.GetUSDPrice()))
	def GetALGOPremium(self, update, context):
		result = self.collection.CalcPremiumPercentage('ALGO')
		self.SendTelegramMessage("알고랜드의 현재 김프: "+str(result)+"%\n"
		+"알고랜드 원화: "+str(self.collection.GetUpbitPrice("ALGO"))+"\n"
		+"알고랜드 달러: "+str(self.collection.GetBinancePrice("ALGO"))+"\n"
		+"USD/KRW 환율: "+str(self.collection.GetUSDPrice()))
    # CommandHandler 생성 함수
	def HandlerInitialize(self):
		# Handler 정의 (텔레그램 /"명령어" 인삭)
		self.startHandler = CommandHandler('start', self.StartBot)
		self.stopHandler = CommandHandler('stop', self.StopBot)
		self.getXRPPremiumHandler = CommandHandler('xrp', self.GetXRPPremium)
		self.getXLMPremiumHandler = CommandHandler('xlm', self.GetXLMPremium)
		self.getEOSPremiumHandler = CommandHandler('eos', self.GetEOSPremium)
		self.getTRXPremiumHandler = CommandHandler('trx', self.GetTRXPremium)
		self.getDOTPremiumHandler = CommandHandler('dot', self.GetDOTPremium)
		self.getALGOPremiumHandler = CommandHandler('algo', self.GetALGOPremium)
		# Handler 추가
		self.dispatcher.add_handler(self.startHandler)
		self.dispatcher.add_handler(self.stopHandler)
		self.dispatcher.add_handler(self.getXRPPremiumHandler)
		self.dispatcher.add_handler(self.getXLMPremiumHandler)
		self.dispatcher.add_handler(self.getEOSPremiumHandler)
		self.dispatcher.add_handler(self.getTRXPremiumHandler)
		self.dispatcher.add_handler(self.getDOTPremiumHandler)
		self.dispatcher.add_handler(self.getALGOPremiumHandler)

def main():
	print("Telegram Module Test")
	
if __name__ == '__main__':
	main()