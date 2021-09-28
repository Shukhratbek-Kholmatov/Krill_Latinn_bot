from telebot import types
def admin_button(button):
    if button=="main_button":
        button=types.InlineKeyboardMarkup(row_width=2)
        button1=types.InlineKeyboardButton(text="↗️Oddiy xabar",callback_data="oddiyxabar")
        button2=types.InlineKeyboardButton(text="↗️Forward",callback_data="forwardxabar")
        button3=types.InlineKeyboardButton(text="↗️Rassilka",callback_data="rassilka")
        button4=types.InlineKeyboardButton(text="📊Poll",callback_data="poll")
        button5=types.InlineKeyboardButton(text="Panelni yopish❌",callback_data="delete")
        button6=types.InlineKeyboardButton(text="Bekor qilish❌",callback_data="cancel")
        button.add(button1,button2,button3,button4,button5,button6)
    elif button=="cancel":
        button=types.InlineKeyboardMarkup(row_width=2)
        button1=types.InlineKeyboardButton(text="Bekor qilish❌",callback_data="cancel")
        button2=types.InlineKeyboardButton(text="⬅️Orqaga qaytish",callback_data="admin_back")
        button.add(button1,button2)
        
        
    return button

def button_photo(name,link):
    button=types.InlineKeyboardMarkup(row_width=1)
    button1=types.InlineKeyboardButton(text=name,url=link)
    button.add(button1)
    return button
    
    
    