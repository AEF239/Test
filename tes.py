import instaloader
import os
import re
from pyrogram import Client, filters
from urlextract import URLExtract

# إعدادات الاتصال
api_id = '25369670'
api_hash = '07e3b4d9762b6f38a111a32d86eb5666'
phone_number = '+526221567510'

# تحديد متغير لحالة الترحيب
welcome_enabled = True

# إنشاء العميل
app = Client("my_account", api_id=api_id, api_hash=api_hash, phone_number=phone_number)

# إنشاء كائن Instaloader
L = instaloader.Instaloader()

# تحديد مكتبة لاستخراج الروابط
extractor = URLExtract()

# تحديد الحدث للاستماع إلى الرسائل الواردة
@app.on_message(filters.private)
async def handle_message(client, message):
    global welcome_enabled

    # الكلمة المراد تغييرها والكلمة الجديدة
    old_word = ".رحب"
    new_word = "السلام عليكم"

    # التحقق مما إذا كانت الرسالة تحتوي على الكلمة المراد تغييرها
    if old_word in message.text:
        # تعديل الرسالة
        modified_text = message.text.replace(old_word, new_word)
        await client.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.id,
            text=modified_text
        )

    # إيقاف إرسال رسالة الترحيب
    if message.text.lower() == ".ايقاف":
        welcome_enabled = False
        await message.reply("تم إيقاف إرسال رسالة الترحيب.")

    # إعادة تشغيل إرسال رسالة الترحيب
    if message.text.lower() == ".تشغيل":
        welcome_enabled = True
        await message.reply("تم إعادة تشغيل إرسال رسالة الترحيب.")

    # الترحيب بأي شخص يقوم بمراسلتك
    if welcome_enabled and not message.outgoing and not message.from_user.is_self and not message.from_user.is_bot:
        await message.reply("أهلاً بك! كيف يمكنني مساعدتك؟")

    # تعديل الرسالة لإظهار معرف الحساب عند كتابة ".ايدي" في الرد على رسالة
    if message.text == ".ايدي" and message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await client.edit_message_text(
            chat_id=message.chat.id,
            message_id=message.id,
            text=f"معرف هذا الحساب هو: {user_id}"
        )

    # جلب وتنزيل فيديو Instagram عند كتابة ".انستا + رابط"
    if message.text.startswith(".انستا "):
        instagram_url = message.text.split(".انستا ")[1]
        try:
            # تحميل المنشور باستخدام instaloader
            post = instaloader.Post.from_shortcode(L.context, instagram_url.split("/")[-2])
            target_dir = f"{post.owner_username}_{post.shortcode}"
            L.download_post(post, target=target_dir)

            # إيجاد الملف المحمل
            downloaded_files = os.listdir(target_dir)
            video_file = None
            for file in downloaded_files:
                if file.endswith('.mp4'):
                    video_file = os.path.join(target_dir, file)
                    break

            if video_file:
                await client.send_video(
                    chat_id=message.chat.id,
                    video=video_file
                )
                # حذف الرسالة الأصلية التي تحتوي على الرابط
                if extractor.has_urls(message.text):
                    await client.delete_messages(chat_id=message.chat.id, message_ids=message.id)
            else:
                await message.reply("لم أتمكن من العثور على فيديو في الرابط المرسل.")

            # حذف الملفات المؤقتة
            for file in downloaded_files:
                os.remove(os.path.join(target_dir, file))
            os.rmdir(target_dir)

        except Exception as e:
            await message.reply(f"حدث خطأ أثناء جلب المنشور: {e}")

# تشغيل العميل
app.run()
