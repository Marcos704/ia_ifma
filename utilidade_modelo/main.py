class Agente:
    def __init__(self, atividade):
        self.atividade = atividade

    def getAtividade(self):
        max_utilidade = float('-inf')
        melhor_atividade = None
        for atividade, utilidade in self.atividade.items():
            if utilidade > max_utilidade:
                max_utilidade = utilidade
                melhor_atividade = atividade
        return melhor_atividade

# Exemplo de usabilidade
def iniciar_agente():
    atividade = {
        "Estudar": 10,
        "Assistir TV": 5,
        "Sair com amigos": 8,
        "Dormir": 12
    }

    agente = Agente(atividade)
    obter_atividade = agente.getAtividade()
    print("Atividade escolhida pelo agente:", obter_atividade)

if __name__ == "__main__":
    iniciar_agente()
