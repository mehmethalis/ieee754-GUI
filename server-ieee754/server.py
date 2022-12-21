from flask import Flask, request
from flask_cors import CORS, cross_origin

from ieee754 import IEEE754


app = Flask(__name__)
cors = CORS(app)


@app.route("/", methods=["GET"])
def root():
    return {"message": "Works"}


@cross_origin()
@app.route("/ieee754", methods=["POST", "GET"])
def ieee754():
    if request.method == "POST":

        number = request.json["number"]
        precisionType = request.json["precisionType"]

        sign = None
        exponent = None
        mantissa = None
        pType = None

        if precisionType == "half":
            b = IEEE754(
                x=number,
                precision=0,
            )
            sign = str(b)[0]
            exponent = str(b)[1:6]
            mantissa = str(b)[6:16]
            pType = "Half Precision"
        elif precisionType == "single":
            b = IEEE754(
                x=number,
                precision=1,
            )
            sign = str(b)[0]
            exponent = str(b)[1:9]
            mantissa = str(b)[9:32]
            pType = "Single Precision"
        elif precisionType == "double":
            b = IEEE754(
                x=number,
                precision=2,
            )
            sign = str(b)[0]
            exponent = str(b)[1:12]
            mantissa = str(b)[12:64]
            pType = "Double Precision"
        elif precisionType == "quadruple":
            b = IEEE754(
                x=number,
                precision=3,
            )
            sign = str(b)[0]
            exponent = str(b)[1:16]
            mantissa = str(b)[16:128]
            pType = "Quadruple Precision"
        elif precisionType == "octuple":
            b = IEEE754(
                x=number,
                precision=4,
            )
            sign = str(b)[0]
            exponent = str(b)[1:20]
            mantissa = str(b)[20:256]
            pType = "Octuple Precision"

        def find_bias(exponent):
            return 2 ** (exponent - 1) - 1

        return {
            "data": str(b),
            "sign": sign,
            "exponent": exponent,
            "mantissa": mantissa,
            "type": pType,
            "number": number,
        }

    else:
        return {"message": "Welcome ieee754 API", "Author": "haliscicek.com/en"}
