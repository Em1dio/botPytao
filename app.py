from flask import Flask
import random
app = Flask(__name__)

valor = {}

@app.route('/')
def main():
    return str(valor)

@app.route('/pytao-top3')
def top3():
    my_keys = sorted(valor, key=valor.get, reverse=True)[:3]
    return f"O Filosofo Pytao congratula o top3 de hoje: {'-'.join(my_keys)}"

@app.route('/pytao-clear')
def cleanValor():
    valor.clear()
    return "Que comece a filosofia de Pytao :)"

@app.route('/pytao/<name>')
def pomba(name):
    if name not in valor:
        aleatorio = random.randint(0,100)
        valor[name] = aleatorio
    return f"{name} tem {valor[name]}cm de Pytao!"

if __name__ == '__main__':
    app.run(debug=True)
