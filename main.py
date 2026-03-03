from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import dotenv_values
env = dotenv_values(".env")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
app.secret_key = env["SECRET_KEY"]


@app.route("/")
def root():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
