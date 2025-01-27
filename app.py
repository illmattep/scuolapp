from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from modules.config import Config
from modules.db import db
from routes.auth import auth
from modules.config import Config
from flask_login import login_required
from flask_login import current_user


Config = Config()
app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app, db)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login'  # Set the login route
login_manager.login_message = "Please log in to access this page."

@login_manager.user_loader
def load_user(user_id):
    from modules.models import User  # Import User model here to avoid circular imports
    return User.query.get(int(user_id))


@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('home.html', user=current_user)

app.register_blueprint(auth, url_prefix='/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
