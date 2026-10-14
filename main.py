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

""" print("\n=== CENÁRIO 2: LISTAGEM COM TAREFAS REGISTRADAS ===")
cadastrar_tarefa("criar tela de login", "ALTA")
cadastrar_tarefa("Ajustar cor do botão", "BAIXA")
cadastrar_tarefa("Investigar bug crítico no checkout", "URGENTE")
 """
listar_tarefas()

#FUNÇÃO 03: atualizar status (updade)

def atualizar_status(id_tarefa, novo_status):
    status_ajustados = novo_status.strip().upper()
    status_validos = ["PENDENTE", "EM_PROGRESSO", "CONCLUIDO"]

    if status_ajustados not in status_validos:
        print(
            f"\n[ERRO] Status '{novo_status}' Invalido. Opções permitidas:"
            f"{status_validos}"
        )
        return None
    for tarefa in tarefas:
        if tarefa["id"] == id_tarefa:
            tarefa["status"] = status_ajustados
            print(f"\n[SUCESSO] Status da tarefa #{id_tarefa}atualizado para {status_ajustados}")
            return None
    print(f"\n[ERRO] Tarefa com ID #{id_tarefa} não foi encontrada.")
    return None 

# ==========================================
# BATERIA DE TESTES - ATUALIZAÇÃO
# ==========================================
tarefas.clear()

# Preparação da base
cadastrar_tarefa("Criar tela de login", "ALTA")
cadastrar_tarefa("Ajustar cor do botão", "BAIXA")

print("\n--- BASE INICIAL ---")
listar_tarefas()

# Teste 1: Atualização com sucesso (Caminho feliz)
print("\n--- TESTE 1: ALTERAÇÃO VÁLIDA ---")
atualizar_status(1, "EM_PROGRESSO")

# Teste 2: Status inexistente (Regra de validação)
print("\n--- TESTE 2: STATUS INVÁLIDO ---")
atualizar_status(1, "FINALIZADO_ONTEM")

# Teste 3: ID que não existe na base (Tratamento de erro)
print("\n--- TESTE 3: ID INEXISTENTE ---")
atualizar_status(99, "CONCLUIDO")

print("\n--- RESULTADO FINAL DA BASE ---")
listar_tarefas()