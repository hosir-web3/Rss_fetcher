import telebot

bot_token = ''
bot = telebot.TeleBot(bot_token)

updates = bot.get_updates()

for update in updates:
    print(update.message.chat.id, update.message.text)
