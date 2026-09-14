# -*- coding: utf-8 -*-
"""
Precarga la base de datos con productos de ejemplo del supermercado (Aurrera),
organizados por categoría, para que el sistema ya tenga datos con qué trabajar.
"""
try:
    from db.database import crear_tabla, contar_productos, insertar_producto
except ImportError:
    from database import crear_tabla, contar_productos, insertar_producto

PRODUCTOS_INICIALES = [
    # --- Lácteos ---
    {"categoria": "Lacteos", "nombre": "Leche entera", "precio": 26.50,
     "fecha_caducidad": "2026-09-25", "unidad_medida": "1 L",
     "cantidad_inventario": 120, "marca": "Lala", "codigo_barras": "7501020501234"},
    {"categoria": "Lacteos", "nombre": "Yogurt natural", "precio": 32.00,
     "fecha_caducidad": "2026-09-18", "unidad_medida": "1 L",
     "cantidad_inventario": 80, "marca": "Danone", "codigo_barras": "7501020501241"},
    {"categoria": "Lacteos", "nombre": "Queso panela", "precio": 65.90,
     "fecha_caducidad": "2026-09-15", "unidad_medida": "400 g",
     "cantidad_inventario": 45, "marca": "Chilchota", "codigo_barras": "7501020501258"},
    {"categoria": "Lacteos", "nombre": "Mantequilla", "precio": 48.00,
     "fecha_caducidad": "2026-11-10", "unidad_medida": "90 g",
     "cantidad_inventario": 60, "marca": "Gloria", "codigo_barras": "7501020501265"},

    # --- Carnes ---
    {"categoria": "Carnes", "nombre": "Pechuga de pollo", "precio": 89.00,
     "fecha_caducidad": "2026-09-12", "unidad_medida": "1 kg",
     "cantidad_inventario": 35, "marca": "Bachoco", "codigo_barras": "7501030601234"},
    {"categoria": "Carnes", "nombre": "Jamon de pavo", "precio": 55.50,
     "fecha_caducidad": "2026-09-20", "unidad_medida": "250 g",
     "cantidad_inventario": 70, "marca": "FUD", "codigo_barras": "7501030601241"},
    {"categoria": "Carnes", "nombre": "Carne molida de res", "precio": 130.00,
     "fecha_caducidad": "2026-09-13", "unidad_medida": "1 kg",
     "cantidad_inventario": 25, "marca": "SuKarne", "codigo_barras": "7501030601258"},
    {"categoria": "Carnes", "nombre": "Chorizo", "precio": 42.00,
     "fecha_caducidad": "2026-10-01", "unidad_medida": "250 g",
     "cantidad_inventario": 50, "marca": "San Rafael", "codigo_barras": "7501030601265"},

    # --- Hogar ---
    {"categoria": "Hogar", "nombre": "Papel higienico (4 rollos)", "precio": 58.00,
     "fecha_caducidad": "2028-01-01", "unidad_medida": "4 pza",
     "cantidad_inventario": 200, "marca": "Pétalo", "codigo_barras": "7501040701234"},
    {"categoria": "Hogar", "nombre": "Servilletas", "precio": 22.50,
     "fecha_caducidad": "2028-01-01", "unidad_medida": "1 paquete",
     "cantidad_inventario": 150, "marca": "Kleenex", "codigo_barras": "7501040701241"},
    {"categoria": "Hogar", "nombre": "Foco LED", "precio": 39.00,
     "fecha_caducidad": "2030-01-01", "unidad_medida": "1 pza",
     "cantidad_inventario": 90, "marca": "Philips", "codigo_barras": "7501040701258"},

    # --- Limpieza ---
    {"categoria": "Limpieza", "nombre": "Jabon liquido para trastes", "precio": 34.00,
     "fecha_caducidad": "2027-06-01", "unidad_medida": "750 ml",
     "cantidad_inventario": 110, "marca": "Salvo", "codigo_barras": "7501050801234"},
    {"categoria": "Limpieza", "nombre": "Cloro", "precio": 24.00,
     "fecha_caducidad": "2027-08-01", "unidad_medida": "1 L",
     "cantidad_inventario": 95, "marca": "Cloralex", "codigo_barras": "7501050801241"},
    {"categoria": "Limpieza", "nombre": "Detergente en polvo", "precio": 89.90,
     "fecha_caducidad": "2027-12-01", "unidad_medida": "1 kg",
     "cantidad_inventario": 65, "marca": "Ariel", "codigo_barras": "7501050801258"},

    # --- Bebidas ---
    {"categoria": "Bebidas", "nombre": "Agua natural", "precio": 15.00,
     "fecha_caducidad": "2027-03-01", "unidad_medida": "1.5 L",
     "cantidad_inventario": 300, "marca": "Ciel", "codigo_barras": "7501060901234"},
    {"categoria": "Bebidas", "nombre": "Refresco de cola", "precio": 20.00,
     "fecha_caducidad": "2026-12-01", "unidad_medida": "600 ml",
     "cantidad_inventario": 180, "marca": "Coca-Cola", "codigo_barras": "7501060901241"},
    {"categoria": "Bebidas", "nombre": "Jugo de naranja", "precio": 28.50,
     "fecha_caducidad": "2026-10-15", "unidad_medida": "1 L",
     "cantidad_inventario": 75, "marca": "Jumex", "codigo_barras": "7501060901258"},

    # --- Panadería ---
    {"categoria": "Panaderia", "nombre": "Pan de caja blanco", "precio": 36.00,
     "fecha_caducidad": "2026-09-16", "unidad_medida": "680 g",
     "cantidad_inventario": 55, "marca": "Bimbo", "codigo_barras": "7501071001234"},
    {"categoria": "Panaderia", "nombre": "Panque de vainilla", "precio": 29.00,
     "fecha_caducidad": "2026-09-22", "unidad_medida": "435 g",
     "cantidad_inventario": 40, "marca": "Marinela", "codigo_barras": "7501071001241"},

    # --- Frutas y Verduras ---
    {"categoria": "Frutas y Verduras", "nombre": "Manzana roja", "precio": 42.00,
     "fecha_caducidad": "2026-09-19", "unidad_medida": "1 kg",
     "cantidad_inventario": 100, "marca": "Granel", "codigo_barras": "7501081101234"},
    {"categoria": "Frutas y Verduras", "nombre": "Platano", "precio": 18.00,
     "fecha_caducidad": "2026-09-14", "unidad_medida": "1 kg",
     "cantidad_inventario": 130, "marca": "Granel", "codigo_barras": "7501081101241"},
    {"categoria": "Frutas y Verduras", "nombre": "Jitomate", "precio": 24.00,
     "fecha_caducidad": "2026-09-13", "unidad_medida": "1 kg",
     "cantidad_inventario": 90, "marca": "Granel", "codigo_barras": "7501081101258"},

    # --- Abarrotes ---
    {"categoria": "Abarrotes", "nombre": "Arroz", "precio": 32.00,
     "fecha_caducidad": "2027-05-01", "unidad_medida": "1 kg",
     "cantidad_inventario": 140, "marca": "Verde Valle", "codigo_barras": "7501091201234"},
    {"categoria": "Abarrotes", "nombre": "Frijol negro", "precio": 35.00,
     "fecha_caducidad": "2027-04-01", "unidad_medida": "1 kg",
     "cantidad_inventario": 110, "marca": "La Sierra", "codigo_barras": "7501091201241"},
    {"categoria": "Abarrotes", "nombre": "Aceite vegetal", "precio": 48.00,
     "fecha_caducidad": "2027-07-01", "unidad_medida": "1 L",
     "cantidad_inventario": 85, "marca": "1-2-3", "codigo_barras": "7501091201258"},
]


def poblar_base_de_datos():
    crear_tabla()
    if contar_productos() == 0:
        for producto in PRODUCTOS_INICIALES:
            insertar_producto(producto)
        print(f"Se insertaron {len(PRODUCTOS_INICIALES)} productos de ejemplo.")
    else:
        print("La base de datos ya tiene productos, no se vuelve a poblar.")


if __name__ == "__main__":
    poblar_base_de_datos()
