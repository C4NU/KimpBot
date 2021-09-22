import math # 김프 소수점 2자리 계산용 math 패키지
import pyupbit # 업비트 python wrapper 패키지
from binance import Client # 바이낸스 API python wrapper 패키지

class Kimp:
    # 클래스 생성자
    def __init__(self):
        self.client = Client('NDtnzdI8zBKeE6Ffq0PRjyYWq81NH4nsbUMsB09d9py0JPdaCeBl7SR7DHkVWExo',
         'IdUxUQNRUbMGYO4JPjbWEfcx4ZlANFNZvPut13WsFHG5Haebja8hw0sLIgC75Ftm') # 바이낸스 client 변수
        self.xrp = {'NAME': 'XRP', 'PRICE': 0, 'KIMP': 0}  # 리플 딕셔너리 변수
        self.xlm = {'NAME': 'XLM', 'PRICE': 0, 'KIMP': 0}  # 스텔라 딕셔너리 변수
        self.eos = {'NAME': 'EOS', 'PRICE': 0, 'KIMP': 0}  # 이오스 딕셔너리 변수
        self.trx = {'NAME': 'TRX', 'PRICE': 0, 'KIMP': 0}  # 트론 딕셔너리 변수
        self.dot = {'NAME': 'DOT', 'PRICE': 0, 'KIMP': 0}  # 폴카닷 딕셔너리 변수
    # 김프 퍼센티지 계산 함수
    def CalcPremiumPercentage(self, krwPrice, usdPrice, tetherPrice):
        return round(((krwPrice/(usdPrice*tetherPrice))*100)-100, 2)
    # 업비트 가격 긁어오는 함수, name 인자값에 xrp, xlm, eos, trx, dot
    def GetUpbitPrice(self, name):
        return pyupbit.get_current_price("KRW-"+name) # type: float
    # 바이낸스 가격 긁어오는 함수, name 인자값에 xrp / xlm / eos / trx / dot
    def GetBinancePrice(self, name):
        return float(self.client.get_ticker(symbol=name+'USDT')['lastPrice']) # type: float
    #def GetUSDTPrice(self):
    #    return float(self.client.get_ticker(symbol='USDT')['lastPrice']) # type: float


# 프리미엄 모듈 테스트용 메인 함수
def main():
    premium = Kimp()
    result = premium.CalcPremiumPercentage(premium.GetUpbitPrice('XRP'), premium.GetBinancePrice('XRP'), 1184.44)

    print(result)

# 메인 함수 구역
if __name__ == '__main__':
    main()
