import telebot
import os
import requests

# Bot Token
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")  # Use environment variable for better security
if not BOT_TOKEN:
    raise ValueError("Bot token is not set. Please provide it in environment variables.")

# Remove Webhook
requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook")
print("Webhook successfully removed bhadwe! 🚀")

# OpenRouter API Key
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
if not OPENROUTER_API_KEY:
    raise ValueError("OpenRouter API Key not found. Please set it in environment variables.")

# Initialize the Bot
bot = telebot.TeleBot(BOT_TOKEN)

# Define the handler for messages
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
        "model": "deepseek/deepseek-chat-v3-0324:free",  # You can try other models too
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

    # Handle response
    if response.status_code == 200:
        data = response.json()
        if 'choices' in data and len(data['choices']) > 0:
            reply = data['choices'][0]['message']['content']
            bot.reply_to(message, reply)
        else:
            bot.reply_to(message, "Ruk ja bhai thodi der Abhi mera maa chuda hua hai"! 😵")
    else:
        bot.reply_to(message, f"Error: {response.status_code} - Something went wrong! 😖")

# Start polling
bot.infinity_polling(skip_pending=True)
