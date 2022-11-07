from flask import Blueprint, abort, render_template
from utils import Utils

username_blueprint = Blueprint('username_blueprint', __name__, template_folder='templates', url_prefix='/users')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@username_blueprint.route('/<username>')
def username_page(username):
    users = Utils.get_posts_by_user(username)
    if len(users) == 0:
        abort(404)
    users_number = len(users)
    print(users)
    return render_template("user-feed.html", users=users, users_number=users_number)
