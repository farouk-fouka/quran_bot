# Quran Bot بوت القرآن

## Overview

This bot is designed to send random Quranic content to a user or a specified Telegram channel. The bot offers two modes: sending a random Ayah (verse) or a random page from the Quran. Users can interact with the bot to select the desired mode and specify the destination for the content, either in the current chat or another Telegram channel.

## Features

- **Two Content Modes**: 
  - **Mode 1**: Sends a random Ayah from the Quran.
  - **Mode 2**: Sends a random page from the Quran.
  
- **Destination Options**: Users can choose to receive the content in the current chat or have the bot send the content to a different Telegram channel.

## Setup Instructions

1. **Install Dependencies**: The bot uses the `requests`, `telebot`, and `pyTelegramBotAPI` libraries. If these are not installed, the script will attempt to install them automatically.
  
2. **Environment Variables**: Create a `.env` file in the same directory as the script and add your Telegram bot key as follows:
   ```
   Bot_key=YOUR_TELEGRAM_BOT_API_KEY
   ```

3. **Run the Bot**: Simply execute the script, and the bot will start listening for user commands and interactions on Telegram.

## How It Works

1. **Start Command**: When the user sends the `/start` command, the bot greets the user and presents an inline keyboard with two options:
   - **Mode 1**: Sends a random Ayah.
   - **Mode 2**: Sends a random Quran page.

2. **Mode Selection**: Based on the user's selection, the bot will remember the chosen mode.

3. **Destination Selection**: The bot then asks whether to send the messages to the current chat or another Telegram channel. If the user selects another channel, the bot asks for the channel ID and reminds the user to add the bot as an admin to that channel.

4. **Content Delivery**: After the setup is complete, the bot continuously sends random content every 24 hours based on the selected mode. The interval is set to 24 hours (in the code, it's set as `sleep(10)` for demonstration purposes, but this should be changed to `sleep(86400)` for actual use).

5. **Random Ayah**: When sending a random Ayah, the bot uses the Al-Quran API to fetch a random Ayah's text, Surah name, and Surah number. It then sends the Ayah to the chat or channel along with a randomly selected emoji for variety.

6. **Random Quran Page**: The bot randomly selects a Quran page number and sends an image of that page to the chat or channel.

## API Usage

- **api.alquran.cloud API**: Used to retrieve a random Ayah and its associated Surah details.
- **alquran.vip API**: Provides images of Quran pages.

## Customization

You can customize the interval for content delivery by adjusting the `sleep()` function in the `start_sending()` method. The current setup sends content every 10 seconds for testing purposes. Change it to `86400` for daily messages.

## Note

For the bot to send messages to a channel, ensure that the bot is added as an admin to the channel.
## Note 2 
maybe I'll translate the guide part to Arabic if someone need it or if this gets some attention who knows.you can ask if you need anything 
أي شخص يريد مساعدة في شيء يمكن طرحها في "المشاكل"
في المستقبل ربما سوف أترجم خطوات الإستعمال إذا كان هناك أحد مهتم بالبوت
## License

This project is licensed under the MIT License.
Big thanks to @oorog on telegram and the Api providers 

## Contribution

Feel free to open issues or pull requests if you want to contribute or report bugs.