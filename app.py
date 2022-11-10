from flask import Flask
from api.views import api_blueprint
from posts.views import posts_blueprint
from postsid.views import postsid_blueprint
from search.views import search_blueprint
from username.views import username_blueprint


app = Flask(__name__)


app.register_blueprint(posts_blueprint)
app.register_blueprint(postsid_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(username_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Нет такой страницы</h1>", 404


@app.errorhandler(500)
def internal_error(error):
    return "<h1>Ошибка сервера</h1>", 500


if __name__ == '__main__':
    app.run(debug=True)
