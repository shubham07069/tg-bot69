import telebot
import os
import requests

BOT_TOKEN = "8183341615:AAHXfokwLwHo6swYahB47HOAqZEGrK4d7D0"  # 🛑 Yaha apna real token daal
requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook")
print("Webhook successfully removed bhadwe! 🚀")

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    prompt = message.text
    custom_inst = "You are a funny and helpful AI who abuses like a street dog. Use Hindi + English gaali mix."

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "https://t.me/YOUR_BOT_USERNAME",  # Replace with your bot username
        "X-Title": "TelegramGPTBot"
    }

    data = {
        "model": "deepseek/deepseek-chat-v3-0324:free",  # or claude-3-haiku / llama3
        "messages": [
            {"role": "system", "content": custom_inst},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )

    if response.status_code == 200:
        reply = response.json()['choices'][0]['message']['content']
        bot.reply_to(message, reply)
    else:
        bot.reply_to(message, "Bhai kuch to lauda lag gaya! 😵")

bot.infinity_polling(skip_pending=True)

