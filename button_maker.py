from telebot import types
def make_button(button):
    if button=="main_button":
        button=types.InlineKeyboardMarkup(row_width=2)
        item1=types.InlineKeyboardButton(text="Tarjima",callback_data="translate")
        item2=types.InlineKeyboardButton(text="Shriftlar",callback_data="shrift")
        item3=types.InlineKeyboardButton(text="❌",callback_data="delete")
        button.add(item1,item2,item3)
        
    elif button=="shrift_button1":
        button=types.InlineKeyboardMarkup(row_width=2)
        item1=types.InlineKeyboardButton(text="𝚂𝚝𝚢𝚕𝚎-1",callback_data="item1")
        item2=types.InlineKeyboardButton(text="𝘚𝘵𝘺𝘭𝘦-2",callback_data="item2")
        item3=types.InlineKeyboardButton(text="𝓢𝓽𝔂𝓵𝓮-3",callback_data="item3")
        item4=types.InlineKeyboardButton(text="sᴛʏʟᴇ-4",callback_data="item4")
        item5=types.InlineKeyboardButton(text="Dekoratsiya",callback_data="decoration")
        item6=types.InlineKeyboardButton(text="⏪",callback_data="main_back")
        delete=types.InlineKeyboardButton(text="❌",callback_data="delete")
        button.add(item1,item2,item3,item4,item5,delete,item6)
    elif button=="share_button":
        button=types.InlineKeyboardMarkup(row_width=2)
        item1=types.InlineKeyboardButton(text="♻️Ulashish♻️",url=f"https://t.me/share/url?url=https://t.me/Krill_Latinn_bot")
        item2=types.InlineKeyboardButton(text="❌",callback_data="delete")
        item3=types.InlineKeyboardButton(text="🔙",callback_data="orqaga")
        button.add(item1,item2,item3)
    elif button=="shrift_button2":
        button=types.InlineKeyboardMarkup(row_width=2)
        item1=types.InlineKeyboardButton(text="Smile va belgilar",callback_data="smile")
        item2=types.InlineKeyboardButton(text="Uslubiy",callback_data="stylish")
        item3=types.InlineKeyboardButton(text="⬅️",callback_data="back")
        item4=types.InlineKeyboardButton(text="❌",callback_data="delete")
        button.add(item1,item2,item3,item4)
    elif button=="delete_button_for_smile":
        button=types.InlineKeyboardMarkup(row_width=1)
        item1=types.InlineKeyboardButton(text="❌",callback_data="delete")
        button.add(item1)
        
        
        
             
             
    return button