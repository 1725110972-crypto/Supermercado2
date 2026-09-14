# -*- coding: utf-8 -*-
"""
TDA: Lista Ordenada
--------------------
Este módulo implementa el Tipo de Dato Abstracto "Lista Ordenada".

La idea central (como la lista de alumnos ordenada por apellido paterno
que puso de ejemplo el profesor) es que cada elemento que se inserta
NO se agrega al final, sino que se busca su posición correcta según
un criterio de orden, y ahí se coloca. Así, en todo momento, la lista
completa está ordenada y cada producto "ocupa una posición determinada".

Operaciones que ofrece el TDA:
    - insertar(elemento):        inserta manteniendo el orden
    - obtener_todos():           regresa la lista completa, ya ordenada
    - buscar_por_valor(valor):   búsqueda binaria (la lista ya está ordenada)
    - buscar_por_rango(a, b):    todos los elementos cuyo valor de clave
                                  está entre a y b (ej. precios entre 100 y 200)
    - en_posicion(i):            regresa el elemento que está en la posición i

La "clave" es una función que recibe un producto (diccionario) y regresa
el valor por el cual se debe ordenar. Esto permite reutilizar la misma
lista ordenada para ordenar por categoría, por precio, por nombre, etc.,
sin tener que escribir una clase distinta para cada criterio.
"""


class ListaOrdenada:
    def __init__(self, clave):
        """
        clave: función que recibe un producto (dict) y regresa el valor
               usado para decidir su posición dentro de la lista.
               Ejemplos:
                 clave = lambda p: p["precio"]
                 clave = lambda p: p["categoria"]
                 clave = lambda p: (p["categoria"], p["precio"])  # orden compuesto
        """
        self._datos = []
        self._clave = clave

    def __len__(self):
        return len(self._datos)

    def insertar(self, elemento):
        """
        Inserta 'elemento' en la posición que le corresponde para que
        la lista se mantenga ordenada (inserción ordenada, no al final).
        """
        valor = self._clave(elemento)
        posicion = 0
        while posicion < len(self._datos) and self._clave(self._datos[posicion]) <= valor:
            posicion += 1
        self._datos.insert(posicion, elemento)
        return posicion

    def obtener_todos(self):
        """Regresa la lista completa, ya ordenada según la clave."""
        return list(self._datos)

    def en_posicion(self, i):
        """Regresa el elemento que ocupa la posición i de la lista."""
        return self._datos[i]

    def buscar_por_valor(self, valor):
        """
        Búsqueda binaria: como la lista ya está ordenada por 'clave',
        no es necesario recorrerla elemento por elemento.
        Regresa todos los elementos cuya clave sea igual a 'valor'
        (puede haber varios productos con el mismo precio, por ejemplo).
        """
        izquierda, derecha = 0, len(self._datos) - 1
        encontrado = -1

        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            valor_medio = self._clave(self._datos[medio])
            if valor_medio == valor:
                encontrado = medio
                break
            elif valor_medio < valor:
                izquierda = medio + 1
            else:
                derecha = medio - 1

        if encontrado == -1:
            return []

        # Puede haber varios elementos con la misma clave (duplicados),
        # así que se expande hacia ambos lados desde el punto encontrado.
        resultados = [self._datos[encontrado]]
        izq = encontrado - 1
        while izq >= 0 and self._clave(self._datos[izq]) == valor:
            resultados.insert(0, self._datos[izq])
            izq -= 1
        der = encontrado + 1
        while der < len(self._datos) and self._clave(self._datos[der]) == valor:
            resultados.append(self._datos[der])
            der += 1

        return resultados

    def buscar_por_rango(self, minimo, maximo):
        """
        Regresa todos los elementos cuya clave está entre 'minimo' y 'maximo'
        (inclusive). Útil para "productos entre $100 y $200", por ejemplo.
        """
        return [e for e in self._datos if minimo <= self._clave(e) <= maximo]
