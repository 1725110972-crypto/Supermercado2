# -*- coding: utf-8 -*-
"""
Sistema de Productos del Supermercado (Aurrera)
------------------------------------------------
Proyecto de estructuras de datos (TDA): muestra cómo una lista ordenada
acomoda los productos según una regla elegida por el usuario (por
categoría, por precio, por nombre, etc.), de forma que cada producto
queda en una posición determinada dentro de la lista.

Framework: web.py
Base de datos: SQLite3
"""
import web

from db.database import crear_tabla, obtener_productos
from db.seed_data import poblar_base_de_datos
from tda.lista_ordenada import ListaOrdenada

urls = (
    "/", "Index",
    "/lista", "Lista",
)

render = web.template.render("templates/", base="base")

# Reglas de orden disponibles: clave interna -> (etiqueta visible, función de clave)
REGLAS = {
    "categoria": "Categoria",
    "nombre": "Nombre del producto",
    "precio": "Precio",
    "fecha_caducidad": "Fecha de caducidad",
    "unidad_medida": "Unidad de medida",
    "cantidad_inventario": "Cantidad en inventario",
    "marca": "Marca",
    "codigo_barras": "Codigo de barras",
}


def construir_clave(criterio, subcriterio):
    """
    Regresa la función de clave que usará el TDA ListaOrdenada para
    decidir la posición de cada producto.

    Si se eligió 'categoria' y además una regla secundaria (subcriterio),
    se ordena primero por categoría y, dentro de cada categoría, por el
    subcriterio (por ejemplo: categoria y luego precio).
    """
    if criterio == "categoria" and subcriterio in REGLAS:
        return lambda p: (p["categoria"], p[subcriterio])
    if criterio in REGLAS:
        return lambda p: p[criterio]
    return lambda p: p["categoria"]


class Index:
    def GET(self):
        crear_tabla()
        poblar_base_de_datos()
        return render.index(REGLAS)


class Lista:
    def GET(self):
        crear_tabla()
        entrada = web.input(
            criterio="categoria",
            subcriterio="",
            precio_min="",
            precio_max="",
            precio_exacto="",
        )

        productos = obtener_productos()
        clave = construir_clave(entrada.criterio, entrada.subcriterio)

        lista = ListaOrdenada(clave)
        for producto in productos:
            lista.insertar(producto)

        resultado = lista.obtener_todos()

        # Si se pidió un precio exacto, se usa la búsqueda binaria del TDA
        if entrada.criterio == "precio" and entrada.precio_exacto:
            resultado = lista.buscar_por_valor(float(entrada.precio_exacto))

        # Si se pidió un rango de precios, se usa la búsqueda por rango del TDA
        elif entrada.criterio == "precio" and entrada.precio_min and entrada.precio_max:
            resultado = lista.buscar_por_rango(
                float(entrada.precio_min), float(entrada.precio_max)
            )

        return render.lista(resultado, entrada.criterio, REGLAS)


if __name__ == "__main__":
    crear_tabla()
    poblar_base_de_datos()
    app = web.application(urls, globals())
    app.run()
