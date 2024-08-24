import math 

class Ponto():

   def __init__(self, x, y, cor="preto"):
      self.x = x
      self.y = y
      self.cor = cor

   @classmethod
   def Criar(cls):
      ponto = input("Digite as coordenadas do seu ponto (x,y): ")
      x, y = Ponto.coordenadas(ponto)
      ponto = cls(x, y)
      return ponto

   def Distancia(self, ponto):
      return math.sqrt((self.x - ponto.x)**2 + (self.y - ponto.y)**2)
   
   def Apresentar(self):
      print(f"Minhas coordenadas são ({self.x},{self.y})")

   def setCor(self,cor):      
      cor = input("Digite a cor da sua forma:")
      self.cor = cor

   @staticmethod
   def coordenadas(entrada):
        entrada = entrada.strip("()")
        partes = entrada.split(",")

        x = int(partes[0].strip())
        y = int(partes[1].strip())

        return x, y
   
   def Interferencia(self, ponto3):
      if self.Distancia(ponto3) == 0:
         print("Existe interferência")
      else:
         print("Não existe interferência")   

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


