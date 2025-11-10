class HistorialVuelos:
    def __init__(self, vuelo_inicial):
        self.raiz = vuelo_inicial

    # Recorrido simple (similar a preorden en este contexto)
    def recorrer_historial(self):
        resultado = []
        self._recorrer_recursivo(self.raiz, resultado)
        return resultado

    def _recorrer_recursivo(self, nodo, resultado):
        if nodo:
            resultado.append(f"Vuelo {nodo.numero_vuelo} de {nodo.origen} a {nodo.destino}")
            for conexion in nodo.conexiones:
                self._recorrer_recursivo(conexion, resultado)

    # Búsqueda (DFS - Profundidad)
    def buscar_vuelo_general(self, numero_vuelo):
        return self._buscar_vuelo_recursivo_general(self.raiz, numero_vuelo)

    def _buscar_vuelo_recursivo_general(self, nodo, numero_vuelo):
        if nodo is None:
            return None
        if nodo.numero_vuelo == numero_vuelo:
            return nodo
        for conexion in nodo.conexiones:
            resultado = self._buscar_vuelo_recursivo_general(conexion, numero_vuelo)
            if resultado:
                return resultado
        return None
