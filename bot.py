import telebot
import requests
bot = telebot.TeleBot("5729803893:AAENu5_k_0w10-rjaz2T5b8L5SPCBEEZlUk")
admin_id = 879124022
key1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
key1.add("✍️افزودن کاربر✍️","✍️حذف کاربر✍️","🔧ادیت کاربر🔧","⚙مشخصات کاربر⚙")

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
    else:
        bot.send_message(message.chat.id, "You are not authorized to access these features.") 

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
    url = "https://ger.mrkiller90.fun:8082/api&key=16868401323MNEPOJF6ZG1C8T&method=adduser" 
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
    url = "https://ger.mrkiller90.fun:8082/api&key=16868401323MNEPOJF6ZG1C8T&method=deleteuser" 
    result = {"username": delnamek}
    requests.post(url, result)
    bot.send_message(message.chat.id,"☠️کاربر با موفقیت حذف شد✅")

def mosh(message):
    try:
        mosh_username = message.text
        url = f"https://ger.mrkiller90.fun:8082/api&key=16868401323MNEPOJF6ZG1C8T&method=user&username={mosh_username}" 
        response = requests.get(url)
        data = response.json()
        if data.get("status") == 200:
            username = data["data"][0]["username"]
            password = data["data"][0]["password"]
            start_date = data["data"][0]["startdate"]
            exp_date = data["data"][0]["finishdate"]
            traffic = data["data"][0]["traffic"]
            bot.sendmessage(message.chat.id, f"💀Username: {username}\n🎩 Password: {password}\n☕️ Start Date: {startdate}\n☕ Exp Date: {expdate}\n🚀 Traffic: {traffic}")
        else:
            bot.sendmessage(message.chat.id, "👹User not found !")
    except Exception:
        bot.sendmessage(message.chat.id, "Please try again later !")

bot.infinity_polling()