import telebot

# استبدال "TOKEN" بتوكن البوت الخاص بك
bot = telebot.TeleBot("6974068885:AAElseXagWLaIp8ruyyotazAu3uYu6lvyCI")

# تعيين معرف المشرف
admin_id = "6916589114"

# رسالة الترحيب
welcome_message = "مرحباً بك انا بوت سايت قم بارسال اي رساله وسف اقوم ارسالها الي المشرف بصيغه مجهول"

# إرسال رسالة الترحيب عند الانضمام إلى الدردشة
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, welcome_message)

# استقبال الرسائل من المستخدمين وإرسالها إلى المشرف
@bot.message_handler(func=lambda message: True)
def forward_to_admin(message):
    user_id = message.from_user.id
    user_username = message.from_user.username
    user_name = message.from_user.first_name + " " + message.from_user.last_name if message.from_user.last_name else message.from_user.first_name
    if user_username:
        forwarded_message = bot.forward_message(admin_id, user_id, message.id)
bot.polling()
