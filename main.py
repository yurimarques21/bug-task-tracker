tarefas = []
proximo_id = 1

def cadastrar_tarefa(titulo, prioridade):
    global proximo_id

    titulo_limpo = titulo.strip()
    if len(titulo_limpo) < 3:
        print("\n [ERRO] O título da tarefa deve ter pelo menos 3 caracteres.")
        return None

    prioridade_ajustada = prioridade.strip().upper()
    opcoes_validas = ["BAIXA", "MEDIA", "ALTA"]

    if prioridade_ajustada not in opcoes_validas:
        print(
            "\n[AVISO] Prioridade inválida. Definindo automaticamente como"  "'BAIXA'" 
        )
        prioridade_ajustada = "BAIXA"
        