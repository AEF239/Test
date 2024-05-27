import telebot
import random
import time
import requests

TOKEN = '6974068885:AAF1ri7vhih_x3eCaOOBNIfCtw-SLCZi7wY'
bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.InlineKeyboardMarkup()
start_button = telebot.types.InlineKeyboardButton(text='بدأ الصيد 🎯', callback_data='start_hunting')
stop_button = telebot.types.InlineKeyboardButton(text='إيقاف الصيد 🛑', callback_data='stop_hunting')
keyboard.row(start_button)
keyboard.row(stop_button)

stop_flag = False

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'اتفضل', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['start_hunting', 'stop_hunting'])
def handle_callback_query(call):
    global stop_flag
    if call.data == 'start_hunting':
        stop_flag = False
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        bot.answer_callback_query(call.id, text='بدأ الصيد')
        start_hunting(call.message)
    elif call.data == 'stop_hunting':
        stop_flag = True
        bot.answer_callback_query(call.id, text='تم إيقاف الصيد')

def start_hunting(message):
    global stop_flag
    j = 1
    b = 'QWERTYUIOPLKJHGFDSAZXCVBNM1234567809'
    a = 'QWERTYUIOPLKJHGFDSAMNBVCXC'
    n = '_'
    length = 1
    while not stop_flag:
        try:
            u = ''.join(random.sample(b, length))
            r = ''.join(random.sample(a, length))
            k = ''.join(random.sample(b, length))
            n = ''.join(random.sample(n, length))
            AA = (k + k + k + k + k + k + k + u)
            A = (u + u + u + u + u + u + u + k)
            AAA = (u + n + u + n + k)
            AAAA = (u + n + k + n + r)
            AAAAA = (u + n + r + n + k)
            AAAAAA = (k + n + r + n + u)
            AAAAAAA = (k + n + u + n + r)
            AAAAAAAAA = (r + n + u + n + k)
            AHMad = AA, A, AAA, AAAA, AAAAA, AAAAAA, AAAAAAA, AAAAAAAAA
            user = str("".join(random.choice(AHMad)))
            url = f"https://t.me/{user}"
            req = requests.get(url)
            if 'If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"' in req.text:
                bot.send_message(message.chat.id, f"[{j}] ✅ ☑️    >> [ {user} ]")
                try:
                    req = requests.post(f'''https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={message.chat.id}&text=-\n 𝗨𝗦𝗘𝗥 :  @{user} \n @QYQ_3 -''')
                except NameError:
                    pass
            else:
                bot.send_message(message.chat.id, f"[{j}] ⛔🚫 >> [ {user} ]")
            j += 1
            time.sleep(1)  # إضافة تأخير قصير لجعل العملية أقل عبئًا على الخادم
        except Exception as e:
            print(f"Error: {e}")

bot.polling()
