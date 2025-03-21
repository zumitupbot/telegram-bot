import os
import sys
from keep_alive import keep_alive
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger("mybot")

# Replace with your BotFather token
os.environ.get("BOT_TOKEN")

# ✅ Faster response: Use @run_async
@run_async
def start(update, context):
    update.message.reply_text(
        "Hello! I am your chatbot. Here are some commands you can use:\n"
        "/help - Show available commands\n"
        "/about - Learn about this bot\n"
        "You can also just chat with me!"
    )


@run_async
def help_command(update, context):
    update.message.reply_text(
        "Available commands:\n"
        "/start - Start the bot\n"
        "/help - Show this help message\n"
        "/about - Learn about this bot\n\n"
        "Or simply chat with me by saying hi, how are you, etc."
    )


@run_async
def about_command(update, context):
    update.message.reply_text(
        "I'm a simple chatbot created with Python and the Telegram Bot API. "
        "I can respond to basic messages and commands!"
    )


@run_async
def reply_hi(update, context):
    username = update.message.from_user.first_name
    update.message.reply_text(f"Hi {username}, how are you!")


@run_async
def reply_fine(update, context):
    update.message.reply_text("Nice! What are you up to today?")


@run_async
def reply_how_are_you(update, context):
    update.message.reply_text("I'm doing great, thanks for asking! How about you?")


@run_async
def reply_default(update, context):
    update.message.reply_text(
        "hi."
    )


def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(CommandHandler("about", about_command))

    # ✅ Faster filters for messages
    dp.add_handler(MessageHandler(Filters.regex("(?i)^hi$|^hello$"), reply_hi))
    dp.add_handler(MessageHandler(Filters.regex("(?i)^i am fine$|^i'm good$|^good$|^great$"), reply_fine))
    dp.add_handler(MessageHandler(Filters.regex("(?i)^how are you$|^how are you\?$"), reply_how_are_you))
    
    # Default handler for other messages
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, reply_default))

    # Start the bot
    keep_alive()
    updater.start_polling()
    logger.info("🤖 Chatbot is running...")
    updater.idle()


if __name__ == "__main__":
    main()
