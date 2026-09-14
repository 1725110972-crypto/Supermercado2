# -*- coding: utf-8 -*-
import sqlite3
import os

RUTA_DB = os.path.join(os.path.dirname(__file__), "productos.db")


def obtener_conexion():
    conexion = sqlite3.connect(RUTA_DB)
    conexion.row_factory = sqlite3.Row
    return conexion


def crear_tabla():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            categoria TEXT NOT NULL,
            nombre TEXT NOT NULL,
            precio REAL NOT NULL,
            fecha_caducidad TEXT NOT NULL,
            unidad_medida TEXT NOT NULL,
            cantidad_inventario INTEGER NOT NULL,
            marca TEXT NOT NULL,
            codigo_barras TEXT NOT NULL
        )
    """)
    conexion.commit()
    conexion.close()


def obtener_productos():
    """Regresa todos los productos de la base de datos como lista de diccionarios."""
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    filas = cursor.fetchall()
    conexion.close()
    return [dict(fila) for fila in filas]


def contar_productos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) as total FROM productos")
    total = cursor.fetchone()["total"]
    conexion.close()
    return total


def insertar_producto(producto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO productos
        (categoria, nombre, precio, fecha_caducidad, unidad_medida,
         cantidad_inventario, marca, codigo_barras)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        producto["categoria"], producto["nombre"], producto["precio"],
        producto["fecha_caducidad"], producto["unidad_medida"],
        producto["cantidad_inventario"], producto["marca"], producto["codigo_barras"]
    ))
    conexion.commit()
    conexion.close()
