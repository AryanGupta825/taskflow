import os
from flask import Flask
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

    # Configuration
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'taskflow-secret-key-2024')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'jwt-secret-taskflow-2024')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = False

    # --- Database Configuration ---
    db_url = os.environ.get('DATABASE_URL')
    
    if db_url:
        # 1. Fix the driver prefix
        if db_url.startswith("mysql://"):
            db_url = db_url.replace("mysql://", "mysql+pymysql://", 1)
        
        # 2. STRIP the 'ssl-mode' query parameter (Crucial Fix)
        # PyMySQL throws a TypeError if 'ssl-mode' is in the connection string
        if "?" in db_url:
            db_url = db_url.split("?")[0]
        
        app.config['SQLALCHEMY_DATABASE_URI'] = db_url
        
        # 3. Handle SSL manually for PyMySQL/Aiven compatibility
        app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
            "connect_args": {
                "ssl": {
                    "fake_config_to_trigger_ssl": True 
                }
            }
        }
    else:
        # Local development fallback
        db_password = quote_plus(os.environ.get('DB_PASSWORD', 'Aryan@psit123'))
        app.config['SQLALCHEMY_DATABASE_URI'] = (
            f"mysql+pymysql://{os.environ.get('DB_USER','root')}:"
            f"{db_password}@"
            f"{os.environ.get('DB_HOST','127.0.0.1')}:"
            f"{os.environ.get('DB_PORT','3307')}/"
            f"{os.environ.get('DB_NAME','taskflow')}"
        )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize Extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    
    # CORS setup
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    # Register Blueprints
    from .routes.auth import auth_bp
    from .routes.projects import projects_bp
    from .routes.tasks import tasks_bp
    from .routes.dashboard import dashboard_bp
    from .routes.frontend import frontend_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(projects_bp, url_prefix='/api/projects')
    app.register_blueprint(tasks_bp, url_prefix='/api/tasks')
    app.register_blueprint(dashboard_bp, url_prefix='/api/dashboard')
    app.register_blueprint(frontend_bp)

    # Automatically create tables in the database
    with app.app_context():
        try:
            db.create_all()
            print("Database tables verified/created successfully.")
        except Exception as e:
            print(f"Database table creation error: {e}")

    return app
