class Equipaje:
  def __init__(self, peso, descripcion):
    self.peso = peso
    self.descripcion = descripcion
  def __str__(self):
    return self.descripcion + " " + str(self.peso) + "kg"



class Pasajero:
  def __init__(self, nombre, documento, nacionalidad ):
    self.nombre = nombre
    self.documento = documento
    self.nacionalidad = nacionalidad
    self.historial_de_vuelo = []
    self.equipajes = []
    self.equipajes_peso=0

  def mostrar_pasajero(self):
    print(f"Nombre: {self.nombre}")
    print(f"Documento: {self.documento}")
    print(f"Nacionalidad: {self.nacionalidad}")
    print("Equipajes: Peso Total:", self.equipajes_peso, "Kg")
    for e in self.equipajes:
      print(e)

  def agregar_vuelo(self, vuelo):
    self.historial_de_vuelo.append(vuelo)
    return self.historial_de_vuelo

  def agregar_equipaje(self, equipaje):
      self.equipajes.append(equipaje)
      self.equipajes_peso += equipaje.peso
      return self.equipajes

  def quitar_equipaje(self, equipaje):
     self.equipajes.remove(equipaje)
     self.equipajes_peso -= equipaje.peso
     return self.equipajes

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


class Reserva_Pasajes:
    def __init__(self, numero_reserva, pasajero_asociado, asiento_asignado, vuelo_asociado, precio_pasaje):
      self.numero_reserva = numero_reserva
      self.pasajero_asociado = pasajero_asociado
      self.asiento_asignado = asiento_asignado
      self.vuelo_asociado = vuelo_asociado
      self.precio_pasaje = precio_pasaje

    def cancelar_reserva(self):
        if self.numero_reserva is not self.numero_reserva:
          return "El numero de reserva no coincide"
        else:
          self.numero_reserva.remove(self.numero_reserva)
          return self.numero_reserva


    def actualizar_precio_pasaje(self, nuevo_precio):
        if self.precio_pasaje < 0:
          return "El precio del pasaje no puede ser negativo"
        else:
          self.precio_pasaje = nuevo_precio
          return nuevo_precio

#implementación:
pasajero1=Pasajero("Juan", "123456789", "Argentina")
pasajero2=Pasajero("Maria", "987654321", "Brasil")
pasajero3=Pasajero("Pedro", "456789123", "Chile")

equipaje1=Equipaje(10, "Bolso chico")
equipaje2=Equipaje(30, "mochila")
equipaje3=Equipaje(50, "Bolso")
equipaje4=Equipaje(20, "Bolso grande")
pasajero1.agregar_equipaje(equipaje1)
pasajero1.agregar_equipaje(equipaje2)
pasajero2.agregar_equipaje(equipaje3)
pasajero3.agregar_equipaje(equipaje4)
#pasajero1.quitar_equipaje(equipaje2)


pasajero1.mostrar_pasajero()
print()
pasajero2.mostrar_pasajero()
print()
pasajero3.mostrar_pasajero()







