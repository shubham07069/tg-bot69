import telebot
import os
import random

TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# 🔞 Random gaali list (aur add kar sakta hai tu apni pasand ki 😎)
gaali_list = [
    "Kya bolta be bhosdike? 😤",
    "Chal bhaag yaha se laude! 💩",
    "Sun bhen ke l***, kya chahiye tujhe? 😂",
    "Aa gaya firse chutiyapa leke? 😒",
    "Kyu bula raha hai bhenchod? 🤬",
    "Apun busy hai madarchod! 😎",
    "Gand maarunga teri virtual hi sahi 💀"
]

@bot.message_handler(func=lambda message: message.chat.type in ['group', 'supergroup'])
def handle_group_messages(message):
    if f"@{bot.get_me().username}" in message.text:
        random_gaali = random.choice(gaali_list)
        bot.reply_to(message, random_gaali)

@bot.message_handler(func=lambda message: message.chat.type == 'private')
def handle_private(message):
    bot.reply_to(message, "Private me mat aa laude, public me chillaunga teri maa ki 😆")

bot.polling()
