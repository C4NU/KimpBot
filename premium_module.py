import math

class Kimp:
    # 클래스 생성자
    def __init__(self):
        self.xrp = {'NAME': 'XRP', 'PRICE': 0, 'KIMP': 0}  # 리플 딕셔너리 변수
        self.xlm = {'NAME': 'XLM', 'PRICE': 0, 'KIMP': 0}  # 스텔라 딕셔너리 변수
        self.eos = {'NAME': 'EOS', 'PRICE': 0, 'KIMP': 0}  # 이오스 딕셔너리 변수
        self.trx = {'NAME': 'TRX', 'PRICE': 0, 'KIMP': 0}  # 트론 딕셔너리 변수
        self.dot = {'NAME': 'DOT', 'PRICE': 0, 'KIMP': 0}  # 폴카닷 딕셔너리 변수
    # 김프 퍼센티지 계산 함수
    def CalcPremiumPercentage(self, krwPrice, usdPrice, tetherPrice):
        return round(((krwPrice/(usdPrice*tetherPrice))*100)-100, 2)
    # 가격 긁어오는 함수

