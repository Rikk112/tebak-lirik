from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

pertanyaan = [
    {"soal": "I can see my sweet boy swayin'", "jawaban": "He's crazy y cubano como yo, la-la"},
    {"soal": "Word to all my friends":, "jawaban": "With their red flags, their white knights"},
    {"soal": "I'm gonna swing from the chandelier...", "jawaban": "from the chandelier"}
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_soal")
def get_soal():
    soal = random.choice(pertanyaan)
    return jsonify(soal=soal["soal"])

@app.route("/cek_jawaban", methods=["POST"])
def cek_jawaban():
    data = request.get_json()
    jawaban = data.get("jawaban", "").lower()
    soal = data.get("soal", "")
    kunci = next((p["jawaban"] for p in pertanyaan if p["soal"] == soal), "")
    benar = jawaban.strip() == kunci.lower()
    return jsonify(benar=benar, jawaban_benar=kunci)

if __name__ == "__main__":
    app.run()
