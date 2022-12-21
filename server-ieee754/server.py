from flask import Flask, request

from ieee754 import IEEE754

app = Flask(__name__)


@app.route("/", methods=["GET"])
def root():
    return {"message": "Works"}


@app.route("/ieee754", methods=["POST", "GET"])
def ieee754():
    if request.method == "POST":
        number = request.json["number"]
        precisionType=request.json["precisionType"]

        # force_length,
        # force_exponent,
        # force_mantissa,
        # force_bias,
        # precision=2

        # half
        # signle
        #..
        #..
        if(precisionType == "single"):





    

        def find_bias(exponent):
            return 2 ** (exponent - 1) - 1

        b = IEEE754(
            x=number,
            precision=precision,
            force_length=force_length,
            force_exponent=force_exponent,
            force_mantissa=force_mantissa,
            force_bias=force_bias,
        )

        return {"data": str(b)}
    else:
        return {"message": "Welcome ieee754 API", "Author": "haliscicek.com/en"}
