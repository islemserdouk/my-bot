import telebot
from googletrans import Translator  


bot = telebot.TeleBot('6380402666:AAHS7PROsr2jp7AnUSKWbyhe2P7s1F7tQTw')
translator = Translator()

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "مرحبًا! أرسل النص الذي تريد ترجمته.")

@bot.message_handler(func=lambda message: True)
def translate(message):
    try:
        text = message.text
        translated_text = translator.translate(text, dest='fr')
        bot.reply_to(message, f"النص المترجم: {translated_text.text}")
    except Exception as e:
        bot.reply_to(message, "حدث خطأ أثناء الترجمة. يُرجى المحاولة مرة أخرى.")

bot.polling()
