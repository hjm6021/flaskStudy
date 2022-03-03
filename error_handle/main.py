from flask import Flask, abort

# create the little application object
app = Flask(__name__)


@app.route("/error401")
def error401():
    abort(401)


@app.route("/error403")
def error403():
    abort(403)


@app.route("/error404")
def error404():
    abort(404)


@app.route("/error405")
def error405():
    abort(405)


@app.route("/error500")
def error500():
    abort(500)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
