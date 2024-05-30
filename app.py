from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    try:
        num = int(request.form['name'])
        return int_to_roman(num)
    except ValueError:
        erro = "INFORME UM VALOR VALIDO!!"
        return render_template("index.html", erro=erro)
    
def int_to_roman(num):
    sub = num
    numero_romano = "" 

    while sub != 0:
        if sub == 4:
            numero_romano += "IV"
            sub -= 4
        elif sub == 9:
            numero_romano += "IX"
            sub -= 9
        elif sub >= 40 and sub < 50:
            numero_romano += "XL"
            sub -= 40
        elif sub >= 90 and sub < 100:
            numero_romano += "XC"
            sub -= 90
        elif sub >= 400 and sub < 500:
            numero_romano += "CD"
            sub -= 400
        elif sub >= 900 and sub < 1000:
            numero_romano += "CM"
            sub -= 900
        elif sub == 1:
            numero_romano += "I"
            sub -= 1
        elif sub < 5:
            numero_romano += "I"
            sub -= 1
        elif sub < 10:
            numero_romano += "V"
            sub -= 5
        elif sub < 50:
            numero_romano += "X"
            sub -= 10
        elif sub < 100:
            numero_romano += "L"
            sub -= 50
        elif sub < 500:
            numero_romano += "C"
            sub -= 100
        elif sub < 1000:
            numero_romano += "D"
            sub -= 500
        elif sub >= 1000:
            numero_romano += "M"
            sub -= 1000

    return render_template("index.html", n_romano_convertido = numero_romano)

if __name__ == '__main__':
    app.run(debug=True)






