# telegram-order-b
Telegram botim
import telebot
from telebot import types

TOKEN = '8109214293:AAGPLoCeUN3xwr6lAC6sFI4d76LrU3VSLzA'

ADMIN_ID = 8161512589  # O'zing Telegram ID'ingni yoz

bot = telebot.TeleBot(TOKEN)
users = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    users[chat_id] = {}
    bot.send_message(chat_id, "Ismingizni kiriting:")

@bot.message_handler(func=lambda m: chat_step(m.chat.id) == 0)
def get_name(message):
    users[message.chat.id]["name"] = message.text
    bot.send_message(message.chat.id, "Telefon raqamingizni kiriting:")
    users[message.chat.id]["step"] = 1

@bot.message_handler(func=lambda m: chat_step(m.chat.id) == 1)
def get_phone(message):
    users[message.chat.id]["phone"] = message.text
    bot.send_message(message.chat.id, "Telegram username'ingizni kiriting:")
    users[message.chat.id]["step"] = 2

@bot.message_handler(func=lambda m: chat_step(m.chat.id) == 2)
def get_username(message):
    users[message.chat.id]["username"] = message.text
    bot.send_message(message.chat.id, "Buyurtma qilmoqchi bo‘lgan mahsulot nomini yozing:")
    users[message.chat.id]["step"] = 3

@bot.message_handler(func=lambda m: chat_step(m.chat.id) == 3)
def get_product(message):
    users[message.chat.id]["product"] = message.text
    data = users[message.chat.id]
    text = f"🛒 Yangi buyurtma:\n\n👤 Ism: {data['name']}\n📱 Tel: {data['phone']}\n🔗 Username: {data['username']}\n📦 Mahsulot: {data['product']}"
    bot.send_message(ADMIN_ID, text)
    bot.send_message(message.chat.id, "✅
