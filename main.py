from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite3"
# app.secret_key = "733091110c9f248ebcceba9255ce0f9cf185df470d54e8f5e5eda44643d5f3d7"


@app.route("/")
def root():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
