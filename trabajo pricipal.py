class Equipaje:
  def __init__(self, peso, descripcion):
    self.peso = peso
    self.descripcion = descripcion

class Pasajero:
  def __init__(self, nombre, documento, nacionalidad):
    self.nombre = nombre
    self.documento = documento
    self.nacionalidad = nacionalidad
    self.historial_de_vuelo = [historial_de_vuelo]
    self.equipaje = []

  def actualizar_informacion(self, nuevo_nombre, nuevo_documento, nueva_nacionalidad, nueva_edad, nuevo_telefono, nuevo_email):
    self.nombre = nuevo_nombre
    self.documento = nuevo_documento
    self.nacionalidad = nueva_nacionalidad
    self.edad = nueva_edad
    self.telefono = nuevo_telefono
    self.email = nuevo_email

  def agregar_vuelo(self, vuelo):
   if vuelo not in self.historial_de_vuelo:
    self.historial_de_vuelo.append(vuelo)
    return self.historial_de_vuelo

  def agregar_equipaje(self, equipaje):
   if equipaje not in self.equipaje:
    self.equipaje.append(equipaje)
    return self.equipaje

  def quitar_equipaje(self, equipaje):
   if self.equipaje:
    return self.equipaje.pop()
    return self.equipaje

  def actualizar_equipaje(self, equipaje, nuevo_peso, nueva_descripcion):
    equipaje.peso = nuevo_peso
    equipaje.descripcion = nueva_descripcion

class Vuelo:
  def __init__(self, codigo, origen, destino, fecha_de_salida, hora_de_salida, lista_de_pasajeros=None):
    self.codigo = codigo
    self.origen = origen
    self.destino = destino
    self.fecha_de_salida = fecha_de_salida
    self.hora_de_salida = hora_de_salida
    self.lista_de_pasajeros = []

    def agregar_pasajero(self, pasajero):
     if pasajero not in self.lista_de_pasajeros:
       self.lista_de_pasajeros.append(pasajero)
    return self.lista_de_pasajeros

    def quitar_pasajero(self, pasajero):
     if pasajero in self.lista_de_pasajeros:
      self.lista_de_pasajeros.remove(pasajero)
    return self.lista_de_pasajeros


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







