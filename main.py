tarefas = []
proximo_id = 1

#FUNÇÃO 01: CADASTRAR TAREFA (CREATE)

def cadastrar_tarefa(titulo, prioridade):
    global proximo_id

    titulo_limpo = titulo.strip()
    if len(titulo_limpo) < 3:
        print("\n [ERRO] O título da tarefa deve ter pelo menos 3 caracteres.")
        return None

    prioridade_ajustada = prioridade.strip().upper()
    opcoes_validas = ["BAIXA", "MEDIA", "ALTA", "URGENTE"]

    if prioridade_ajustada not in opcoes_validas:
        print(
            "\n[AVISO] Prioridade inválida. Definindo automaticamente como"  "'BAIXA'" 
        )
        prioridade_ajustada = "BAIXA"

    nova_tarefa = {
        "id": proximo_id,
        "titulo": titulo_limpo,
        "prioridade": prioridade_ajustada,
        "status": "PENDENTE",
    }

    tarefas.append(nova_tarefa)
    proximo_id += 1

    return nova_tarefa 

#FUNÇÃO 02: LISTAR TAREFAS (READ)

def listar_tarefas():

    if len(tarefas) == 0:
        print("\n[INFO] Nenhuma tarefa cadastrada no momento.")
        return None
    
    print("\n--- LISTA DE TAREFAS REGISTRADAS ---")

    for tarefa in tarefas:
        print(
            f"[#{tarefa['id']}] {tarefa['titulo']} | Prioridade:"
            f" {tarefa['prioridade']} | Status: {tarefa['status']}"
        )
    
#BATERIA DE TESTES - LISTAGEM

#Cenáriio 1: Lista vazia (deve exibir aviso amigavel, sem quebrar o código)

print("=== CENÁRIO 1: LISTAGEM COM BASE VAZIA ===")
tarefas.clear()
listar_tarefas()

#Cenário 2: Lista com tarefas cadastradas

print("\n=== CENÁRIO 2: LISTAGEM COM TAREFAS REGISTRADAS ===")
cadastrar_tarefa("criar tela de login", "ALTA")
cadastrar_tarefa("Ajustar cor do botão", "BAIXA")
cadastrar_tarefa("Investigar bug crítico no checkout", "URGENTE")

listar_tarefas()

#FUNÇÃO 03: atualizar status (updade)
