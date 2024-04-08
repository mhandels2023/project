from flask import Flask
from app.routes import configure_routes
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

configure_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
