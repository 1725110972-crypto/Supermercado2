# Productos del Supermercado (Aurrera)

Proyecto de estructuras de datos: una **lista ordenada (TDA)** de productos
de supermercado, consultable por el público. La idea, igual que con una
lista de alumnos ordenada por apellido paterno, es que cada producto
ocupe una **posición determinada** dentro de la lista según la regla que
se elija (categoría, precio, nombre, etc.), y no simplemente aparezca en
el orden en que se guardó en la base de datos.

## ¿Qué hace?

1. La base de datos (SQLite) ya viene precargada con ~24 productos de
   ejemplo, repartidos en categorías: Lácteos, Carnes, Hogar, Limpieza,
   Bebidas, Panadería, Frutas y Verduras, Abarrotes.
2. En la pantalla principal se elige una **regla de orden/búsqueda**:
   - Categoría (y opcionalmente una segunda regla dentro de la categoría,
     por ejemplo: primero por categoría y luego por precio)
   - Nombre del producto
   - Precio (exacto, ej. "$200", o por rango, ej. "entre $20 y $100")
   - Fecha de caducidad
   - Unidad de medida
   - Cantidad en inventario
   - Marca
   - Código de barras
3. Al generar la lista, el sistema construye el TDA `ListaOrdenada`
   (ver `tda/lista_ordenada.py`) insertando cada producto en su posición
   correcta, y muestra la tabla resultante con las 8 columnas:
   categoría, nombre, precio, fecha de caducidad, unidad de medida,
   cantidad en inventario, marca y código de barras.

## El TDA (lo importante para la materia)

`tda/lista_ordenada.py` define la clase `ListaOrdenada`, que **no** es
simplemente "usar `sorted()`". Implementa:

- `insertar(elemento)`: cada producto se coloca en la posición que le
  corresponde (inserción ordenada), en vez de agregarse al final.
- `buscar_por_valor(valor)`: búsqueda **binaria**, posible precisamente
  porque la lista ya está ordenada.
- `buscar_por_rango(minimo, maximo)`: para pedidos tipo "productos entre
  $100 y $200".
- La "clave" de orden es una función que se le pasa a la lista, así la
  misma estructura sirve para ordenar por categoría, por precio, por
  nombre, o por una combinación (categoría y luego precio).

## Estructura del proyecto

```
supermercado_aurrera/
├── app.py                  # Rutas web.py (Index y Lista)
├── tda/
│   └── lista_ordenada.py   # El TDA: lista ordenada
├── db/
│   ├── database.py         # Conexión SQLite y esquema
│   ├── seed_data.py        # Productos de ejemplo precargados
│   └── productos.db        # Se genera al correr el programa
├── templates/
│   ├── base.html
│   ├── index.html          # Pantalla de reglas
│   └── lista.html          # Tabla con la lista ordenada
├── static/
│   └── style.css
└── requirements.txt
```

## Cómo correrlo

```bash
pip install -r requirements.txt
python app.py
```

Esto crea `db/productos.db` (si no existe) con los productos de ejemplo,
y levanta el servidor en `http://localhost:8080`.

## Cómo agregar más productos

Edita la lista `PRODUCTOS_INICIALES` en `db/seed_data.py` y borra
`db/productos.db` para que se vuelva a generar con los nuevos datos, o
usa `insertar_producto(...)` de `db/database.py` desde una consola de
Python.
