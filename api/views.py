from flask import Blueprint, jsonify
from utils import Utils
import logging
from constance import PATH_POSTS_FILE

api_blueprint = Blueprint('api_blueprint', __name__)

# получение пользовательского логгера и установка уровня логирования
py_logger = logging.getLogger(__name__)
py_logger.setLevel(logging.INFO)

# настройка обработчика и форматировщика в соответствии с нашими нуждами
py_handler = logging.FileHandler("api.log", mode='w')
py_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

# добавление форматировщика к обработчику
py_handler.setFormatter(py_formatter)
# добавление обработчика к логгеру
py_logger.addHandler(py_handler)


@api_blueprint.route('/api/posts/')
def posts_api():
    py_logger.info("/api/posts")
    posts = posts = Utils.get_file(PATH_POSTS_FILE)
    return jsonify(posts), 200


@api_blueprint.route('/api/posts/<int:post_id>')
def posts_id_api(post_id):
    py_logger.info(f"/api/posts/{post_id}")
    post = posts = Utils.get_post_by_pk(post_id)
    return jsonify(post), 200
