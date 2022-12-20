import math # 김프 소수점 2자리 계산용 math 패키지
from datetime import datetime # 오늘의 USD/KRW 환율 받아오기 위한 time 패키지
import json # 바낸 클라이언트 키 읽어올 json 패키지

import yfinance as yfi # 야후 파이낸스 python wrapper 패키지
import pyupbit # 업비트 python wrapper 패키지
from binance import Client # 바이낸스 API python wrapper 패키지

class Kimp:
    # 클래스 생성자
    def __init__(self):
        #with open("keys.json") as f:
        with open("keys_sample.json") as f:
            self.data = json.load(f)
        self.client = Client(self.data["binance"]["api_key"],
        self.data["binance"]["api_secret"]) # 바이낸스 client 변수
    # 김프 퍼센티지 계산 함수
    def CalcPremiumPercentage(self, name):
        return round(((self.GetUpbitPrice(name)/(self.GetBinancePrice(name)*self.GetUSDPrice()))*100)-100, 2) # 1184.44는 테더 가격 (임시)
    # 업비트 가격 긁어오는 함수, name 인자값에 xrp, xlm, eos, trx, dot
    def GetUpbitPrice(self, name):
        return pyupbit.get_current_price("KRW-"+name) # type: float
    # 바이낸스 가격 긁어오는 함수, name 인자값에 xrp / xlm / eos / trx / dot
    def GetBinancePrice(self, name):
        return float(self.client.get_ticker(symbol=name+'USDT')['lastPrice']) # type: float
    # 야후 파이낸스에서 USD/KRW 받아오는 함수, pandas series 값.
    def GetUSDPrice(self):
        result = yfi.download(['KRW=X'],start=datetime.today().strftime("%Y-%m-%d"),end=datetime.today().strftime("%Y-%m-%d"))['Close'][0]
        #result = pyupbit.get_current_price("KRW-BTC") / pyupbit.get_current_price("USDT-BTC") 업비트의 테더 가격..
        return round(result,2)

# 프리미엄 모듈 테스트용 메인 함수
def main():
    premium = Kimp()
    #print(datetime.today().strftime("%Y-%m-%d"))
    print(premium.GetUSDPrice())
    print(premium.GetUpbitPrice("XRP"))
    print(premium.GetBinancePrice("XRP"))

# 메인 함수 구역
if __name__ == '__main__':
    main()
