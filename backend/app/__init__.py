import bcrypt
from flask_cors import CORS
from flask import Flask
import os

from .controller.LetterController import letter
from .controller.UserController import user
from .controller.MyPageController import myPage
from .controller.oauth import kakao_login
app = Flask(__name__)
CORS(app)

os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
app.config['SECRET_KEY'] = 'd9owj3982oi8329dsh38'

app.register_blueprint(letter)
app.register_blueprint(user)
app.register_blueprint(myPage)
app.register_blueprint(kakao_login)
