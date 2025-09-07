import telebot
import os

TOKEN = os.getenv("TOKEN")  # Railway'den alacak
ADMIN_ID = 123456789  # Buraya kendi Telegram ID’ni yaz

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "👋 Merhaba! Bot çalışıyor 🚀")

bot.polling()
