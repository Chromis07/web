from typing import Dict
from flask import Flask, jsonify, request
from flask.templating import render_template
import ml

app = Flask(__name__)

# 템플릿 자동 로딩
app.config["TEMPLATES_AUTO_RELOAD"] = True

# 브라우저 http://localhost:5000 주소로 접속하면, hello world 출력
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    expected: Dict[str, int] = {}
    # 업로드된 모든 파일에 대해서 예측
    for name, f in request.files.items():
        expected[name] = ml.predict(f)

    return jsonify({"expected": expected})
