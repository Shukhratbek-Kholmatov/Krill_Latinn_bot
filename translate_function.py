from transliterator import to_cyrillic,to_latin
from latin2 import detect
from telebot import types
def translate(text):
    if text.isascii():
            translate=to_cyrillic(text)
            response=detect(translate)
    else:
        response=to_latin(text)
    return response
def make_button(button):
        if button=="main_button":
            button=types.InlineKeyboardMarkup(row_width=1)
            button1=types.InlineKeyboardButton("🔹Loyiha muallifi🚩",url="https://t.me/Shukhratbek_Kholmatov")
            button.add(button1) 
        else:
            button=types.InlineKeyboardMarkup(row_width=1)
            button1=types.InlineKeyboardButton("♻️ Do'stlarga ulashish♻️",url="https://t.me/share/url?url=https://t.me/Krill_Latinn_bot")
            button.add(button1)  
        return button

