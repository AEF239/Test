import telebot
import random
import time
import requests

TOKEN = '6933304796:AAHrv9LQ4CUZs-ZFIwKCiDgx1-f0gfkWgsM'
bot = telebot.TeleBot(TOKEN)

keyboard = telebot.types.InlineKeyboardMarkup()
start_button = telebot.types.InlineKeyboardButton(text='بدأ الصيد 🎯', callback_data='start_hunting')
keyboard.row(start_button)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'اتفضل', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: call.data in ['start_hunting'])
def handle_callback_query(call):
    if call.data == 'start_hunting':
        bot.edit_message_reply_markup(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
        bot.answer_callback_query(call.id, text='tm')
        start_hunting(call.message)

def start_hunting(message):
    j = 1
    b='QWERTYUIOPLKJHGFDSAZXCVBNM1234567809'
    a = 'QWERTYUIOPLKJHGFDSAMNBVCXC'
    n = '_'
    length = 1
    while True:
       u= ''.join(random.sample(b,length))
       r= ''.join(random.sample(a,length))
       k= ''.join(random.sample(b,length))
       n= ''.join(random.sample(n,length))
       AA=(k+k+k+k+k+k+k+u)
       A=(u+u+u+u+u+u+u+k)
       AAA=(u+n+u+n+k)
       AAAA=(u+n+k+n+r)
       AAAAA=(u+n+r+n+k)
       AAAAAA=(k+n+r+n+u)
       AAAAAAA=(k+n+u+n+r)
       AAAAAAAAA=(r+n+u+n+k)
       AHMad = AA , A , AAA , AAAA , AAAAA , AAAAAA , AAAAAAA , AAAAAAAAA
       user = str("".join(random.choice(AHMad)))
       url = f"https://t.me/{user}"
       req = requests.get(url)
       if req.text.find('If you have <strong>Telegram</strong>, you can contact <a class="tgme_username_link"')>=0: 
        bot.reply_to(message, f" [{j}] ✅ ☑️    >> [ {user} ]")
        try:
         req = requests.post(f'''https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={message.chat.id}&text=-\n 𝗨𝗦𝗘𝗥 :  @{user} \n @R_A_J_Y -''')
        except NameError:
         pass
       else:
        bot.reply_to(message, f" [{j}] ⛔🚫 >> [ {user} ]")
       j += 1
       



bot.polling()
