import telebot
import os
import requests


bot = telebot.TeleBot("5729803893:AAENu5_k_0w10-rjaz2T5b8L5SPCBEEZlUk")
admin_id = 879124022
api = "1686920134QXERSKV7BDIFG2U"
usernamee = "admin"
passwordd = "killer44775566ki"
key1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
key1.add("✍️افزودن کاربر✍️","✍️حذف کاربر✍️","🔧ادیت کاربر🔧","⚙مشخصات کاربر⚙","💾تنظیم بنر💾","🪦بکاپ🪦")

@bot.message_handler(commands=["start"])
def wellcome(message):
    bot.send_message(message.chat.id, "Hi", reply_markup=key1)

@bot.message_handler()
def info(message):
    if message.chat.id == admin_id: 
        if message.text == "✍️افزودن کاربر✍️":
            msg = bot.send_message(message.chat.id, "🎃نام کاربر را وارد کنید :")
            bot.register_next_step_handler(msg, name)
        elif message.text == "✍️حذف کاربر✍️":
            mssg = bot.send_message(message.chat.id, "🎃نام کاربر را وارد کنید :")
            bot.register_next_step_handler(mssg, namede)
        elif message.text == "⚙مشخصات کاربر⚙":
            mo = bot.send_message(message.chat.id, "🎃نام کاربر را وارد کنید :")
            bot.register_next_step_handler(mo, mosh) 
        elif message.text == "💾تنظیم بنر💾":
            bot.send_message(message.chat.id,"☕️متن خود را وارد کنید :")
            bot.register_next_step_handler(message, banner)
        elif message.text == "🪦بکاپ🪦":
            bot.register_next_step_handler(message, backup)

    else:
        bot.send_message(message.chat.id, "گمشو مردک فضول👹") 

        
def name(message):
    global namek 
    namek = message.text
    msg = bot.send_message(message.chat.id, "🎃رمز کاربر را وارد کنید : ")
    bot.register_next_step_handler(msg, ramz)

def ramz(message):
    global ramzk
    ramzk = message.text
    msg = bot.send_message(message.chat.id, "🎃تعداد کاربر را وارد کنید :")
    bot.register_next_step_handler(msg, tedad)

def tedad(message):
    global tedadk
    tedadk = message.text
    msg = bot.send_message(message.chat.id, "🎃تاریخ انقضاء را وارد کنید :")
    bot.register_next_step_handler(msg, enq)

def enq(message):
    global enqk
    enqk = message.text
    msg = bot.send_message(message.chat.id, "🎃حجم مصرفی را وارد کنید : ")
    bot.register_next_step_handler(msg, trf)

def trf(message):
    global trfk
    trfk = message.text
    url = "https://ger.mrkiller90.fun:8082/api&key="+api+"&method=adduser" 
    etk = {
        "username": namek,
        "password": ramzk,
        "multiuser": tedadk,
        "traffic": trfk,
        "type_traffic Required": "gb",
        "expdate": enqk
    }
    requests.post(url,etk)
    bot.send_message(message.chat.id,"☠️your user has been created✅"+"\n💥username :" " " + namek+"\n💥password :" " " + ramzk +"\n👹multiuser :" " " + tedadk+"\n🔥traffic :" " " + trfk)


def namede(message):
    global delnamek
    delnamek = message.text
    url = "https://ger.mrkiller90.fun:8082/api&key="+api+"&method=deleteuser" 
    result = {"username": delnamek}
    requests.post(url, result)
    bot.send_message(message.chat.id,"☠️کاربر با موفقیت حذف شد✅")

def mosh(message):
    mosh_username = message.text
    url = f"https://ger.mrkiller90.fun:8082/api&key="+api+"&method=user&username={mosh_username}" 
    response = requests.get(url)
    data = response.json()["data"][0]
    if data.get("status") == 200:
        username = data["username"]
        password = data["password"]
        startdate = data["startdate"]
        expdate = data["finishdate"]
        traffic = data["traffic"]
        bot.send_message(message.chat.id, f"💀Username: {username}\n🎩 Password: {password}\n☕️ Start Date: {startdate}\n☕ Exp Date: {expdate}\n🚀 Traffic: {traffic}")
    else:
        bot.send_message(message.chat.id, "👹User not found !")

        
def banner(message):
    matnk = message.text
    f = open("banner.txt", "w+")
    f.write(matnk)
    f.close()
    bot.send_message(message.chat.id, "☠️بنر شما با موفقیت ساخته شد !✅")
def backup(message):
    os.system("mysqldump -u 'admin' --password='killer44775566ki' XPanel > /root/XPanel.sql")
    file_path = "/root/XPanel.sql"
    with open(file_path, 'rb') as f:
        file_data = f.read()
    bot.send_document(message.chat.id, file_data, visible_file_name='XPanel.sql')

	
bot.infinity_polling()