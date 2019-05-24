import telegram
import os
from datetime import datetime
from random import choice

chats = set()

bot = telegram.Bot(token='asdasdasdasdads')

init = datetime.now()
atual = 0
run_find, run_send = False, False
while True:
    duration = datetime.now() - init
    if duration.seconds > atual:
        print(f"Tempo: {atual}s")
        atual = duration.seconds
        run_find, run_send = False, False

    if atual%60 == 0 and run_find == False:
        print("find users")
        for update in bot.get_updates():
            chat_id = update.message.chat.id
            if chat_id in chats:
                continue        
            username = update.message.chat.username
            bot.send_message(chat_id, f"Você foi adicionado! {username}")
            chats.add(chat_id)
        run_find = True
    
    if atual%1800 == 0 and run_send == False:
        print("Send photo")
        image = choice(os.listdir('images'))
        for chat_id in chats:
            try:
                bot.send_photo(chat_id, photo=open(f'images/{image}', 'rb'))
            except telegram.error.BadRequest:
                print("Send photo went wrong")
                bot.send_photo(chat_id, photo=open(f'cat.jpeg', 'rb'))
            except telegram.error.NetworkError:
                print("Internet error")
                bot.send_message(chat_id, f"Não foi possivel enviar uma imagem agora, mais tarde tentaremos de novo!")


        run_send = True

