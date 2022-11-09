from flask import Blueprint, request, render_template
from utils import Utils

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates', url_prefix='/search')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@search_blueprint.route('/')
def search_page():
    s = request.args.get('s')
    posts = Utils.search_for_posts(s)
    posts_number = len(posts)
    return render_template("search.html", posts=posts, posts_number=posts_number)

