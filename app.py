# -*- coding: utf-8 -*-
"""
Sistema de Productos del Supermercado (Aurrera) - version simple
------------------------------------------------------------------
Una sola pantalla: eliges la regla de orden/busqueda y ves la lista.
"""
from flask import Flask, render_template, request

from db.database import crear_tabla, obtener_productos, buscar_productos
from db.seed_data import poblar_base_de_datos
from tda.lista_ordenada import ListaOrdenada

app = Flask(__name__)

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


def construir_clave(criterio):
    if criterio in REGLAS:
        return lambda p: p[criterio]
    return lambda p: p["categoria"]


@app.route("/")
def index():
    crear_tabla()
    poblar_base_de_datos()

    criterio = request.args.get("criterio", "categoria")
    busqueda = request.args.get("q", "").strip()

    productos = buscar_productos(busqueda) if busqueda else obtener_productos()

    lista_ordenada = ListaOrdenada(construir_clave(criterio))
    for producto in productos:
        lista_ordenada.insertar(producto)

    return render_template(
        "index.html",
        reglas=REGLAS,
        criterio=criterio,
        busqueda=busqueda,
        productos=lista_ordenada.obtener_todos(),
    )


if __name__ == "__main__":
    crear_tabla()
    poblar_base_de_datos()
    app.run(host="0.0.0.0", port=8080, debug=True)
