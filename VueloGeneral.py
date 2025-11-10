""" Arbol General para Historias de vuelo de pasajero:
Este árbol modela el historial de un pasajero, donde cada nodo es un vuelo y sus hijos son las posibles conexiones o escalas
 subsiguientes en ese viaje. No hay un límite fijo de hijos por nodo."""


class VueloGeneral:
    def __init__(self, numero_vuelo, fecha, origen, destino):
        self.numero_vuelo = numero_vuelo
        self.fecha = fecha
        self.origen = origen
        self.destino = destino
        self.conexiones = [] # Lista de nodos hijos (conexiones/escalas)

    def __str__(self):
        return f"Vuelo {self.numero_vuelo} de {self.origen} a {self.destino}"

    def agregar_conexion(self, vuelo):
        self.conexiones.append(vuelo)


