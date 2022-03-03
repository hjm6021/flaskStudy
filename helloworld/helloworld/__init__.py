from datetime import timedelta
from flask import Flask, make_response, request, session


app = Flask(__name__)
app.config.update(
    SECRET_KEY="zbnUlPpPPvGmu3IxaQX4",
    SESSION_COOKIE_NAME="sessionName",
    PERMANENT_SESSION_LIFETIME=timedelta(31),
)


@app.route("/session_set")
def session_set():
    session["ID"] = "JPUB Flask Programming"
    session["NAME"] = "HJM"
    return "Session이 설정되었습니다."


@app.route("/session_out")
def session_out():
    del session["ID"]
    del session["NAME"]
    return "Session이 설정되었습니다."


@app.route("/session_status")
def cookie_status():
    sessionId = session["ID"] if session else "빈 문자열"
    sessionName = session["NAME"] if session else "이름 없음"
    c_response = make_response(
        "ID Cookie는 {}, {} 값을 가지고 있습니다.".format(sessionId, sessionName)
    )

    return c_response
