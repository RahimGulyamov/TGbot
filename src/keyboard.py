from aiogram.types import ReplyKeyboardMarkup as Button
from aiogram.types import KeyboardButton as addButton

from googletrans import Translator

tr = Translator()

EPL = ('EPL🏴󠁧󠁢󠁥󠁮󠁧󠁿')
LaLiga = ('La Liga󠁧󠁢󠁥󠁮󠁧󠁿🇪🇸')
SerieA = ('Serie A🇮🇹')
BunLiga = ('Bundesliga🇩🇪')
Ligue1 = ('Ligue 1🇫🇷')
Back = ('/back')

# 🏴󠁧󠁢󠁥󠁮󠁧󠁿 🇪🇸 🇮🇹 🇩🇪 🇫🇷 🇷🇺

btn_lang_en = addButton('en🏴󠁧󠁢󠁥󠁮󠁧󠁿')
btn_lang_ru = addButton('ru🇷🇺')
btn_lang_es = addButton('es🇪🇸')
btn_lang_de = addButton('de🇩🇪')
btn_lang_fr = addButton('fr🇫🇷')

btn_liga_epl = addButton(EPL)
btn_liga_laliga = addButton(LaLiga)
btn_liga_seria_a = addButton(SerieA)
btn_liga_bunliga = addButton(BunLiga)
btn_liga_ligue_1 = addButton(Ligue1)
btn_back = addButton(Back)


kb_user = Button(resize_keyboard=True)
kb_user.row(btn_liga_epl, btn_liga_laliga).row(btn_liga_seria_a, btn_liga_bunliga).row(btn_liga_ligue_1, btn_back)

kb_lang = Button(resize_keyboard=True)
kb_lang.row(btn_lang_en, btn_lang_ru, btn_lang_es, btn_lang_de, btn_lang_fr)
kb_lang0 = ['en🏴󠁧󠁢󠁥󠁮󠁧󠁿', 'ru🇷🇺', 'es🇪🇸', 'de🇩🇪', 'fr🇫🇷']





