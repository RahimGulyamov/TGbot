from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from googletrans import Translator
from googletrans.constants import LANGUAGES
import src.keyboard as keyboard
from src.keyboard import kb_user
from src.keyboard import kb_lang
from src.keyboard import kb_lang0
from src.wiki import Football
from src.config import TOKEN
from src.constants import *

tr = Translator()

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

language = 'ru'

active = False


@dp.message_handler(commands=['start', 'back', 'language'])
async def command_start(message: types.Message):
    """
    This async function for command of [/start], [/back], [/language].
    :param message: messenger.text
    :return: message to user
    """
    global active
    active = False
    await bot.send_message(
        message.from_user.id, 'Hi!  Plaese change the language:\n '
                              'Example:  <b><i>en</i></b>', parse_mode='HTML',
        reply_markup=kb_lang)


@dp.message_handler()
async def leagues(message: types.Message):
    """
    This async function responsible for every message from user.
    Bot will read and answer to user
    :param message:
    :return:messege
    """
    # these condition for choosing language
    global language, active
    for i in kb_lang0:
        if message.text == i:
            message.text = message.text[:2]
    if not active and LANGUAGES.__contains__(message.text):
        language = message.text
        active = True
        await bot.send_message(
            message.from_user.id, tr.translate('Choose the League:', dest=language).text,
            reply_markup=kb_user)
    elif not active and not LANGUAGES.__contains__(message.text):
        active = False
        await bot.send_message(
            message.from_user.id, "Wrong language input.\n "
                                  'Example:  <b><i>en</i></b>', parse_mode='HTML',
            reply_markup=kb_lang)

    # this condition for table
    elif active and message.text in main_leagues:
        f = Football(main_leagues[message.text].url, language)
        f.update()
        await bot.send_message(
            message.from_user.id, tr.translate(main_leagues[message.text].table_name, dest=language).text,
            reply_markup=kb_user)
        await bot.send_message(message.from_user.id, f.get_rank(),
                               parse_mode='HTML', reply_markup=kb_user)

    # this condition for status of active after command [/back]
    elif active and message.text == '/back':
        active = False

    # this condition every wrong message from user
    else:
        f = Football(url_ligue_1, language)
        f.update()
        await bot.send_message(message.from_user.id, f.get_error(),
                               parse_mode='HTML', reply_markup=kb_user)


# running bot
def running():
    executor.start_polling(dp, skip_updates=True)
