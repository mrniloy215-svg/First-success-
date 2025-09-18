# bot.py
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from gtts import gTTS
import os

BOT_TOKEN = "8479594948:AAFhKVWbScojvFrFx-KBlBoT-DlH5fzxW7M"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎤 স্বাগতম! যে কোনো লেখা পাঠান, আমি সেটাকে ভয়েসে রূপান্তর করে দেব।\n\n"
        "উদাহরণ: 'হ্যালো, কেমন আছো?'"
    )

async def text_to_voice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    try:
        # gTTS দিয়ে ভয়েস তৈরি
        tts = gTTS(text=user_text, lang='bn')  # এখানে 'bn' বাংলা; চাওলে অন্য ভাষাও দিতে পারবে
        filename = "voice.mp3"
        tts.save(filename)

        # Telegram এ অডিও পাঠানো
        await update.message.reply_voice(voice=open(filename, 'rb'))
        os.remove(filename)
    except Exception as e:
        await update.message.reply_text(f"❌ ভয়েস তৈরি করতে সমস্যা হয়েছে: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_to_voice))

    print("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()