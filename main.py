import telebot
import requests
import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

CUSTOM_INSTRUCTION = "Act like a witty assistant who roasts idiots but still gives accurate info."

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text

    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "google/gemini-2.5-pro-exp-03-25:free",
        "messages": [
            {"role": "system", "content": CUSTOM_INSTRUCTION},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        result = response.json()

        if "choices" in result:
            bot.reply_to(message, result["choices"][0]["message"]["content"])
        else:
            bot.reply_to(message, f"maa chudi padi hai, response ye aya:\n{result}")

    except Exception as e:
        bot.reply_to(message, f"Error aa gaya laude: {str(e)}")

bot.polling()
