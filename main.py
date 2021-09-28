import telebot
from datetime import datetime
from translate_function import translate
from button_maker import make_button
from open_file import open_file
from get_item import get,add_item
from admin_panel import admin_button,button_photo
TOKEN="1801023834:AAHuLfP2yJm7Kt_NKBOKXVgd7hMWBRkfomc"
bot = telebot.TeleBot(TOKEN,parse_mode="MARKDOWN")
admin="904185120"
@bot.message_handler(commands=['start'])
def start(message):
    hozir=datetime.now()
    mid=message.chat.id
    user=message.from_user
    bot.send_message(message.chat.id,f"*Assalomu alaykum {format(user.first_name)}.\nMatn yuboring📥\nBuyruqlar👉 /buyruqlar*")
    bot.send_message(admin,f"*/start bosildi.\n👤Foydalanuvchi:{format(user.first_name)}\n👤 Useri:\n@{format(user.username)}\n🆔 Foydalanuvchi id raqami:\n{message.chat.id}*")
@bot.message_handler(commands=['buyruqlar'])
def buyruqlar(message):
        bot.send_message(message.chat.id,f"*/start - botni ishga tushurish\n/info - bot haqida ma'lumot\n/stat - bot statistikasi*")
        
@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id,f"*Bot orqali matnlarni lotindan-kirillga,kirilldan-lotinga o'girishingiz va matningizni chiroyli shaklga o'tqazishingiz mumkin.Eslatma : tarjima uchun matn 400 belgidan,shriftlar uchun esa 30 belgidan oshmasligi kerak.Tayyor matnni unga bitta bosish orqali nusxalab olishingiz mumkin.*")
@bot.message_handler(commands=['stat'])
def stat(message):
    response1=open_file("database/database.txt","r", return_type="list")
    response1=len(response1)
    response2=open_file("count/count.txt","r",return_type="read")
    bot.send_message(message.chat.id, f"*👥Bot foydalanuvchilari➙{response1} ta\n✅Shu kungacha qilingan tarjimalar soni➙{response2} ta*")
@bot.message_handler(commands=['panel'])
def panel(message):
   global main_admin_button
   main_admin_button=admin_button("main_button")
   msg=message.text
   mid=message.chat.id
   if f"{mid}"==admin:
            request=bot.send_message(admin,"*Userlarga yuboriladigan kontentni tanlang👇*",reply_markup=main_admin_button)
            bot.register_next_step_handler(request,admins)
def admins(message):
         blocked=[]
         read=open_file("admin.txt","r",return_type="read")
         if read=="oddiyxabar":
             users=open_file("database/database.txt","r",return_type="list")
             for user in users:
                                        try:
                                            bot.send_message(user,f"*{message.text}*")
                                        except:
                                            blocked.append(user)
                                            continue
         elif read=="forward":
                 users=open_file("database/database.txt","r",return_type="list")
                 for user in users:
                                        try:
                                            bot.forward_message(user,admin,message.id)
                                        except:
                                            blocked.append(user)
                                            continue
         elif read=="rassilka":
                match=""
                msg=message.text
                for i in msg:
                    if i!="+":
                        match+=i
                    else:
                        match+=i.replace(i," ")
                
                b=match.split()
                if len(b)==4:
                    photo=b[0]
                    caption=b[1]
                    button=button_photo(b[2],b[3])
                    users=open_file("database/database.txt","r",return_type="list")
                    for user in users:
                                            try:
                                                bot.send_photo(user,photo,f"*{caption}*",reply_markup=button)
                                            except:
                                                blocked.append(user)
                                                continue
                else:
                    bot.send_message(admin,f"*Ma'lumotlarda xatolik bor.*")
   
@bot.message_handler(content_types=["text"])
def text(message):
    mid=message.chat.id
    global msg
    msg=message.text
    hozir=datetime.now()
    button=make_button("main_button")
    bot.send_chat_action(message.chat.id,"typing")
    bot.send_message(message.chat.id,f"{msg}\n\n*Tanlang👇*",reply_markup=button) 
#database👇
    users=open_file("database/database.txt","r",return_type="list")
    if f"{mid}" not in users:
        open_file("database/database.txt","a",text_for_write=f"{mid}") 

@bot.callback_query_handler(func=lambda call:True)
def answer(call):
    main_button=make_button("main_button")
    share_button=make_button("share_button")
    shrift_button1=make_button("shrift_button1")
    shrift_button2=make_button("shrift_button2")
    cancel_button=admin_button("cancel")
    delete_button_for_smile=make_button("delete_button_for_smile")
       
    try:
        if call.data=="translate":
            if len(msg)<400:
                response=translate(msg)
                read=open_file("count/count.txt","r",return_type="read")
                read=int(read)+1
                read=str(read)
                open_file("count/count.txt","w",text_for_write=read)
            else:
                response="Matn 400 belgidan oshmasligi kerak."
            bot.edit_message_text(f"`{response}`",call.message.chat.id,call.message.id,reply_markup=share_button)
        elif call.data=="shrift":
            if len(msg)<30:
                bot.edit_message_text(msg,call.message.chat.id,call.message.id,reply_markup=shrift_button1)
            else:
                bot.send_message(call.message.chat.id,"*Matn shriftini o'zgartirish uchun matn belgilari 30 tadan oshmasligi kerak.❗*")
        elif call.data=="item1":
                text=get("item1",msg)
                bot.edit_message_text(f"`{text}`",call.message.chat.id,call.message.id,reply_markup=shrift_button1)   
        elif call.data=="item2":
                text=get("item2",msg)
                bot.edit_message_text(f"`{text}`",call.message.chat.id,call.message.id,reply_markup=shrift_button1)
        elif call.data=="item3":
                text=get("item3",msg)
                bot.edit_message_text(f"`{text}`",call.message.chat.id,call.message.id,reply_markup=shrift_button1)
        elif call.data=="item4":
                text=get("item4",msg)
                bot.edit_message_text(f"`{text}`",call.message.chat.id,call.message.id,reply_markup=shrift_button1)
        elif call.data=="decoration":
                bot.edit_message_reply_markup(call.message.chat.id,call.message.id,reply_markup=shrift_button2)
        elif call.data=="smile":
                text=add_item(call.message.text,"items")
                bot.send_message(call.message.chat.id,f"`{text}`",reply_markup=delete_button_for_smile)
        elif call.data=="stylish":
                text=add_item(call.message.text,"decoration_items")
                bot.send_message(call.message.chat.id,f"`{text}`",reply_markup=delete_button_for_smile)
        elif call.data=="back":
                bot.edit_message_text(f"{msg}",call.message.chat.id,call.message.id,reply_markup=shrift_button1)
        elif call.data=="delete":
                bot.delete_message(call.message.chat.id,call.message.id)
        elif call.data=="orqaga":
                bot.edit_message_text(msg,call.message.chat.id,call.message.id,reply_markup=main_button)
        elif call.data=="main_back":
                bot.edit_message_text(msg,call.message.chat.id,call.message.id,reply_markup=main_button)        #admin_panel
        elif call.data=="oddiyxabar":
                        with open ("admin.txt","w") as file:
                            file.write("oddiyxabar")
                        bot.edit_message_text(f"*Xabar yuboring:*",call.message.chat.id,call.message.id,reply_markup=cancel_button)
        elif call.data=="forwardxabar":
                    with open ("admin.txt","w") as file:
                        file.write("forward")
                    bot.edit_message_text(f"*Forward xabar yuboring:*",call.message.chat.id,call.message.id,reply_markup=cancel_button)
        elif call.data=="rassilka":
                    with open ("admin.txt","w") as file:
                        file.write("rassilka")
                    bot.edit_message_text(f"*Quyidagi formatda rassilka yuboring:\nrasm linki+rasm sarlavhasi+tugma nomi+tugma manzili*",call.message.chat.id,call.message.id,reply_markup=cancel_button)    
        elif call.data=="cancel":
                    with open ("admin.txt","w") as file:
                        file.write("")
                    bot.delete_message(call.message.chat.id,call.message.id)
                    bot.send_message(call.message.chat.id,"*Bekor qilindi*")
        elif call.data=="admin_back":
               bot.edit_message_text("*Asosiy panel.*",call.message.chat.id,call.message.id, reply_markup=main_admin_button)
        elif call.data=="back":
                bot.edit_message_text("*Asosiy menyu*",call.message.chat.id,call.message.id, reply_markup=shrift_button1)
                
    except :
         bot.send_message(call.message.chat.id,"*Xatolik yuz berdi.Yana bir bor urinib ko'ring.*")
         


bot.polling()

