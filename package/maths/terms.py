from package.maths.controllers import Util
from package.maths.ponto import Ponto
import math
import os



class Circulo(Ponto):

   def __init__(self, centro, ponto2, cor="azul"):
      super().__init__(centro.x, centro.y, cor)
      self.raio = self.Raio(ponto2)


   @classmethod
   def Criar(cls):
      centro = input("Digite as coordenadas do centro do seu círculo (x,y): ")

      xc, yc = Ponto.coordenadas(centro)

      centro = Ponto(xc, yc)

      ponto2 = input("Digite as coordenadas da extremidade do seu círculo (x,y): ")
      xp, yp = Ponto.coordenadas(ponto2)

      ponto2 = Ponto(xp, yp)

      circulo = cls(centro, ponto2)
      return circulo


   def Raio(self, ponto2):
      return self.Distancia(ponto2)

   def Perimetro(self):
      return 2 * self.raio * math.pi
      
   def Area(self):
      return math.pi * (self.raio**2)
   
     
   def Apresentar(self):
      print(f"Minhas coordenadas são ({self.x},{self.y}). Meu raio é {self.raio:.2f} e minha cor é {self.cor}")


   def Interferencia(self, ponto3):
      if self.Distancia(ponto3) <= self.raio:
         print("Existe interferência")
      else:
         print("Não existe interferência")

   def verificarInt(self):
      Util.verificar_interferencia(self)




class Retangulo(Ponto):

   def __init__(self, centro, largura, altura, cor="branco"):
      super().__init__(centro.x, centro.y, cor)
      self.largura = largura
      self.altura = altura
      self.vi = Ponto(centro.x - largura / 2, centro.y - altura / 2)
      self.vs = Ponto(centro.x + largura / 2, centro.y + altura / 2)

   @classmethod
   def Criar(cls):
      centro = input("Digite as coordenadas do centro do seu retângulo (x,y): ")

      xc, yc = Ponto.coordenadas(centro)

      centro = Ponto(xc, yc)


      largura = int(input("Digite a largura do retângulo: "))
      altura = int(input("Digite a altura do retângulo: "))


      retangulo = cls(centro, largura, altura)
      return retangulo


   def Area(self):
      return (self.largura * self.altura)
   

   def Apresentar(self):
      print(f"Minhas coordenadas são ({self.x},{self.y}). Minha largura é {self.largura}, minha altura é {self.altura} e minha cor é {self.cor}. Minha área é {self.Area()}")


   def Interferencia(self, ponto3):
      if (self.vi.x <= ponto3.x <= self.vs.x) and (self.vi.y <= ponto3.y <= self.vs.y):
         print("Existe interferência")
      else:
         print("Não existe interferência")

   def verificarInt(self):
      Util.verificar_interferencia(self)



    



class Triangulo(Ponto):
    
   def __init__(self, vertice1, base, altura, cor="branco"):
      super().__init__(vertice1.x, vertice1.y, cor)
      self.vertice1 = vertice1
      self.base = base
      self.altura = altura

        #vertices
      self.vertice2 = Ponto(self.x + base, self.y)
      self.vertice3 = Ponto(self.x, self.y + altura)


   @classmethod
   def Criar(cls):
      vertice1 = input("Digite as coordenadas do vértice do seu triângulo (x,y): ")

      xv, yv = Ponto.coordenadas(vertice1)

      vertice1 = Ponto(xv, yv)


      base = int(input("Digite a base do triângulo: "))
      altura = int(input("Digite a altura do triângulo: "))


      triangulo = cls(vertice1, base, altura)
      return triangulo



   def Area(self):
      return (self.base * self.altura) / 2


   def Interferencia(self, ponto3):
      #áreas dos sub-triângulos formados com o ponto3
      triangulo1 = Triangulo(self.vertice1, self.vertice2.Distancia(ponto3), self.vertice3.Distancia(ponto3))
      triangulo2 = Triangulo(self.vertice2, self.vertice1.Distancia(ponto3), self.vertice3.Distancia(ponto3))
      triangulo3 = Triangulo(self.vertice3, self.vertice1.Distancia(ponto3), self.vertice2.Distancia(ponto3))

      
      area_sub_triangulos = triangulo1.Area() + triangulo2.Area() + triangulo3.Area()

    
      if math.isclose(area_sub_triangulos, self.Area(), rel_tol=1e-9):
         print("Existe interferência")
      else:
         print("Não existe interferência")


   def verificarInt(self):
      Util.verificar_interferencia(self)
    



class Segmento(Ponto):

   def __init__(self, ponto1, ponto2, cor="laranja"):
      super().__init__(ponto1.x, ponto1.y, cor)
      self.ponto1 = ponto1
      self.ponto2 = ponto2


   @classmethod       
   def Criar(cls):
      ponto1 = input("Digite as coordenadas do ponto 1 do seu segmento (x,y): ")

      x1, y1 = Ponto.coordenadas(ponto1)

      ponto1 = Ponto(x1, y1)


      ponto2 = input("Digite as coordenadas do ponto 2 do seu segmento (x,y): ")

      x2, y2 = Ponto.coordenadas(ponto2)

      ponto2 = Ponto(x2, y2)


      segmento = cls(ponto1, ponto2)
      return segmento


   def Comprimento(self):
      return self.Distancia(self.ponto2) 
   

   def Interferencia(self, ponto3):
      d1 = self.Distancia(ponto3)
      d2 = self.Distancia(ponto3)
      comprimentoSeg = self.Comprimento()

      if d1 + d2 <= 1.1 * comprimentoSeg:
         print("Existe interferência")
      elif d1 + d2 <= 1.2 * comprimentoSeg: 
         print("Está nas proximidades do segmento")
      else:
         print("Não existe interferência")


   def Apresentar(self):
      self.ponto1.Apresentar()
      self.ponto2.Apresentar()

   def verificarInt(self):
      Util.verificar_interferencia(self)

class Forma:

   @staticmethod
   def criar_forma(formaSelection):
      formas = {
         '1': Circulo,
         '2': Retangulo,
         '3': Triangulo,
         '4': Segmento
      }

      if formaSelection in formas:
         os.system("clear")
         nome_objeto = formaSelection.lower() 
         forma = formas[formaSelection].Criar()
         locals()[nome_objeto] = forma
         forma.verificarInt()

      else:
         Util.exibir_erro()





