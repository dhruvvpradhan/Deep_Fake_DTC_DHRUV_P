from flask import Flask, request, render_template
from utils.predict import predict_video
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""

    if request.method == "POST":
        file = request.files["video"]
        path = os.path.join("uploads", file.filename)
        file.save(path)

        result = predict_video(path)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
