import config
import telebot
bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,  "Рада тебя видеть! \nКак настроение?")

@bot.message_handler(content_types=['text'])
def answer(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop = True)
