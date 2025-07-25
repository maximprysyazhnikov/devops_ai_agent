from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from bot.config import TELEGRAM_BOT_TOKEN
from bot.ai_agent import ask_ai


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привіт! Я — твій DevOps AI Agent Максіка. Напиши мені щось.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = update.message.text
    await update.message.reply_text("🔄 Думаю над відповіддю...")
    try:
        response = await ask_ai(user_input)
        await update.message.reply_text(response)
    except Exception as e:
        await update.message.reply_text(f"⚠️ Помилка: {e}")


def main():
    print("🚀 Bot is starting...")

    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🤖 Polling started...")
    application.run_polling()


if __name__ == "__main__":
    main()
