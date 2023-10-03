from abc import *

class Poligono(ABC):

    @abstractmethod
    
    def __init__ (self):
        self.lado = None

    def qtd_lados(self):
        return self.lado

class Triangulo(Poligono):
    def __init__ (self):
        self.lado = 3

class Quadrado(Poligono):
    def __init__ (self):
        self.lado = 4