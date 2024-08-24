from package.maths.ponto import Ponto
import os



class Menu:
    def exibir_menu1(self):
        os.system("clear")
        print("Olá! Seja bem-vindo(a) à Calculadora de Formas!")
        print()
        print("1) CRIAR NOVA FORMA")
        print("2) VER FORMAS DISPONIVEIS")
        print("3) DISTANCIA ENTRE PONTOS")
        print()
        print("Digite o número da opção:")

    def exibir_menu2(self):
        print("------------------------------")
        print("1) VOLTAR AO MENU INICIAL")
        print("2) ENCERRAR")

        menu2input = input()

        if menu2input == '1':
            return True
        else:
            return False

class FormaManager:
    def exibir_formas_disponiveis(self):
        formas = ['CIRCULO', 'RETANGULO', 'TRIANGULO', 'SEGMENTO']
        print("Formas disponíveis para criação e uso:")
        print()
        for i, forma in enumerate(formas, start=1):
            print(f"{i}) {forma}")
        print()
    



class Util:

    @staticmethod
    def exibir_erro():
        print("ERRO! Opção inválida")
        print()
        menu = Menu()
        continuar = menu.exibir_menu2()
        return continuar

    @staticmethod
    def verificar_interferencia(forma):
        interSelection = input("Deseja checar uma interferência? (SIM/NAO): ").upper()
        if interSelection == 'SIM':
            ponto3 = input("Digite as coordenadas do ponto que deseja checar (x,y): ")
            x, y = Ponto.coordenadas(ponto3)
            ponto3 = Ponto(x, y)
            forma.Interferencia(ponto3)
        else:
            print("Verificação de interferência cancelada.")



