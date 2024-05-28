import telebot
import random
import time
import requests
import os

TOKEN = '6974068885:AAF1ri7vhih_x3eCaOOBNIfCtw-SLCZi7wY'
bot = telebot.TeleBot(TOKEN)

stop_flag = False
checked_usernames = set()  # مجموعة للاحتفاظ باليوزرات التي تم التحقق منها
FILENAME = 'checked_usernames.txt'  # اسم الملف لحفظ اليوزرات

def load_checked_usernames():
    global checked_usernames
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            checked_usernames = set(line.strip() for line in file)

def save_checked_username(username):
    with open(FILENAME, 'a') as file:
        file.write(username + '\n')

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'بدء صيد يوزرات بوتات ثلاثية...')

    # ابدأ عملية الصيد مباشرة عند استلام رسالة /start
    global stop_flag
    stop_flag = False
    load_checked_usernames()  # تحميل اليوزرات التي تم التحقق منها سابقاً
    start_hunting(message)

@bot.message_handler(commands=['stop'])
def stop(message):
    global stop_flag
    stop_flag = True
    bot.send_message(message.chat.id, 'تم إيقاف الصيد')

def check_username(username):
    url = f"https://t.me/{username}"
    req = requests.get(url)
    if req.status_code == 200:
        if 'This username is not taken' in req.text:
            return False  # اليوزر متاح
        elif 'If you have <strong>Telegram</strong>' in req.text:
            return True   # اليوزر محجوز من قبل مستخدم Telegram
    return False  # اليوزر غير معروف أو متاح

def start_hunting(message):
    global stop_flag
    j = 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    while not stop_flag:
        try:
            # توليد يوزر ثلاثي مع لاحقة "bot"
            while True:
                username = ''.join(random.choices(alphabet, k=3)) + 'bot'
                if username not in checked_usernames:
                    checked_usernames.add(username)
                    save_checked_username(username)  # حفظ اليوزر في الملف
                    break
            
            if check_username(username):
                bot.send_message(message.chat.id, f"[{j}] ⛔🚫 >> [ {username} ] (تم حجزه من قبل مستخدم Telegram)")
            else:
                bot.send_message(message.chat.id, f"[{j}] ✅ ☑️    >> [ {username} ] متاح")
                try:
                    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={message.chat.id}&text=-\n 𝗨𝗦𝗘𝗥 :  @{username} \n @QYQ_3 -')
                except Exception as e:
                    print(f"Error: {e}")
            j += 1
            # إضافة تأخير قصير لجعل العملية أقل عبئًا على الخادم
        except Exception as e:
            print(f"Error: {e}")

bot.polling()
