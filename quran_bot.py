
import os
from dotenv import load_dotenv
try:
    import requests, telebot
    from telebot import *
    import random
    from time import *
except ModuleNotFoundError:
    os.system('pip install requests')
    os.system('pip install telebot')
    os.system('pip install pyTelegramBotAPI')
load_dotenv()
bot_key=os.getenv("Bot_key")
bot = telebot.TeleBot(bot_key)

# Global variables to track the mod
selected_mode = None
send_to_current_chat = False



emoji_list = ['🤎', '🤍', '🩶', '🖤', '❤️', '🧡', '💛', '💚', '🩵', '💙', '🥀' , '💜' , '🤎' , '🌹' , '✨']

@bot.message_handler(commands=['start'])
def start(message):
    id = message.from_user.id
    name = message.from_user.first_name
    key = types.InlineKeyboardMarkup()
    
    
    mode_1 = types.InlineKeyboardButton('الوضع 1 : آية عشوائية 💜', callback_data='mode_1')
    mode_2 = types.InlineKeyboardButton('الوضع 2 : صفحة من القرآن🤍', callback_data='mode_2')
    mode_3 = types.InlineKeyboardButton("الوضع 3 : حديث عشوائي من صحيح البخاري🖤",callback_data="mode_3")
    
    key.add(mode_1)
    key.add(mode_2)
    key.add(mode_3)
    
    bot.send_message(message.chat.id, f"مرحباً {name}, أهلا بك في بوت القرآن الكريم ،إختر الوضع:", 
                     reply_markup=key)

@bot.callback_query_handler(func=lambda call: call.data in ['mode_1', 'mode_2',"mode_3"])
def mode_selection(call):
    global selected_mode
    if call.data == "mode_1":
        selected_mode = "ayah"
    elif call.data == "mode_2":
        selected_mode = "page"
    elif call.data == "mode_3":
        selected_mode = "hadith"
    ask_destination(call.message)

def ask_destination(message):
    key = types.InlineKeyboardMarkup()
    
    # what channel the bot sends_في أي قناة يرسل لك البوت
    option_current_chat = types.InlineKeyboardButton('إرسال هنا', callback_data='current_chat')
    option_another_channel = types.InlineKeyboardButton('إرسال إلى قناة أخرى', callback_data='another_channel')
    
    key.add(option_current_chat)
    key.add(option_another_channel)
    
    bot.send_message(message.chat.id, "هل تريد أن يرسل لك البوت هنا أو في قناة أخرى؟", 
                     reply_markup=key)

@bot.callback_query_handler(func=lambda call: call.data in ['current_chat', 'another_channel'])
def destination_selection(call):
    global send_to_current_chat
    if call.data == "current_chat":
        send_to_current_chat = True
        bot.send_message(call.message.chat.id, "سيتم إرسال الرسائل هنا")
        start_sending(call.message.chat.id)
    elif call.data == "another_channel":
        send_to_current_chat = False
        bot.send_message(call.message.chat.id, "قم بوضع البوت كمسؤول و أرسل ID القناة.من فضلك")
        bot.register_next_step_handler(call.message, get_channel_id)

def get_channel_id(message):
    channel_id = message.text
    bot.send_message(message.chat.id, "تم إضافة القناة الخاصة بك سوف يتم إرسال الرسائل تلقائيا ")
    start_sending(channel_id)

def start_sending(chat_id):
    while True:
        if selected_mode == "ayah":
            send_random_ayah(chat_id)
            sleep(1800)#half hour
        elif selected_mode == "page":
            send_random_quran_page(chat_id)
            sleep(43200)#12hours
        elif selected_mode == "hadith":
            send_random_hadith(chat_id)
            sleep(14400) #4hours
        #sleep(10)  

def send_random_ayah(chat_id):
    random_emoji = random.choice(emoji_list)
    random_ayah_number = random.randint(1, 6236)
    api_url = f"https://api.alquran.cloud/v1/ayah/{random_ayah_number}/image"
    response = requests.get(api_url)
    if response.status_code == 200:
        req = response.json()['data']
        aih = req['text']
        surah = req['surah']['number']
        surah_name = req['surah']['name']
        
        key = types.InlineKeyboardMarkup()
        bot14 = types.InlineKeyboardButton(f'{surah_name} : {surah}', callback_data='ayah_info')
        key.add(bot14)
        
        # Random emoji 
        
        bot.send_message(chat_id, text=f"<strong> ( {aih} ) {random_emoji}</strong>", parse_mode="html",
                         reply_markup=key)

def send_random_quran_page(chat_id):
    random_page_number = random.randint(1, 604)
    page_url = f"https://alquran.vip/APIs/quran-pages/{random_page_number}.png"
    
    bot.send_photo(chat_id, photo=page_url, caption=f"Quran Page {random_page_number}")



def send_random_hadith(chat_id):
    random_emoji = random.choice(emoji_list)
    random_hadith_number = random.randint(1, 7008)
    hadith_url = f"https://api.hadith.gading.dev/books/bukhari/{random_hadith_number}"

    try:
        response = requests.get(hadith_url)
        
        if response.status_code == 200:
            req = response.json()['data']['contents']
            hadith_number = req['number']
            arabic_text = req['arab']
            
            key = types.InlineKeyboardMarkup()
            bot_button = types.InlineKeyboardButton(f"صحيح البخاري رقم : {hadith_number}", callback_data='hadith_info')
            key.add(bot_button)
            
            
            bot.send_message(chat_id, text=f"(<strong> {arabic_text}){random_emoji}</strong>", 
                             parse_mode="html", reply_markup=key)
            
        elif response.status_code == 400:
            print("Error in Hadith API: Bad request")
        else:
            print(f"Error: Received unexpected status code {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error during API request: {e}")

# Example usage


bot.infinity_polling()
