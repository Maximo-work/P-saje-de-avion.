from equipaje import Equipaje
from pasajero import Pasajero
from vuelo import Vuelo
from reserva_pasajes import Reserva_Pasajes


#implementación:
pasajero1 = Pasajero("Juan", "123456789", "Argentina")
pasajero2 = Pasajero("Maria", "987654321", "Brasil")
pasajero3 = Pasajero("Pedro", "456789123", "Chile")

equipaje1 = Equipaje(10, "Bolso chico")
equipaje2 = Equipaje(30, "mochila")
equipaje3 = Equipaje(50, "Bolso")
equipaje4 = Equipaje(20, "Bolso grande")

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