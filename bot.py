import telebot

# Your bot token
BOT_TOKEN = "8368440097:AAHbP1cbmRKAbtCTioZm8naLmTC2dSuIERU"

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Command handlers
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm a simple Telegram bot. Send me any text and I'll echo it back.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

if __name__ == '__main__':
    print("Bot started with long polling...")
    bot.infinity_polling()
