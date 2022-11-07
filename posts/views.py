from flask import Blueprint, render_template
from utils import Utils
from constance import PATH_POSTS_FILE

posts_blueprint = Blueprint('posts_blueprint', __name__, template_folder='templates', url_prefix='/')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@posts_blueprint.route('/')
def posts_page():
    posts = Utils.get_file(PATH_POSTS_FILE)
    bookmark_number = len(posts)
    return render_template("index.html", posts=posts, bookmark_number=bookmark_number)
