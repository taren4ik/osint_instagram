import os
import shutil
import time
from instagrapi import Client
# from python_wireguard import Client as vpn_client, ServerConnection, Key


from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('NAME')
PASSWORD = os.getenv('PASSWORD')
# PRIVATE = os.getenv('PRIVATE')
# LOCAL_IP = os.getenv('LOCAL_IP')
# PUBLIC = os.getenv('PUBLIC')
# ENDPOINT = os.getenv('ENDPOINT')
# PORT = os.getenv('PORT')


# def vpn_connection():
#     """Start connection."""
#
#     client = vpn_client('wg-client', PRIVATE, LOCAL_IP)
#     server_conn = ServerConnection(Key(PUBLIC), ENDPOINT, PORT)
#     client.set_server(server_conn)
#
#     if client.connect():
#         status = 200
#         print("Соединение установлено успешно")
#     else:
#         status = 500
#         print("Не удалось подключиться к VPN")
#     return status


def main():
   # vpn_connection()

    cl = Client()
    # cl.load_settings("session.json")
    cl.delay_range = [1, 3]
    cl.login(USERNAME, PASSWORD)
    cl.dump_settings("session.json")



   # info_channel = cl.user_info_by_username('freedomlegionrussia').pk
    info_channel = cl.user_info_by_username('russianvolcorps').text
    #my_account = cl.account_info().dict() # моя информация
    # followers = cl.user_followers(info_channel.pk)
    # following = cl.user_following(info_channel.pk)
    # user_info = cl.user_info(cl.user_id) # развернутая информация по пользователям

    all_post = cl.user_medias(info_channel.pk) # посты пользователя списком
    for post in all_post:
        id = post.pk
        location = post.location()
        date = post.taken_at
        comments = cl.media_comments(id)  # комменты к посту

    path = os.getcwd() +  r"\config"  #Убираем каталог config от прошлой
   # nсессии
    shutil.rmtree(path)


if __name__ == "__main__":
    main()
