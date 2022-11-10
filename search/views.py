from flask import Blueprint, request, render_template
from utils import Utils

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates', url_prefix='/search')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@search_blueprint.route('/')
def search_page():
    posts = []
    posts_number = []
    try:
        s = request.args['s']
    except KeyError:
        logging.error('Вы ничего не ввели')
    else:
        posts = Utils.search_for_posts(s)
        posts_number = len(posts)
    finally:
        return render_template("search.html", posts=posts, posts_number=posts_number)

