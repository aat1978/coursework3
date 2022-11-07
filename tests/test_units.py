import pytest
from utils import Utils


class TestUtils:

    @staticmethod
    def test_get_posts_all():

        with pytest.raises(FileNotFoundError):
            Utils.get_posts_all('test..json')

    @staticmethod
    def test_get_posts_by_user():

        assert len(Utils.get_posts_by_user("hank")) == 2, "Посты по имени, неверно"

        with pytest.raises(FileNotFoundError):
            Utils.get_posts_all('test..json')

