class TelaVacinacao():

  
    def pega_dados(self):
        print("")
        print("Informe os dados: ")
        cpf = int(input("CPF: "))
        data_de_vacinacao = input("Data de vacinação (DD/MM/YYYY): ")
        vacina = input("Nome da vacina: ")
        dose = input("Código do lote: ")
        print("")
        return {
            "cpf": cpf,
            "data_de_vacinacao": data_de_vacinacao,
            "vacina": vacina,
            "dose": dose
        }

    def mostra_mensagem(self, mensagem):
        print("")
        print(mensagem)
        print("")

    def mostra_vacinacao(self, data_de_vacinacao, doenca, lote):
        print("")
        print("Data: ", data_de_vacinacao)
        print("Doença: ", doenca)
        print("Lote: ", lote)
        print("\n")

    def pegar_cpf(self):
        return int(input("CPF: "))