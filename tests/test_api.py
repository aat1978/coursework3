import pytest

from run import app


class TestAPI:

    # тестируем все посты
    def test_app_all_posts_status_code(self):
        """ Проверяем, получили адекватный список """
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert response.status_code == 200, "Статус код запроса всех постов неверный"

    def test_app_all_posts_type_content(self):
        """ Проверяем, правильные ли данные получены """
        response = app.test_client().get('/api/posts', follow_redirects=True)
        assert type(response.json) == list, "Получен не список"

    def test_app_all_posts_type_check_keys(self):
        """ Проверяем, правильные ли данные полученны """
        keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}
        response = app.test_client().get('/api/posts', follow_redirects=True)
        first_keys = set(response.json[0].keys())
        assert keys == first_keys, "Получены неверные ключи"
