import json
import string
from json import JSONDecodeError
import logging
from constance import PATH_POSTS_FILE, PATH_COMMENTS_FILE


class Utils:
    def __init__(self):
        pass

    @staticmethod
    def get_file(path):
        """
        возвращает посты
        :return:
        """
        posts = []
        try:
            with open(path, 'r', encoding='utf-8') as file:
                posts = json.load(file)
        except FileNotFoundError:
            logging.error('Файл не найден')
        except JSONDecodeError:
            logging.error('Файл не удается преобразовать')
        return posts

    @staticmethod
    def get_posts_by_user(user_name):
        """
        возвращает посты определенного пользователя
        :param user_name:
            ValueError - такого пользователя нет
            ListEmpty - у пользователя нет постов
        :return:
        """
        post_by_user = []
        is_user = False
        posts = Utils.get_file(PATH_POSTS_FILE)
        for post in posts:
            if user_name.lower() in post['poster_name'].lower():
                is_user = True
                post_by_user.append(post)

        if  post_by_user is None:
            raise Exception("У пользователя нет постов")

        return post_by_user

    @staticmethod
    def get_comments_by_post_id(post_id):
        """
        возвращает комментарии определенного поста
        :param post_id:
        :return: ValueError - такого поста нет
                 пустой список - у поста нет комментов
        """
        comments_by_post = []
        comments = Utils.get_file(PATH_COMMENTS_FILE)
        for comment in comments:
            if post_id == comment['post_id']:
                comments_by_post.append(comment)
        if comments_by_post is None:
            raise Exception("Нет поста или у поста нет комментов")
        return comments_by_post

    @staticmethod
    def search_for_posts(query):
        """
        возвращает список постов по ключевому слову
        :param query: 
        :return: 
        """
        posts_by_word = []
        posts = Utils.get_file(PATH_POSTS_FILE)
        for post in posts:
            s = ''.join(filter(lambda x: x not in string.punctuation, post['content'].lower()))
            if query.lower() in s.split(' '):
                posts_by_word.append(post)
        return posts_by_word

    @staticmethod
    def get_post_by_pk(pk):
        """
        возвращает один пост по его идентификатору
        :param pk: 
        :return: 
        """
        posts = Utils.get_file(PATH_POSTS_FILE)
        for post in posts:
            if pk == post['pk']:
                return post

