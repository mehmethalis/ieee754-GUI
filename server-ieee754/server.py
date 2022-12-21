from flask import Flask, request, jsonify

from ieee754 import IEEE754

app = Flask(__name__)

@app.route("/", methods=[ "GET"])
def root():
    return {"message":"Works"}

@app.route("/ieee754", methods=["POST", "GET"])
def ieee754():
    if request.method == "POST":

        def find_bias(exponent):
            return 2 ** (exponent - 1) - 1

        float_number = float(request.json["integer"] + "." + request.json["decimal"])

        b = IEEE754(
            float_number,
            force_length=int(request.json["length"]),
            force_exponent=int(request.json["exponent"]),
            force_mantissa=int(request.json["mantissa"]),
            force_bias=find_bias(int(request.json["exponent"])),
        )
        return jsonify(b)
    else:
        return {"message": "Welcome ieee754 API", "Author": "haliscicek.com/en"}
