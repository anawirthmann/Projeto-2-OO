from package.maths.terms import Forma
from package.maths.ponto import Ponto
from package.maths.controllers import Menu, FormaManager, Util
import os


def app():
    continuar = True
    while continuar:
    
        menu = Menu()
        forma = FormaManager()
        util = Util()
        minha_forma = Forma()

        ### MENU INICIAL ###

        menu.exibir_menu1()
        menuSelection = input()


        ########################### MENU OPCAO 1 (CRIAR FORMA)  ##########################

        if menuSelection == '1':
            os.system("clear") 
            forma.exibir_formas_disponiveis()
            formaSelection = input("Digite o número da forma que deseja criar:")
            minha_forma = minha_forma.criar_forma(formaSelection)

            continuar = menu.exibir_menu2()


        ##################### MENU OPCAO 2 (FORMAS DISP) ###################
        
        elif menuSelection == '2':  
            os.system("clear")
            forma.exibir_formas_disponiveis()
            continuar = menu.exibir_menu2()


        ##################### MENU OPCAO 3 (DIST ENTRE PONTOS) ###############

        elif menuSelection == '3':  
            os.system("clear")
            ponto1 = Ponto.Criar()
            ponto2 = Ponto.Criar()

            print(f"A distância entre os pontos é: {ponto1.Distancia(ponto2)}")
            continuar = menu.exibir_menu2()

        else:
            util.exibir_erro()
            continuar = menu.exibir_menu2()
        
    os.system("clear")
