import telegram
from selenium import webdriver
from selenium.webdriver import ActionChains
from os import path
from requests_html import HTMLSession
from telegram import bot

class TelegramBot:
	# 클래스 생성자
	def __init__(self, token, chatID):
		self.bot = telegram.Bot(token=token)
		self.chatID = chatID
		self.updates = self.bot.getUpdates()
	# 메시지 전송 함수
	def SendTelegramMessage(self, _description):
		self.bot.sendMessage(chat_id=self.chatID, text=_description)

class Kimp:
    # 클래스 생성자
    def __init__(self):
        self.xrp={'NAME':'XRP', 'PRICE':0, 'KIMP':0} # 리플 딕셔너리 변수
        self.xlm={'NAME':'XLM', 'PRICE':0, 'KIMP':0} # 스텔라 딕셔너리 변수
        self.eos={'NAME':'EOS', 'PRICE':0, 'KIMP':0} # 이오스 딕셔너리 변수
        self.trx={'NAME':'TRX', 'PRICE':0, 'KIMP':0} # 트론 딕셔너리 변수
        self.dot={'NAME':'DOT', 'PRICE':0, 'KIMP':0} # 폴카닷 딕셔너리 변수
    # 김프 퍼센트 가져오는 함수
    def GetXRPKimp(self):
	    session = HTMLSession() # session 변수 생셩
	    r = session.get("https://kimpga.com/") # 김프가 사이트 세션 가져오기 
	    current_sleep = 2 # sleep 카운트
	    element_count = 0
	    while element_count == 0:
		    r.html.render(sleep=current_sleep)
		    elements = r.html.xpath('//*[@id="__next"]/div[1]/div/div[1]/div[6]/div/table/tbody/tr[4]/td[3]')
		    element_count = len(elements)
		    current_sleep += 2
		    if current_sleep == 10:
			    return "Timeout"
	    return elements[0].text

"""
메인 함수.
"""
def main():
    # initialize class
    bot = TelegramBot('1912451996:AAH3bvL8HICM64IgmBX0Fn06hfnxw09lqz8', 305295334)
    collection = Kimp()
	# initialize variables
    
    


if __name__ == '__main__':
    main()
"""
코인 이름 xpath //*[@id="__next"]/div[1]/div/div[1]/div[6]/div/table/tbody/tr/td[1]/div/div[1]/span
김프 퍼센트 xpath //*[@id="__next"]/div[1]/div/div[1]/div[6]/div/table/tbody/tr/td[3]/div[1]
"""