


import telebot
import io
import time
import os
import random
from telegram import InputFile
bot = telebot.TeleBot("6363836014:AAHX2Aqd_--KFxJBbNc5aEiJ9Rw6Y9oD_R4")
# Dictionary to store user-submitted GIFs
user_gifs = {}

# Specify the directory to save GIFs
GIF_SAVE_DIR = './user_gifs/'

import requests

timeout = 60  # Increase the timeout to 60 seconds
response = requests.get('https://api.telegram.org', timeout=timeout)



from requests.exceptions import ReadTimeout

max_retries = 3
retry_delay = 5  # seconds

for _ in range(max_retries):
    try:
        response = requests.get('https://api.telegram.org', timeout=25)
        # Process the response
        break  # Break out of the loop if the request succeeds
    except ReadTimeout as e:
        print(f"Timeout occurred: {e}")
        time.sleep(retry_delay)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Ohmmmmmm?")

@bot.message_handler(func=lambda message: message.text == "/stone_infidel")
def send_pee_message(message):
    print("Haram")
    username = message.from_user.username
    
    gif_path = './Haram/'
    gifs = [ '5.gif']
    random_gif = random.choice(gifs)
    bot.send_chat_action(message.chat.id, 'upload_video')
    with open(os.path.join(gif_path, random_gif), 'rb') as f:
        gif = f.read()
        bot.send_chat_action(message.chat.id, 'upload_video')
        bot.send_video_note(message.chat.id, gif, duration=5)



@bot.message_handler(func=lambda message: message.text == "/squigs")
def send_pee_message(message):
    print("Haram")
    username = message.from_user.username
    
    gif_path = './Haram/'
    gifs = [ '5.gif']
    random_gif = random.choice(gifs)
    bot.send_chat_action(message.chat.id, 'upload_video')
    with open(os.path.join(gif_path, random_gif), 'rb') as f:
        gif = f.read()
        bot.send_chat_action(message.chat.id, 'upload_video')
        bot.send_video_note(message.chat.id, gif, duration=5)


@bot.message_handler(func=lambda message: message.text == "/haram")
def send_pee_message(message):
    print("Haram")
    username = message.from_user.username
    
    gif_path = './Haram/'
    gifs = ['1.gif', '2.gif', '3.gif', '4.gif', '5.gif', '6.gif']
    random_gif = random.choice(gifs)
    bot.send_chat_action(message.chat.id, 'upload_video')
    with open(os.path.join(gif_path, random_gif), 'rb') as f:
        gif = f.read()
        bot.send_chat_action(message.chat.id, 'upload_video')
        bot.send_video_note(message.chat.id, gif, duration=5)


@bot.message_handler(commands=['haram'])
def haram_command(message):
    user_id = message.from_user.id
    if user_id in user_gifs:
        gif_location = user_gifs[user_id]
        bot.send_document(message.chat.id, open(gif_location, 'rb'))
    else:
        bot.reply_to(message, "No GIF found for you.")


@bot.message_handler(func=lambda message: message.text == "/game")
def send_pee_message(message):
    print("Haram")
    username = message.from_user.username
    random_quote = "$Stone Infidels for Profit - new utility coming soon."
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, random_quote)
  

@bot.message_handler(func=lambda message: message.text == "/pray")
def send_pee_message(message):
    print("Haram")
    username = message.from_user.username
    quotes = [
    "Verily, with hardship comes ease. – Quran, 94:6",
    "The best among you are those who have the best manners and character. – Prophet Muhammad (peace be upon him)",
    "Do good deeds properly, sincerely and moderately, and remember that your deeds will not make you enter Paradise. The most beloved deed to Allah's is the most regular and constant even though it were little. – Prophet Muhammad (peace be upon him)",
    "Whoever is not grateful for what he has, will not be grateful for what he receives. – Prophet Muhammad (peace be upon him)",
    "The strong person is not the one who can wrestle someone else down. The strong person is the one who can control himself when he is angry. – Prophet Muhammad (peace be upon him)",
    "Speak good or remain silent. – Prophet Muhammad (peace be upon him)",
    "The best jihad (struggle) is the one against the self. – Prophet Muhammad (peace be upon him)",
    "Seek knowledge from the cradle to the grave. – Prophet Muhammad (peace be upon him)",
    "None of you truly believes until he loves for his brother what he loves for himself. – Prophet Muhammad (peace be upon him)",
    "When you see a person who has been given more than you in money and beauty, look to those who have been given less. – Prophet Muhammad (peace be upon him)"
]
    
    random_quote = random.choice(quotes)
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, random_quote)
    
@bot.message_handler(commands=['add_gif'])
def add_gif_command(message):
    bot.reply_to(message, "Send me a GIF to add.")
    bot.register_next_step_handler(message, save_gif)

# Function to save user-submitted GIFs
def save_gif(message):
    user_id = message.from_user.id
    if message.content_type == 'document' and message.document.mime_type == 'video/mp4':
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)
        gif_location = os.path.join(GIF_SAVE_DIR, f'{user_id}_{len(user_gifs.get(user_id, []))}.gif')
        with open(gif_location, 'wb') as new_file:
            new_file.write(downloaded_file)
        if user_id not in user_gifs:
            user_gifs[user_id] = []
        user_gifs[user_id].append(gif_location)
        bot.reply_to(message, "GIF added successfully.")


    
@bot.message_handler(func=lambda message: message.text == "/fed")
def send_pee_message(message):
    print("Haram")
    username = message.from_user.username
    
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, "In case of an investigation by any federal entity or similar, I do not have any involvement with this group or with the Infidels in it, I do not know how I am here, probably added by a third party, My purchase of $HARAM does not show my support of any actions by the Infidels in this group.")



bot.polling()

# https://twitter.com/aut_ism_eth?s=21&t=vHfZIEc50vkOXgh2A8EJlA
# http://tism-awareness.xyz/

# https://www.dextools.io/app/en/ether/pair-explorer/0xCb925C44a7a23D604b7De72E1E23EF3b01d1ae48 