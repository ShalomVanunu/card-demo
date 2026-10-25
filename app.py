import os
import hmac
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "demo-secret-key-change-me")

# נתוני הדמיה בלבד – אינם כרטיס אשראי אמיתי
VALID_CARD = "1111222233333444"
VALID_CODE = "355"


def normalize(value: str) -> str:
    """משאיר רק ספרות (מתעלם מרווחים ומקפים)"""
    return "".join(ch for ch in (value or "") if ch.isdigit())


@app.route("/", methods=["GET", "POST"])
def index():
    error = None
    if request.method == "POST":
        card = normalize(request.form.get("card", ""))
        code = normalize(request.form.get("code", ""))

        card_ok = hmac.compare_digest(card, VALID_CARD)
        code_ok = hmac.compare_digest(code, VALID_CODE)

        if card_ok and code_ok:
            session["authenticated"] = True
            return redirect(url_for("success"))
        error = "הנתונים שהוזנו אינם נכונים. נסו שוב."
    return render_template("index.html", error=error)


@app.route("/success")
def success():
    if not session.get("authenticated"):
        return redirect(url_for("index"))
    return render_template("success.html")


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
