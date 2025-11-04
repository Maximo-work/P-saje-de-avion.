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