from flask import Flask

# __name__ = "__main__"
app = Flask(__name__)

# Primeira rota
@app.route("/")
def hello_world():
    return "Hello World!"

@app.route("/about")
def about():
    return "Página sobre"

# Só executa o servidor se o programa for iniciado de forma manual
# Utilizado apenas no modo de desenvolvimento
# N utlizar no modo de produção
if __name__ == "__main__":
    app.run(debug=True)




