import telebot

# استبدال "TOKEN" بتوكن البوت الخاص بك
bot = telebot.TeleBot("6883914443:AAHsg-zw86-sScBMdGfxPSD8G26H2C-cPi8")

# تعيين معرف المشرف
admin_id = "7038145966"

# رسالة الترحيب
welcome_message = "مرحباً بك انا بوت سايت قم بارسال اي رساله وسف اقوم ارسالها الي المشرف بصيغه مجهول"

# إرسال رسالة الترحيب عند الانضمام إلى الدردشة
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, welcome_message)

# استقبال الرسائل من المستخدمين وإرسالها إلى المشرف
@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    bot.send_message(admin_id, f"Message from user {message.from_user.id} : {message.text}")

# تشغيل البوت
bot.polling()
