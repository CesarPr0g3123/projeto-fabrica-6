from flask import Flask, render_template, abort, url_for

app = Flask(__name__)

alunos = [
    {
        "id": 1,
        "nome":"Cesar",
        "idade": 17,
        "curso":"Python Intermediário",
        "imagem":"https://upload.wikimedia.org/wikipedia/commons/e/e3/DavidGogginsMay08.jpg"
    }
]

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/alunos")
def listar_alunos():
    return render_template('listar_alunos.html', alunos=alunos)

@app.route("/aluno/<int:aluno_id>")
def detalhe_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            return render_template('detalhe_alunos.html', aluno=aluno)
    return "aluno nao encontrado", 404

if __name__ == '__main__':
    app.run(debug=True)