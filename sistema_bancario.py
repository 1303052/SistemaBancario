
class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de €{valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido.")

    def levantar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Levantamento de €{valor:.2f} realizado com sucesso.")
        else:
            print("Valor de levantamento inválido ou saldo insuficiente.")

    def atualizar_titular(self, novo_nome):
        self.titular = novo_nome
        print(f"Titular atualizado para {novo_nome}.")

    def mostrar_saldo(self):
        print(f"Titular: {self.titular} | Saldo: €{self.saldo:.2f}")

def menu():
    conta = ContaBancaria(input("Insira o nome do titular: "))

    while True:
        print("\n--- Menu ---")
        print("1. Depositar")
        print("2. Levantar")
        print("3. Atualizar Titular")
        print("4. Mostrar Saldo")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            valor = float(input("Valor a depositar: "))
            conta.depositar(valor)
        elif escolha == '2':
            valor = float(input("Valor a levantar: "))
            conta.levantar(valor)
        elif escolha == '3':
            novo_nome = input("Novo nome do titular: ")
            conta.atualizar_titular(novo_nome)
        elif escolha == '4':
            conta.mostrar_saldo()
        elif escolha == '5':
            print("A sair do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
