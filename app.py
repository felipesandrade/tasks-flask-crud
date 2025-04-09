from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)

# CRUD - Create, Read, Update and Delete

tasks = []
task_id_control = 1

# Rota para criação de uma task
@app.route('/tasks', methods=['POST'])
def create_task():
    # Permitindo que a variável possa ser acessada dentro do método
    global task_id_control
    # Pegando as informações passadas pelo cliente através do body em JSON
    data = request.get_json()
    # Criando um objeto da classe Task passando as informações enviadas pelo cliente e armazena na variável
    new_task = Task(id= task_id_control, title= data["title"], description= data.get("description", ""))
    # Somando 1 a variável
    task_id_control += 1
    # Adicionando a nova tarefa na lista tasks
    tasks.append(new_task)
    return jsonify({"message": "Nova tarefa criada com sucesso.", "id": new_task.id})

# Rota para obter as tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    # Cria uma lista
    task_list = []
    # Forma mais simples de fazer
    # task_list = [task.to_dict() for task in tasks]
    # Percorre as tasks existentes e adiciona na task_list
    for task in tasks:
        task_list.append(task.to_dict())

    # Formatando a saída conforme documentação 
    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
             }
    return jsonify(output)

# Rota para obter uma task específica
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    # Percorre as atividades
    for t in tasks:
        # Compara o id da atividade localizada com o passado pelo cliente por parâmetro
        if t.id == task_id:
            # Retorna no formato json a tarefa
            return jsonify(t.to_dict())

    # Retorna mensagem e o código http
    return jsonify({"message": "Tarefa não localizada."}), 404

# Rota para alterar uma tarefa
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = None
    # Percorre as tarefas
    for t in tasks:
        # Compara o id da atividade localizada com o passado pelo cliente por parâmetro
        if t.id == task_id:
            # Atribui a atividade a variável task
            task = t
            break
    # Se a task por none
    if task == None:
        # Retorna mensagem e código http
        return jsonify({"message": "Tarefa não localizada."}), 404
    # Armazena as informações enviadas no corpo da requisição na variável data
    data = request.get_json()
    # Altera o valor de title
    task.title = data['title']
    # Altera o valor de description
    task.description = data['description']
    # Altera o valor de completed
    task.completed = data['completed']
    # Retorna mesagem de tarefa alterada
    return jsonify({"message": "Tarefa alterada com sucesso."})

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def detele_tasks(task_id):
    task = None
    for t in tasks:
        if t.id == task_id:
            task = t
            break # usado para sair do loop quando localizar a task
    if task == None:
        return jsonify({"message": "Tarefa não localizada."}), 404

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada."})

# Só executa o servidor se o programa for iniciado de forma manual
# Utilizado apenas no modo de desenvolvimento
# N utlizar no modo de produção
if __name__ == "__main__":
    app.run(debug=True)




