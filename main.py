from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests

# Замените 'YOUR_TELEGRAM_TOKEN' на ваш токен бота Telegram
TELEGRAM_TOKEN = '6898158317:AAGW_WCZ5LoaAyxuxl5r2b0pMIfFdJ-XUOs'
# Замените на ваш Webex 'access_token' и 'site_url'
WEBEX_ACCESS_TOKEN = 'OWNkMWVlMzctOTIzYy00NTQ0LTkyNTMtMjFjNWYwYmJiMTg4MWNmYmU2YzItNjNh_PE93_64bb227d-594d-4030-a56f-373e324be165'
WEBEX_SITE_URL = 'https://www.webex.com/'

def start(update, context):
    update.message.reply_text('Привет! Отправь мне команду /newmeeting, чтобы создать новую видеоконференцию Webex.')

def new_meeting(update, context):
    headers = {
        'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}',
        'Content-Type': 'application/json'
    }
    data = {
        "title": "Новая Видеоконференция",
        # Добавьте другие необходимые параметры для вашего запроса
    }
    response = requests.post(f'https://{WEBEX_SITE_URL}/v1/meetings', headers=headers, json=data)
    if response.status_code == 200:
        meeting_link = response.json()['webLink']
        update.message.reply_text(f'Ссылка на вашу видеоконференцию: {meeting_link}')
    else:
        update.message.reply_text('Произошла ошибка при создании видеоконференции.')

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("newmeeting", new_meeting))

    updater.start_polling()
    updater.idle()

if name == 'main':
    main()