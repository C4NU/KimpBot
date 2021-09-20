import telegram

class TelegramBot:
	# 클래스 생성자
	def __init__(self, token, chatID):
		self.bot = telegram.Bot(token=token)
		self.chatID = chatID
		self.updates = self.bot.getUpdates()
	# 메시지 전송 함수
	def SendTelegramMessage(self, _description):
		self.bot.sendMessage(chat_id=self.chatID, text=_description)

"""
메인 함수.
"""
def main():
    # initialize class
	bot = TelegramBot('1912451996:AAH3bvL8HICM64IgmBX0Fn06hfnxw09lqz8', 305295334)

	# initialize variables


if __name__ == '__main__':
    main()