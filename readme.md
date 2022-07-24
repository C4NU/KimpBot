# 김치프리미엄 봇

## Description
* 리플
* 스텔라
* 이오스
* 트론
* 폴카닷
* 알고랜드 (2022.07.25 추가)

6개의 전송에 용이한 코인의 김치프리미엄을 알려주는 텔레그램 봇.

## Requirements

1. Python 3.9
2. Binance API
   1. 바이낸스 API 발급 받아 keys_sample.json에 맞춰서 작성합니다.
      1. https://hichoco.tistory.com/entry/바이낸스-Binance-API-키-발급-받기
         1. 방법 참조해주세요.
3. Telegram Bot
   1. BotFather에서 개인 봇을 발급 받아 주세요.
      1. https://kminito.tistory.com/24 이 글 참조해주세요 :)
4. PythonAnywhere
   1. 개인 서버에서 돌려도 상관 없습니다 :)

## Install

### Install requirements.txt

```python
pip install -r requirements.txt
```

### Set keys_sample.json

```json
{
	"binance": { 
		"api_key": "바이낸스에서 발급 받은 api key",
		"api_secret": "바이낸스에서 발급 받은 api secret key"
	},
	"telegram": {
		"token": "텔레그램 봇 토큰", - 텔레그램 봇 파더에서 발급 받은 토큰
		"chatID": "텔레그램 개인 chatID" - 텔레그램 봇 파더에서 받은 개인 chat_id 값
	}
}
```

### Run Python3 in "KimpBot" Directory

```python
python3 main.py
```

