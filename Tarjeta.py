import pygame
from constantes import *

class Tarjeta:
    def __init__(self, nombre_imagen: str, identificador: int, nombre_imagen_escondida: str, x: int, y: int ):
        # valores iniciales que se le va a dar al atributo(por medio del constructor)
        self.superficie = pygame.transform.scale(
            pygame.image.load(nombre_imagen), (ANCHO_TARJETA, ALTO_TARJETA))
        self.superficie_escondida = pygame.transform.scale(
            pygame.image.load(nombre_imagen_escondida), (ANCHO_TARJETA, ALTO_TARJETA))
        self.identificador = identificador
        self.visible = False
        self.descubierto = False
        self.rectangulo = self.superficie.get_rect()
        self.rectangulo.x = x
        self.rectangulo.y = y

    def obtener_cantidad_tarjetas_por_estado(self, lista_tarjetas: list[dict], estado: bool) -> int:
        '''
            Obtiene la cantidad de tarjetas que esten visibles y que esten o no cubiertas
            Recibe la lista de tarjetas y un estado (True o False) si es True me devuelve las cartas descubieras sino me devuelve las cubiertas.
            Retorna dicha cantidad
        '''
        cantidad = 0
        for tarjeta in lista_tarjetas:
            if (tarjeta.descubierto == estado and tarjeta.visible):
                cantidad += 1
        return cantidad

    def descubrir_tarjetas(self, lista_tarjetas, identificador):
        '''
            Función que se encarga de cambiarme la bandera a las tarjetas a las que el usuario haya acertado en el memotest
            recibe la lista de tarjetas y el identificador a la que le va a reemplazar la bandera descubierto
            Uso una variable contador para evitar que el bucle se ejecute completo y ahorrar recursos si ya reemplazo a dos tarjetas no tiene sentido seguir iterando
        '''
        contador = 0
        for tarjeta in lista_tarjetas:
            if tarjeta.identificador == identificador and tarjeta.descubierto == False:
                tarjeta.descubierto = True
                contador += 1
            elif contador == 2:
                break
