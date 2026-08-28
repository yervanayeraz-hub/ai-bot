import os
import telebot
import google.generativeai as genai

# Tokenləri birbaşa serverin gizli ayarlarından (Environment Variables) oxuyur
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

bot = telebot.TeleBot(TELEGRAM_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Brat, Gemini bot işləyir və hər şeyi etməyə hazırdır! 🔥 Sualını ver gəlsin.")

@bot.message_handler(func=lambda message: True)
def chat_with_gemini(message):
    try:
        response = model.generate_content(message.text)
        bot.reply_to(message, response.text)
    except Exception as e:
        bot.reply_to(message, f"Brat, xəta baş verdi: {e}")

print("Bot işə düşdü...")
bot.infinity_polling()
