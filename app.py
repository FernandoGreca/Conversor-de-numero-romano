from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/inteiro', methods=['POST'])
def submit_int():
    try:
        num = int(request.form['inteiro'])
        if num > 3999:
            maior = "NUMERO FORNECIDO MAIOR QUE 3999!!"
            return render_template("index.html", erro_int=maior)
        return int_to_roman(num)
    except ValueError:
        erro = "INFORME UM VALOR VALIDO!!"
        return render_template("index.html", erro_int=erro)
    
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


@app.route('/romano', methods=['POST'])
def submit_romano():
    try:
        num = request.form['romano']
        return roman_to_int(num)
    except ValueError:
        erro = "INFORME UM VALOR VALIDO!!"
        return render_template("index.html", erro_romano=erro)
    
def roman_to_int(s):
    def remover_caracteres(frase, caractere):
        indice = frase.find(caractere)  # Encontra a primeira ocorrência do caractere
        if indice != -1:  # Se o caractere for encontrado na frase
            frase = frase[:indice] + frase[indice+len(caractere):]  # Remove o caractere encontrado
        return frase

    def possui_caractere(string, caractere):
        return caractere in string

    def romano_para_decimal(num):
        # Lista de pares de valores e símbolos romanos, incluindo as exceções
        valores_romanos = [
            ("CM", 900), ("CD", 400), ("XC", 90), ("XL", 40), ("IX", 9), ("IV", 4),
            ("M", 1000), ("D", 500), ("C", 100), ("L", 50), ("X", 10), ("V", 5), ("I", 1)
        ]

        n_inteiro_convertido = 0
        frase = num
        
        for simbolo, valor in valores_romanos:
            while possui_caractere(frase, simbolo):
                frase = remover_caracteres(frase, simbolo)
                n_inteiro_convertido += valor

        return n_inteiro_convertido

    
    n_inteiro_convertido = romano_para_decimal(s)

    if n_inteiro_convertido > 3999:
        maior = "NUMERO FORNECIDO MAIOR QUE 3999!!"
        return render_template("index.html", erro_romano=maior)
   
    return render_template("index.html", n_inteiro_convertido = n_inteiro_convertido)

if __name__ == '__main__':
    app.run(debug=True)