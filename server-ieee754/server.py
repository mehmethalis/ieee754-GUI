from flask import Flask, request

from ieee754 import IEEE754

app = Flask(__name__)

@app.route("/", methods=[ "GET"])
def root():
    return {"message":"Works"}

@app.route("/ieee754", methods=["POST", "GET"])
def ieee754():
    if request.method == "POST":

        number = request.json["number"]
        precisionType = request.json["precisionType"]


        if(precisionType == "half"):
            b= IEEE754(
                x=number,
                precision=0,

            )
            sign = str(b)[0]
            exponent = str(b)[1:6]
            mantissa = str(b)[6:16]
        elif(precisionType == "single"):
            b= IEEE754(
                x=number,
                precision=1,
            )
            sign = str(b)[0]
            exponent = str(b)[1:9]
            mantissa = str(b)[9:32]
        elif (precisionType == "double"):
            b = IEEE754(
                x=number,
                precision=2,
            )
            sign = str(b)[0]
            exponent = str(b)[1:12]
            mantissa = str(b)[12:64]
        elif (precisionType == "quadruple"):
            b = IEEE754(
                x=number,
                precision=3,
            )
            sign = str(b)[0]
            exponent = str(b)[1:16]
            mantissa = str(b)[16:128]
        elif (precisionType == "octuple"):
            b = IEEE754(
                x=number,
                precision=4,
            )
            sign = str(b)[0]
            exponent = str(b)[1:20]
            mantissa = str(b)[20:256]


        def find_bias(exponent):
            return 2 ** (exponent -1) -1


        def result(self,b,sign,exponent,mantissa):
            self.b = b
            self.sign = sign
            self.exponent = exponent
            self.mantissa = mantissa

        return {result(str(b),sign,exponent,mantissa)}


    else:
        return {"message": "Welcome ieee754 API", "Author": "haliscicek.com/en"}
