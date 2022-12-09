# pip install python-telegram-bot --pre

# Погода    https://wttr.in/{message_text}
# Википедия https://ru.wikipedia.org/wiki/{message_text}
# Спорт     https://sport24.ru/search?text={message_text}

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import filters, ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler

async def start(update, context):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Напиши мне город, а я отправлю погоду в нём"
    )

async def send_data(update, context):
    message_text = update.message.text

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=f'Хочешь посмотреть в городе {message_text}?',
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text='Посмотреть...', web_app=WebAppInfo(f'https://wttr.in/{message_text}'))]]
        )
    )


application = ApplicationBuilder().token('YOUR TOKEN FROM FATHERBOT').build()

start_handler = CommandHandler('start', start)
application.add_handler(start_handler)

weather_sender = MessageHandler(filters.TEXT, send_data)
application.add_handler(weather_sender)

application.run_polling()