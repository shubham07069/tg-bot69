import telebot
import requests
import os

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
OPENROUTER_API_KEY = os.environ['OPENROUTER_API_KEY']

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "openai/gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are a brutal, dark-humor assistant who uses casual abusive Hindi-English mix language. Give smart, funny and savage replies."
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        result = response.json()
        reply = result["choices"][0]["message"]["content"]
        bot.send_message(message.chat.id, reply)
    except Exception as e:
        bot.send_message(message.chat.id, f"Error aagaya bhosdike: {str(e)}")

bot.polling()

