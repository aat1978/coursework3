from flask import Blueprint, render_template
from utils import Utils

postsid_blueprint = Blueprint('postsid_blueprint', __name__, template_folder='templates', url_prefix='/posts')


# Создаем вьюшку, используя в декораторе блюпринт вместо app
@postsid_blueprint.route('/<int:postid>')
def postsid_page(postid):
    posts = Utils.get_comments_by_post_id(postid)
    user = Utils.get_post_by_pk(postid)
    comment_number = len(posts)
    return render_template("post.html", posts=posts, user=user, comment_number=comment_number)
