import os
try :
    import requests,telebot
    from telebot import *
    import random
    from time import *
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install telebot')
    os.system('pip install pyTelegramBotAPI==3.7.6')

bot = telebot.TeleBot("7510163033:AAFMgB779_uSpohN69ThqPun3W8bPvcfHbg")

@bot.message_handler(commands=['start'])
def start(message):
    id = message.from_user.id
    name = message.from_user.first_name
    use = message.from_user.username
    key = types.InlineKeyboardMarkup()
    cam = types.InlineKeyboardButton('للتواصل مع مطور البوت 🗣️',url ='https://t.me/oorog')
    bot14 = types.InlineKeyboardButton(f'''
📥  اضافه قناة  📥
''',callback_data='d1')
    
    key.add(bot14)
    key.add(cam)
    bot.send_message(message.chat.id,f"""<strong>
مرحبا {name} أهلا بك في بوت القرآن الكريم 🌷.

</strong>""",parse_mode="html",reply_to_message_id=message.message_id,reply_markup=key,timeout=3.5)	
    


    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if call.data == "d1":
        	d1(message,call)
             



def d1(message,call):
    bot.send_message(message.chat.id, text=f"<strong> قم برفع البوت ادمن في قناتك ثم ارسل ايدي القناة؟</strong>",parse_mode="html",timeout=3.5)
    @bot.message_handler(func=lambda message: True)
    def start(message):
        us = message.text
        bot.send_message(message.chat.id, text=f"<strong>تم اضافة القناة إلى الإرسال التلقائي . سيتم ارسال اية قرانية عشوائيه كل 24 ساعة إلى القناة ✅</strong>",parse_mode="html",timeout=3.5)
        while True : 
            random_ayah_number = random.randint(1, 6236)
            api_url = f"https://api.alquran.cloud/v1/ayah/{random_ayah_number}/image"
            response = requests.get(api_url)
            if response.status_code == 200:
                req = response.json()['data']
                aih = req['text']
                surah = req['surah']['number']
                surah_name = req['surah']['name']
                key = types.InlineKeyboardMarkup()
                bot14 = types.InlineKeyboardButton(f'{surah_name} : {surah}',callback_data='d331')
                key.add(bot14)
                a1 = '🤎'
                a2 = '🤍'
                a3 = '🩶'
                a4 = '🖤'
                a5 = '❤️'
                a6 = '🧡'
                a7 = '💛'
                a8 = '💚'
                a9 = '🩵'
                a10 = '💙'
                all = a1,a2,a3,a4,a5,a6,a7,a8,a9,a10
                do = str(''.join((random.choice(all) for i in range(1))))
                bot.send_message(us, text=f"""<strong> ( {aih} ) {do}</strong>""",parse_mode="html",reply_markup=key,timeout=3.5)
                sleep(30)





bot.infinity_polling()