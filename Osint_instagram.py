import os
import shutil
import time
from instagrapi import Client
# from python_wireguard import Client as vpn_client, ServerConnection, Key


from dotenv import load_dotenv

load_dotenv()

USERNAME = os.getenv('NAME')
PASSWORD = os.getenv('PASSWORD')
CHANNEL = 'russianvolcorps'
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
    """All function."""
   #vpn_connection()

    cl = Client()
    cl.delay_range = [2, 7]
 #   cl.load_settings("session.json")
    cl.delay_range = [1, 3]
    cl.login(USERNAME, PASSWORD)
 #   cl.get_timeline_feed()
    cl.dump_settings("session.json") #запись при мервом входе



   # info_channel = cl.user_info_by_username('freedomlegionrussia').pk
    info_channel = cl.user_info_by_username(CHANNEL)
    #my_account = cl.account_info().dict() # моя информация
    # followers = cl.user_followers(info_channel.pk)
    # following = cl.user_following(info_channel.pk)
    # user_info = cl.user_info(cl.user_id) # развернутая информация по пользователям

    all_post = cl.user_medias(info_channel.pk) # посты пользователя списком
    for post in all_post:
        id = post.id
        location = post.location
        date = post.taken_at
        text = post.caption_text
        usertags = post.usertags
        url = 'https:////www.instagram.com//p//' + post.code + '//'
        url = post.thumbnail_url
        comments = get_comment(cl, id)
        resources = post.resources

    path = os.getcwd() +  r"\config"  #Убираем каталог config от прошлой сессии
    shutil.rmtree(path)


def get_comment(pk, client):
    """
    Get comment from post.
    :param pk:
    :return:
    """

    post_id = pk
    comments = client.media_comments(post_id)

    # Вывод комментариев
    for comment in comments:
        print(comment.text)


if __name__ == "__main__":
    main()
