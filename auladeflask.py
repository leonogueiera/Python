from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/decorator') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Um decorator (ou decorador) em Python é uma função que permite adicionar novas funcionalidades a outra função ou método sem precisar modificar o seu código original.Imagine o decorator como uma "embalagem inteligente" ou um "envelope" que você coloca em volta de uma função para estender o que ela faz.' # Isso é o que será retornado quando a rota '/' for acessada


if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento