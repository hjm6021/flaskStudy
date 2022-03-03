from flask import Flask
from simple_page import simple_page

app = Flask(__name__)


app.register_blueprint(simple_page)


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0")
