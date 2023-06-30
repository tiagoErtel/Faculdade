# RU: 3922907

import math

class Calculadora:
    def __init__(self):
        self.numero1 = None
        self.numero2 = None

    def obter_numeros(self):
        self.numero1 = self.obter_numero("Digite o primeiro número: ")
        self.numero2 = self.obter_numero("Digite o segundo número: ")

    def obter_numero(self, mensagem):
        ru = input(mensagem)
        if ru == "0":
            print("O número zero será alterado para 5, pois é o que o exercício está pedindo")
            return 5
        return int(ru)

    def menu(self):
        print("-=-" * 10)
        print("Selecione a operação:")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Expoente")
        print("6. Resto")
        print("7. Raiz quadrada da soma dos dois números")
        print("0. Sair")
        print("-=-" * 10)

    def executar(self):
        while True:
            self.obter_numeros()
            self.menu()
            opcao = input("Digite a opção desejada: ")
            if opcao == "0":
                break
            elif opcao == "1":
                resultado = self.soma()
            elif opcao == "2":
                resultado = self.subtracao()
            elif opcao == "3":
                resultado = self.multiplicacao()
            elif opcao == "4":
                resultado = self.divisao()
            elif opcao == "5":
                resultado = self.expoente()
            elif opcao == "6":
                resultado = self.resto()
            elif opcao == "7":
                resultado = self.raiz_quadrada_da_soma()
            else:
                print("Opção inválida. Digite novamente.")
                continue

            print("Resultado: ", resultado)
            print("-=-" * 10)

    def soma(self):
        return self.numero1 + self.numero2

    def subtracao(self):
        return self.numero1 - self.numero2

    def multiplicacao(self):
        return self.numero1 * self.numero2

    def divisao(self):
        return self.numero1 / self.numero2

    def expoente(self):
        return self.numero1 ** self.numero2

    def resto(self):
        return self.numero1 % self.numero2

    def raiz_quadrada_da_soma(self):
        return math.sqrt(self.numero1 + self.numero2)

# Teste da calculadora
calculadora = Calculadora()
calculadora.executar()