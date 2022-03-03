from models import User
from flask import Flask
from mongoengine import connect

# configuration
mongodbSettings = {"db": "test", "host": "localhost", "port": 27017}

# create the little application object
app = Flask(__name__)

# connect to the database
connect(
    db=mongodbSettings["db"], host=mongodbSettings["host"], port=mongodbSettings["port"]
)


@app.route("/")
def main():
    user = User(name="han", email="han@gmail.com")
    user.save()
    return "/"


@app.route("/get")
def get():
    nameHan = User.objects(name="han")
    fields = {"name": "modifiedHan", "email": "6021@ggmail.com"}
    nameHan.update(**fields)
    print(nameHan.to_json())

    return "get"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
