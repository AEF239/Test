import telebot
import random
import time
import requests
import os

TOKEN = '6974068885:AAF1ri7vhih_x3eCaOOBNIfCtw-SLCZi7wY'
bot = telebot.TeleBot(TOKEN)

stop_flag = False
checked_usernames = set()
FILENAME = 'checked_usernames.txt'

# تعيين متغير لتحديد مدة التأخير بين دورات الصيد
DELAY_BETWEEN_CYCLES = 5  # بالثواني

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
    global stop_flag
    stop_flag = False
    load_checked_usernames()
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
            return False
        elif 'If you have <strong>Telegram</strong>' in req.text:
            return True
    return False

def start_hunting(message):
    global stop_flag
    j = 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    while not stop_flag:
        try:
            while True:
                username = ''.join(random.choices(alphabet, k=3)) + 'bot'
                if username not in checked_usernames:
                    checked_usernames.add(username)
                    save_checked_username(username)
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
            
            # تأخير لبضع ثوانٍ قبل بدء الدورة التالية
            time.sleep(DELAY_BETWEEN_CYCLES)
        except Exception as e:
            print(f"Error: {e}")

bot.polling()
