from flask import Flask, render_template, request,jsonify, make_response
from digitRecognizer import process_predict

app = Flask(__name__)


@app.route("/helthcheck",methods=["GET"])
def status_check():
    try:
        return jsonify({"status": True, "data": {} , "message":"api is running" })
    except Exception as e:
        print(e)
        return jsonify({"status": False, "data": {} , "message":"Error, couldn't fetch the data" })

@app.route("/predict",methods=["POST"])
def predict():
    try:
        image = request.files['image'].read()
        res = process_predict(image)
        return jsonify({"status": True, "data": { "digit": res[0] } , "message":"api is running" })
    except Exception as e:
        print(e)
        return jsonify({"status": False, "data": {} , "message":"Error, couldn't fetch the data" })

@app.errorhandler(404)
def resource_not_found(e):
    return make_response(jsonify(error='Not found!'), 404)

if __name__=="__main__":
    app.run("0.0.0.0",debug=True, port=5051)
    
