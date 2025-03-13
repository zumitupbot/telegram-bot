import logging
from telegram.ext import filters, updater CommandHandler, MessageHandler 
from telegram.ext.dispatcher import run_async  # ✅ Import run_async for faster replies

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("mybot")

# Replace with your BotFather token
BOT_TOKEN = "7736822115:AAFbsHBJeB-goS3U3g6x0p0mGVELqbg7k6Q"


# ✅ Faster response: Use @run_async
@run_async
def start(update, context):
    update.message.reply_text(
        "Hello! I am your chatbot. Say 'hi' and I'll greet you!")


@run_async
def help_command(update, context):
    update.message.reply_text("Just send me a message, and I'll respond!")


@run_async
def reply_hi(update, context):
    username = update.message.from_user.first_name
    update.message.reply_text(f"Hi {username}, how are you!")


@run_async
def reply_fine(update, context):
    update.message.reply_text("Nice!")


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    # ✅ Faster filters
    dp.add_handler(MessageHandler(Filters.regex("(?i)^hi$"), reply_hi))
    dp.add_handler(MessageHandler(Filters.regex("(?i)^i am fine$"),
                                  reply_fine))

    # Start the bot
    updater.start_polling()
    logger.info("🤖 Chatbot is running...")
    updater.idle()


if __name__ == "__main__":
    main()
