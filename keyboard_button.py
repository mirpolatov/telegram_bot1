from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup)

rp_button = [
    [KeyboardButton(text='Rasmli reklama qoyish'),
     KeyboardButton(text='Videoli reklam qoyish')],
]

main_rp = ReplyKeyboardMarkup(keyboard=rp_button, resize_keyboard=True, input_field_placeholder='Hello')

countries_button = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Telegram', url='https://t.me/Ustalar_24_7'),
     InlineKeyboardButton(text='Facebook', url='https://www.facebook.com/profile.php?id=100091343606042&mibextid=V3Yony')],
    [InlineKeyboardButton(text='Instagram',url='https://instagram.com/httpst.mespes_texnika_24_7?igshid=MzRlODBiNWFlZA=='),
     InlineKeyboardButton(text='Tik Tok', url='https://www.tiktok.com/@lutfulloh4050?_t=8fhrq3gvSZV&_r=1')],
    [InlineKeyboardButton(text='Adminga murojat 🙋', url='https://t.me/lutfulloh884050')]

])

