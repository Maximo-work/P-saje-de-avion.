class VueloBinario:


    """Este árbol organiza los vuelos por su número de vuelo (clave). Los vuelos con números menores van a la izquierda,
   los mayores a la derecha, facilitando la búsqueda y ordenación."""

    def __init__(self, numero_vuelo, fecha, destino):
        self.numero_vuelo = numero_vuelo
        self.fecha = fecha
        self.destino = destino
        self.izquierdo = None
        self.derecho = None

class ArbolBinarioVuelos:
    def __init__(self):
        self.raiz = None

    def insertar(self, numero_vuelo, fecha, destino):
        if self.raiz is None:
            self.raiz = VueloBinario(numero_vuelo, fecha, destino)
        else:
            self._insertar_recursivo(self.raiz, numero_vuelo, fecha, destino)

    def _insertar_recursivo(self, nodo_actual, numero_vuelo, fecha, destino):
        if numero_vuelo < nodo_actual.numero_vuelo:
            if nodo_actual.izquierdo is None:
                nodo_actual.izquierdo = VueloBinario(numero_vuelo, fecha, destino)
            else:
                self._insertar_recursivo(nodo_actual.izquierdo, numero_vuelo, fecha, destino)
        elif numero_vuelo > nodo_actual.numero_vuelo:
            if nodo_actual.derecho is None:
                nodo_actual.derecho = VueloBinario(numero_vuelo, fecha, destino)
            else:
                self._insertar_recursivo(nodo_actual.derecho, numero_vuelo, fecha, destino)
        else:
            print(f"Vuelo con número {numero_vuelo} ya existe.")

    def buscar(self, numero_vuelo):
        return self._buscar_recursivo(self.raiz, numero_vuelo)

    def _buscar_recursivo(self, nodo_actual, numero_vuelo):
        if nodo_actual is None:
            return None
        if nodo_actual.numero_vuelo == numero_vuelo:
            return nodo_actual
        elif numero_vuelo < nodo_actual.numero_vuelo:
            return self._buscar_recursivo(nodo_actual.izquierdo, numero_vuelo)
        else:
            return self._buscar_recursivo(nodo_actual.derecho, numero_vuelo)

    # Recorridos
    def inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado

    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.numero_vuelo)
            self._inorden_recursivo(nodo.derecho, resultado)

    def preorden(self):
        resultado = []
        self._preorden_recursivo(self.raiz, resultado)
        return resultado

    def _preorden_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(nodo.numero_vuelo)
            self._preorden_recursivo(nodo.izquierdo, resultado)
            self._preorden_recursivo(nodo.derecho, resultado)

    def postorden(self):
        resultado = []
        self._postorden_recursivo(self.raiz, resultado)
        return resultado

    def _postorden_recursivo(self, nodo, resultado):
        if nodo:
            self._postorden_recursivo(nodo.izquierdo, resultado)
            self._postorden_recursivo(nodo.derecho, resultado)
            resultado.append(nodo.numero_vuelo)


