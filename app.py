
import asyncio
import logging

from telegram import Update
from telegram.ext import Application, ContextTypes, MessageHandler, filters

from config import api_key
from func import searchwb

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(searchwb(update.message.text))


def main() -> None:
    application = Application.builder().token(api_key).build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.run_polling()


if __name__ == "__main__":
    main()