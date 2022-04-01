import telebot
from constants import TEl_BOT_KEY

bot = telebot.TeleBot(TEl_BOT_KEY)

# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am Crypto Assets Monitor.
To register, please use the /register command
""")

# Handle '/register'
@bot.message_handler(commands=['register'])
def register_new_user(message):
  print(message.text)
  print(message.from_user.id)
  print(message.from_user.first_name)
  print(message.from_user.last_name)


bot.polling()