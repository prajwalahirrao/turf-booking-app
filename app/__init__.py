from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return {"message": "Turf Booking App is running!"}

    return app
