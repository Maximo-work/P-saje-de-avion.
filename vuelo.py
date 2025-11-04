class Vuelo:
  def __init__(self, codigo, origen, destino):
    self.codigo = codigo
    self.origen = origen
    self.destino = destino
    self.lista_de_pasajeros = []

    def agregar_pasajero(self, pasajero,reserva):
     if pasajero in self.lista_de_pasajeros:
        return f"el pasajero ya se encuetra"
     elif self.codigo != reserva.vuelo_asociado:
       return f"el vuelo no coincide"
     else:
        self.lista_de_pasajeros.append(pasajero)
        return self.lista_de_pasajeros

    def quitar_pasajero(self):
     if self.pasajero in self.lista_de_pasajeros:
      self.lista_de_pasajeros.pop()
      return self.lista_de_pasajeros

    def mostrar_vuelo(self):
      return f"Codigo: {self.codigo}, Origen: {self.origen}, Destino: {self.destino}"
