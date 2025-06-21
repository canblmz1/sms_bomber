from flask import Flask, render_template, request, jsonify
import threading
import time
import random
import os

app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)

status = {
    "sent": 0,
    "failed": 0,
    "total": 0,
    "log": []
}

def send_sms(phone, message):
    # Dummy: %70 başarıyla SMS göndermiş gibi yapar
    return random.random() < 0.7

def start_bombing(phone, message, count):
    global status
    status = {"sent": 0, "failed": 0, "total": count, "log": []}
    for i in range(count):
        success = send_sms(phone, message)
        time.sleep(0.5)
        if success:
            status["sent"] += 1
            status["log"].append({"no": i+1, "status": "Başarılı"})
        else:
            status["failed"] += 1
            status["log"].append({"no": i+1, "status": "Başarısız"})

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        phone = request.form["phone"]
        message = request.form["message"]
        count = int(request.form["count"])
        thread = threading.Thread(target=start_bombing, args=(phone, message, count))
        thread.start()
        return render_template("index.html", status="SMS gönderimi başlatıldı!")
    return render_template("index.html", status="")

@app.route("/status")
def bombing_status():
    return jsonify(status)

if __name__ == "__main__":
    if not os.path.exists("templates"):
        os.makedirs("templates")
    if not os.path.exists("static"):
        os.makedirs("static")
    app.run(debug=True)