import os
import threading
import telebot
from flask import Flask

# Your bot token
BOT_TOKEN = "8368440097:AAHbP1cbmRKAbtCTioZm8naLmTC2dSuIERU"

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Flask app for health check
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running and polling for messages!"

# Bot command handlers
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm a simple Telegram bot. Send me any text and I'll echo it back.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"You said: {message.text}")

# Function to start bot polling in a background thread
def start_bot():
    print("Starting bot polling...")
    bot.infinity_polling()

if __name__ == '__main__':
    # Start bot in a separate thread
    bot_thread = threading.Thread(target=start_bot, daemon=True)
    bot_thread.start()
    # Run Flask web server
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting web server on port {port}...")
    app.run(host='0.0.0.0', port=port)
