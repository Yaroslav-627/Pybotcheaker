import telebot

token = "5935027403:AAEmkfwKOwPEF2NrhU6IgDK8qHPuIZ5YsSU"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types="text")
def mess(message):
    a = message.text
    text = a.split()
    for texts in text:
        
        if texts == "vvv" or texts == "ggg" or texts == "fff":
            bot.send_message(message.chat.id, text)
            i=+1
            print(i)

bot.polling(none_stop=True)