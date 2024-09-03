
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

# Global variables to track the selected mode and message destination
selected_mode = None
send_to_current_chat = False

@bot.message_handler(commands=['start'])
def start(message):
    id = message.from_user.id
    name = message.from_user.first_name
    key = types.InlineKeyboardMarkup()
    
    # Option to choose between modes
    mode_1 = types.InlineKeyboardButton('Mode 1: Send Random Ayah', callback_data='mode_1')
    mode_2 = types.InlineKeyboardButton('Mode 2: Send Random Quran Page', callback_data='mode_2')
    
    key.add(mode_1)
    key.add(mode_2)
    
    bot.send_message(message.chat.id, f"Hello {name}, welcome to the Quran bot! Please choose a mode:", 
                     reply_markup=key)

@bot.callback_query_handler(func=lambda call: call.data in ['mode_1', 'mode_2'])
def mode_selection(call):
    global selected_mode
    if call.data == "mode_1":
        selected_mode = "ayah"
    elif call.data == "mode_2":
        selected_mode = "page"
    
    ask_destination(call.message)

def ask_destination(message):
    key = types.InlineKeyboardMarkup()
    
    # Option to choose where the bot will send the messages
    option_current_chat = types.InlineKeyboardButton('Send to this chat', callback_data='current_chat')
    option_another_channel = types.InlineKeyboardButton('Send to another channel', callback_data='another_channel')
    
    key.add(option_current_chat)
    key.add(option_another_channel)
    
    bot.send_message(message.chat.id, "Do you want the bot to send messages to this chat or to another channel?", 
                     reply_markup=key)

@bot.callback_query_handler(func=lambda call: call.data in ['current_chat', 'another_channel'])
def destination_selection(call):
    global send_to_current_chat
    if call.data == "current_chat":
        send_to_current_chat = True
        bot.send_message(call.message.chat.id, "Messages will be sent to this chat.")
        start_sending(call.message.chat.id)
    elif call.data == "another_channel":
        send_to_current_chat = False
        bot.send_message(call.message.chat.id, "Please add the bot as an admin in your channel, then send the channel ID:")
        bot.register_next_step_handler(call.message, get_channel_id)

def get_channel_id(message):
    channel_id = message.text
    bot.send_message(message.chat.id, "The channel has been added for automatic sending.")
    start_sending(channel_id)

def start_sending(chat_id):
    while True:
        if selected_mode == "ayah":
            send_random_ayah(chat_id)
        elif selected_mode == "page":
            send_random_quran_page(chat_id)
        sleep(10)  # 24 hours

def send_random_ayah(chat_id):
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
        emoji_list = ['🤎', '🤍', '🩶', '🖤', '❤️', '🧡', '💛', '💚', '🩵', '💙']
        random_emoji = random.choice(emoji_list)
        
        bot.send_message(chat_id, text=f"<strong> ( {aih} ) {random_emoji}</strong>", parse_mode="html",
                         reply_markup=key)

def send_random_quran_page(chat_id):
    random_page_number = random.randint(1, 604)
    page_url = f"https://alquran.vip/APIs/quran-pages/{random_page_number}.png"
    
    bot.send_photo(chat_id, photo=page_url, caption=f"Quran Page {random_page_number}")

bot.infinity_polling()
