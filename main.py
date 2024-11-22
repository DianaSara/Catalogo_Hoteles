import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
from clases import Hotel, Habitacion, Catalogo
import sqlite3
import re


def crear_base_datos():
    # Conectar a la base de datos (se crea si no existe)
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Crear la tabla de usuarios si no existe
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        correo TEXT NOT NULL,
                        contrasena TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

# Función para validar el formato del correo
def validar_correo(correo):
    patron = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(patron, correo) is not None

# Función para guardar los datos en la base de datos
def guardar_en_base_datos(correo, contrasena):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()
    
    # Insertar el correo y la contraseña en la base de datos
    cursor.execute('INSERT INTO usuarios (correo, contrasena) VALUES (?, ?)', (correo, contrasena))
    
    conn.commit()
    conn.close()

# Función para obtener y validar los datos
def obtener_datos():
    correo = entry_correo.get()
    contrasena = entry_contrasena.get()

    # Validación del correo
    if correo:
        if not validar_correo(correo):
            messagebox.showwarning("Correo inválido", "El correo ingresado no tiene un formato válido.")
            return
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa un correo.")
        return

    # Validación de la contraseña
    if contrasena:
        if len(contrasena) < 6:  # La contraseña debe tener al menos 6 caracteres
            messagebox.showwarning("Contraseña inválida", "La contraseña debe tener al menos 6 caracteres.")
            return
    else:
        messagebox.showwarning("Advertencia", "Por favor ingresa una contraseña.")
        return

    # Guardar los datos en la base de datos
    guardar_en_base_datos(correo, contrasena)
    
    # Mostrar mensaje de éxito y cerrar la ventana
    messagebox.showinfo("Datos guardados", "Correo y contraseña guardados exitosamente.")
    ventana.after(1000, ventana.destroy)  # Cierra la ventana después de 1 segundo

# Crear la base de datos y la tabla si no existe
crear_base_datos()

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de Correo y Contraseña")
ventana.geometry("300x250")

# Crear el campo para el correo
label_correo = tk.Label(ventana, text="Correo Electrónico:")
label_correo.pack(pady=10)

entry_correo = tk.Entry(ventana, width=30)
entry_correo.pack(pady=5)

# Crear el campo para la contraseña
label_contrasena = tk.Label(ventana, text="Contraseña:")
label_contrasena.pack(pady=10)

entry_contrasena = tk.Entry(ventana, width=30, show="*")  # Ocultar el texto de la contraseña
entry_contrasena.pack(pady=5)

# Botón para validar y guardar los datos
boton_validar = tk.Button(ventana, text="Validar y Guardar", command=obtener_datos)
boton_validar.pack(pady=20)

# Ejecutar la aplicación
ventana.mainloop()
# Crear conexión a la base de datos
def conectar_db():
    conn = sqlite3.connect('hoteles.db')
    return conn
# Crear tablas necesarias en la base de datos
def crear_tablas():
    conn = conectar_db()
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hoteles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        estrellas INTEGER,
        precio REAL,
        descripcion TEXT,
        ubicacion TEXT,
        imagen TEXT
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS habitaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_hotel INTEGER,
        nombre TEXT,
        descripcion TEXT,
        capacidad INTEGER,
        precio REAL,
        FOREIGN KEY (id_hotel) REFERENCES hoteles(id)
    )
    ''')
    
    conn.commit()
    conn.close()


# Función para insertar datos en la base de datos
def insertar_datos():
    conn = conectar_db()
    cursor = conn.cursor()
"""
    # Tropico Inn
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Tropico Inn", 3, 75, "Un hotel cómodo y céntrico con servicios básicos.", "En el corazón de la ciudad", "imagenes/Tropico.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Estándar", "Cama queen y baño privado", 2, 75)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite Familiar", "Espacio para 4 personas con sala de estar", 4, 100)
    ''', (hotel_id,))

    # Hotel Florencia
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel Florencia", 4, 95, "Hotel moderno con instalaciones de lujo.", "Cerca de las principales atracciones de la ciudad", "imagenes/Hotel_Florencia.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Doble", "Cama doble y balcón", 2, 95)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite Premium", "Vista panorámica, cama king y jacuzzi", 3, 140)
    ''', (hotel_id,))

    # Comfort Inn Real San Miguel
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Comfort Inn Real San Miguel", 4, 89, "Hotel de alta calidad con una excelente reputación.", "A pocos minutos del centro de San Miguel", "imagenes/Confort_INN_Real_San_miguel.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Deluxe", "Vista a la ciudad, cama king y escritorio", 2, 89)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite Ejecutiva", "Incluye sala de estar, mini cocina y baño de lujo", 3, 120)
    ''', (hotel_id,))

    # Bella Vista Hotel Boutique
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Bella Vista Hotel Boutique", 5, 120, "Hotel boutique con vistas espectaculares y atención personalizada.", "Ubicación tranquila en las colinas", "imagenes/Bella_Vista_Hotel.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 120)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 180)
    ''', (hotel_id,))
    
    # Hoter europa
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hoteles Europa", 5, 150, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/hoteles_europa.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 150)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 200)
    ''', (hotel_id,))
    
    # Gran Hotel San Miguel
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Gran Hotel San Miguel", 5, 200, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Gran_Hotel_San_Miguel.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 200)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 250)
    ''', (hotel_id,))
   
    # Hotel real caribe
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel Real Caribe", 5, 250, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hotel_Real_Caribe.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 250)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 300)
    ''', (hotel_id,))
    
    #hotel montaña
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel Montaña", 5, 300, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hotel_Montana.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 300)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 350)
    ''', (hotel_id,))
    #Hostal luz de luna
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hostal Luz de Luna", 5, 350, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hostal_Luz_de_Luna.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 350)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 400)
    ''', (hotel_id,))
    #hotel amanecer tropical
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel Amanecer Tropical", 5, 400, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hotel_Amanecer_Tropical.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 400)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 450)
    ''', (hotel_id,))
    
    #Hotel oasis
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel Oasis", 5, 450, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hotel_Oasis.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 450)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 500)
    ''', (hotel_id,))
    
    #Hotel Esmeralda
    
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel Esmeralda", 5, 500, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hotel_Esmeralda.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 500)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 550)
    ''', (hotel_id,))
    
    #Hotel Las palmeras
    
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel Las Palmeras", 5, 550, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hotel_Las_Palmeras.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 550)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 600)
    ''', (hotel_id,))
    
    #Hotel sol y mar
    
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel Sol y Mar", 5, 600, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hotel_Sol_y_Mar.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 600)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 650)
    ''', (hotel_id,))
    
    #hotel la cascada
    
    cursor.execute('''
    INSERT INTO hoteles (nombre, estrellas, precio, descripcion, ubicacion, imagen)
    VALUES ("Hotel La Cascada", 5, 650, "Hotel de lujo con vistas panorámicas y servicios de alta calidad.", "En el corazón de la ciudad", "imagenes/Hotel_La_Cascada.png")
    ''')
    hotel_id = cursor.lastrowid
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Habitación Panorámica", "Vista a las montañas, cama king", 2, 650)
    ''', (hotel_id,))
    cursor.execute('''
    INSERT INTO habitaciones (id_hotel, nombre, descripcion, capacidad, precio)
    VALUES (?, "Suite de Lujo", "Espaciosa con terraza privada", 3, 700)
    ''', (hotel_id,))
    
    conn.commit()
    conn.close()
"""



# Crear instancia del catálogo
catalogo_hoteles = Catalogo()


# Función para inicializar los datos
def inicializar_datos():
    # Tropico Inn
    hotel1 = Hotel(
        nombre="Tropico Inn",
        estrellas=3,
        precio=75,
        descripcion="Un hotel cómodo y céntrico con servicios básicos.",
        servicios=["WiFi gratuito", "Restaurante", "Estacionamiento"],
        ubicacion="En el corazón de la ciudad",
        imagen="imagenes/Tropico.png"
    )
    hotel1.agregar_habitacion(Habitacion("Habitación Estándar", "Cama queen y baño privado", 2, 75))
    hotel1.agregar_habitacion(Habitacion("Suite Familiar", "Espacio para 4 personas con sala de estar", 4, 100))
    catalogo_hoteles.agregar_hotel(hotel1)

    # Hotel Florencia
    hotel2 = Hotel(
        nombre="Hotel Florencia",
        estrellas=4,
        precio=95,
        descripcion="Hotel moderno con instalaciones de lujo.",
        servicios=["Piscina", "Restaurante", "Spa", "Desayuno incluido"],
        ubicacion="Cerca de las principales atracciones de la ciudad",
        imagen="imagenes/Hotel_Florencia.png"
    )
    hotel2.agregar_habitacion(Habitacion("Habitación Doble", "Cama doble y balcón", 2, 95))
    hotel2.agregar_habitacion(Habitacion("Suite Premium", "Vista panorámica, cama king y jacuzzi", 3, 140))
    catalogo_hoteles.agregar_hotel(hotel2)

    # Comfort Inn Real San Miguel
    hotel3 = Hotel(
        nombre="Comfort Inn Real San Miguel",
        estrellas=4,
        precio=89,
        descripcion="Hotel de alta calidad con una excelente reputación.",
        servicios=["Piscina", "Gimnasio", "Desayuno incluido", "Restaurante", "Bar"],
        ubicacion="A pocos minutos del centro de San Miguel",
        imagen="imagenes/Confort_INN_Real_San_miguel.png"
    )
    hotel3.agregar_habitacion(Habitacion("Habitación Deluxe", "Vista a la ciudad, cama king y escritorio", 2, 89))
    hotel3.agregar_habitacion(Habitacion("Suite Ejecutiva", "Incluye sala de estar, mini cocina y baño de lujo", 3, 120))
    catalogo_hoteles.agregar_hotel(hotel3)

    # Bella Vista Hotel Boutique
    hotel4 = Hotel(
        nombre="Bella Vista Hotel Boutique",
        estrellas=5,
        precio=120,
        descripcion="Hotel boutique con vistas espectaculares y atención personalizada.",
        servicios=["Piscina", "Gimnasio", "Restaurante gourmet", "WiFi gratuito"],
        ubicacion="Ubicación tranquila en las colinas",
        imagen="imagenes/Bella_Vista_Hotel.png"
    )
    hotel4.agregar_habitacion(Habitacion("Habitación Panorámica", "Vista a las montañas, cama king", 2, 120))
    hotel4.agregar_habitacion(Habitacion("Suite de Lujo", "Espaciosa con terraza privada", 3, 180))
    catalogo_hoteles.agregar_hotel(hotel4)

    # Hotel Europa
    hotel5 = Hotel(
        nombre="Hotel Europa",
        estrellas=3,
        precio=80,
        descripcion="Hotel acogedor con un ambiente europeo clásico.",
        servicios=["Desayuno incluido", "Bar", "WiFi gratuito"],
        ubicacion="Zona histórica de la ciudad",
        imagen="imagenes/Hote_Europa.png"
    )
    hotel5.agregar_habitacion(Habitacion("Habitación Clásica", "Cama doble y decoración vintage", 2, 80))
    hotel5.agregar_habitacion(Habitacion("Suite Superior", "Espacio amplio con sala de estar", 3, 110))
    catalogo_hoteles.agregar_hotel(hotel5)

        # Gran Hotel San Miguel
    hotel6 = Hotel(
        nombre="Gran Hotel San Miguel",
        estrellas=4,
        precio=100,
        descripcion="Hotel elegante y espacioso con todas las comodidades modernas.",
        servicios=["Piscina", "Gimnasio", "Restaurante", "Bar", "Desayuno incluido"],
        ubicacion="Zona céntrica de San Miguel",
        imagen="imagenes/Gran_Hotel_San_Miguel.png"
    )
    hotel6.agregar_habitacion(Habitacion("Habitación Ejecutiva", "Cama queen, escritorio", 2, 100))
    hotel6.agregar_habitacion(Habitacion("Suite Presidencial", "Área de lujo con vista panorámica", 3, 200))
    catalogo_hoteles.agregar_hotel(hotel6)

    # Hotel Real Caribe
    hotel7 = Hotel(
        nombre="Hotel Real Caribe",
        estrellas=3,
        precio=85,
        descripcion="Una opción económica con ambiente caribeño.",
        servicios=["Piscina", "Bar", "WiFi gratuito"],
        ubicacion="Cerca de la playa",
        imagen="imagenes/Hotel_Real_Caribe.png"
    )
    hotel7.agregar_habitacion(Habitacion("Habitación Doble", "Vista al mar, cama queen", 2, 85))
    hotel7.agregar_habitacion(Habitacion("Suite Tropical", "Terraza privada y jacuzzi", 3, 150))
    catalogo_hoteles.agregar_hotel(hotel7)

    # Hotel Montaña Verde
    hotel8 = Hotel(
        nombre="Hotel Montaña Verde",
        estrellas=4,
        precio=90,
        descripcion="Un hotel rodeado de naturaleza, ideal para escapar del bullicio de la ciudad.",
        servicios=["Senderos naturales", "Restaurante", "WiFi gratuito", "Desayuno incluido"],
        ubicacion="Ubicado en una reserva natural",
        imagen="imagenes/Hotel_Montana_Verde.png"
    )
    hotel8.agregar_habitacion(Habitacion("Habitación Ecológica", "Vista a la montaña, cama doble", 2, 90))
    hotel8.agregar_habitacion(Habitacion("Cabaña Premium", "Privada, con terraza y chimenea", 4, 150))
    catalogo_hoteles.agregar_hotel(hotel8)

    # Hostal Luz de Luna
    hotel9 = Hotel(
        nombre="Hostal Luz de Luna",
        estrellas=2,
        precio=50,
        descripcion="Hostal económico con un ambiente acogedor.",
        servicios=["WiFi gratuito", "Cocina compartida", "Recepción 24 horas"],
        ubicacion="Cerca de la terminal de autobuses",
        imagen="imagenes/Hostal_Luz_de_Luna.png"
    )
    hotel9.agregar_habitacion(Habitacion("Habitación Básica", "Cama individual y baño compartido", 1, 50))
    hotel9.agregar_habitacion(Habitacion("Habitación Familiar", "Cama doble y literas", 4, 70))
    catalogo_hoteles.agregar_hotel(hotel9)

    # Hotel Amanecer Tropical
    hotel10 = Hotel(
        nombre="Hotel Amanecer Tropical",
        estrellas=3,
        precio=85,
        descripcion="Perfecto para unas vacaciones relajantes en un entorno tropical.",
        servicios=["Piscina", "Restaurante", "Jardín tropical"],
        ubicacion="Cerca de la playa",
        imagen="imagenes/Amanecer_Tropical.png"
    )
    hotel10.agregar_habitacion(Habitacion("Habitación Estándar", "Cama queen, vista al jardín", 2, 85))
    hotel10.agregar_habitacion(Habitacion("Suite con Balcón", "Vista al mar y balcón privado", 3, 120))
    catalogo_hoteles.agregar_hotel(hotel10)

    # Hotel Oasis
    hotel11 = Hotel(
        nombre="Hotel Oasis",
        estrellas=4,
        precio=95,
        descripcion="Un lugar tranquilo para desconectar del mundo.",
        servicios=["Spa", "Piscina", "Bar", "WiFi gratuito"],
        ubicacion="A las afueras de la ciudad",
        imagen="imagenes/Hotel_Oasis.png"
    )
    hotel11.agregar_habitacion(Habitacion("Habitación Zen", "Decoración minimalista, cama king", 2, 95))
    hotel11.agregar_habitacion(Habitacion("Suite Oasis", "Vista a la piscina, jacuzzi", 3, 140))
    catalogo_hoteles.agregar_hotel(hotel11)

    # Hotel Esmeralda
    hotel12 = Hotel(
        nombre="Hotel Esmeralda",
        estrellas=3,
        precio=75,
        descripcion="Un hotel clásico con un toque moderno.",
        servicios=["Restaurante", "Bar", "WiFi gratuito"],
        ubicacion="En el casco antiguo de la ciudad",
        imagen="imagenes/Hotel_Esmeralda.png"
    )
    hotel12.agregar_habitacion(Habitacion("Habitación Clásica", "Cama doble, decoración vintage", 2, 75))
    hotel12.agregar_habitacion(Habitacion("Suite Elegante", "Espaciosa con sala de estar", 3, 110))
    catalogo_hoteles.agregar_hotel(hotel12)

    # Hotel Las Palmeras
    hotel13 = Hotel(
        nombre="Hotel Las Palmeras",
        estrellas=3,
        precio=70,
        descripcion="Confortable y accesible, rodeado de palmeras.",
        servicios=["Piscina", "Restaurante", "WiFi gratuito"],
        ubicacion="Cerca del parque central",
        imagen="imagenes/Las_Palmeras.png"
    )
    hotel13.agregar_habitacion(Habitacion("Habitación Básica", "Cama queen y baño privado", 2, 70))
    hotel13.agregar_habitacion(Habitacion("Habitación Familiar", "Camas dobles, ideal para grupos", 4, 100))
    catalogo_hoteles.agregar_hotel(hotel13)

    # Hotel Sol y Mar
    hotel14 = Hotel(
        nombre="Hotel Sol y Mar",
        estrellas=4,
        precio=110,
        descripcion="Hotel costero ideal para unas vacaciones inolvidables.",
        servicios=["Playa privada", "Restaurante", "Bar", "Deportes acuáticos"],
        ubicacion="Frente al mar",
        imagen="imagenes/Sol_y_Mar.png"
    )
    hotel14.agregar_habitacion(Habitacion("Habitación Vista al Mar", "Balcón privado, cama king", 2, 110))
    hotel14.agregar_habitacion(Habitacion("Suite Familiar", "Dos habitaciones conectadas, sala de estar", 5, 180))
    catalogo_hoteles.agregar_hotel(hotel14)

    # Hotel La Cascada
    hotel15 = Hotel(
        nombre="Hotel La Cascada",
        estrellas=4,
        precio=100,
        descripcion="Un refugio natural con una cascada en su interior.",
        servicios=["Senderos naturales", "Piscina", "Restaurante", "Spa"],
        ubicacion="En un parque natural",
        imagen="imagenes/La_Cascada.png"
    )
    hotel15.agregar_habitacion(Habitacion("Habitación Natural", "Vista a la cascada, cama doble", 2, 100))
    hotel15.agregar_habitacion(Habitacion("Suite con Terraza", "Terraza privada con vista a la cascada", 3, 150))
    catalogo_hoteles.agregar_hotel(hotel15)



# Función para redimensionar imágenes
def redimensionar_imagen(imagen_path, tamaño=(200, 150)):
    try:
        img = Image.open(imagen_path)
        img = img.resize(tamaño, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Error al redimensionar la imagen: {e}")
        return None

# Función para mostrar hoteles
def mostrar_hoteles():
    for widget in contenedor_hoteles.winfo_children():
        widget.destroy()

    for hotel in catalogo_hoteles.hoteles:
        frame_hotel = ttk.Frame(contenedor_hoteles, padding=10, style="Hotel.TFrame")
        frame_hotel.pack(fill='x', padx=5, pady=5)

        if hotel.imagen:
            img = redimensionar_imagen(hotel.imagen)
            if img:
                lbl_imagen = ttk.Label(frame_hotel, image=img, style="HotelImage.TLabel")
                lbl_imagen.image = img
                lbl_imagen.pack(side='left', padx=10, pady=5)

        info_frame = ttk.Frame(frame_hotel)
        info_frame.pack(side='left', fill='both', expand=True, padx=10)
        ttk.Label(info_frame, text=f"{hotel.nombre} ({hotel.estrellas} estrellas)", font=("Arial", 12, "bold")).pack(anchor='w')
        ttk.Label(info_frame, text=f"Desde ${hotel.precio:.2f}", font=("Arial", 10)).pack(anchor='w')
        ttk.Label(info_frame, text=f"{hotel.descripcion}", wraplength=400).pack(anchor='w', pady=5)
        ttk.Button(info_frame, text="Ver detalles", command=lambda h=hotel: mostrar_detalles_hotel(h)).pack(anchor='e', pady=5)

# Función para mostrar detalles de un hotel
def mostrar_detalles_hotel(hotel):
    detalles_ventana = tk.Toplevel()
    detalles_ventana.title(f"Detalles de {hotel.nombre}")
    detalles_ventana.configure(bg="#f0f0f0")

    frame_principal = ttk.Frame(detalles_ventana, padding=20)
    frame_principal.pack(fill='both', expand=True)

    ttk.Label(frame_principal, text=f"{hotel.nombre}", font=("Arial", 16, "bold")).pack(anchor='w', pady=10)
    if hotel.imagen:
        img = redimensionar_imagen(hotel.imagen, tamaño=(300, 200))
        if img:
            lbl_imagen = ttk.Label(frame_principal, image=img)
            lbl_imagen.image = img
            lbl_imagen.pack(pady=10)

    ttk.Label(frame_principal, text=f"Descripción: {hotel.descripcion}", wraplength=500).pack(anchor='w', pady=5)
    ttk.Label(frame_principal, text=f"Ubicación: {hotel.ubicacion}").pack(anchor='w', pady=5)
    ttk.Label(frame_principal, text=f"Servicios: {', '.join(hotel.servicios)}").pack(anchor='w', pady=10)

    ttk.Button(frame_principal, text="Cerrar", command=detalles_ventana.destroy).pack(pady=10)
    


# Configuración de la ventana principal
root = tk.Tk()
root.title("Catálogo de Hoteles")
root.configure(bg="#e8f5e9")

style = ttk.Style()
style.configure("TFrame", background="#e8f5e9")
style.configure("TLabel", background="#e8f5e9", font=("Arial", 10))
style.configure("Hotel.TFrame", background="#ffffff", relief="raised", borderwidth=2)
style.configure("HotelImage.TLabel", background="#ffffff")

ttk.Label(root, text="Hoteles de San Miguel", font=("Arial", 18, "bold"), background="#e8f5e9").pack(pady=10)

frame_scroll = ttk.Frame(root)
frame_scroll.pack(fill='both', expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_scroll, bg="#e8f5e9")
canvas.pack(side="left", fill="both", expand=True)

scrollbar = ttk.Scrollbar(frame_scroll, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

contenedor_hoteles = ttk.Frame(canvas)
canvas.create_window((0, 0), window=contenedor_hoteles, anchor="nw")

inicializar_datos()
mostrar_hoteles()  # Agrega esta línea para mostrar los hoteles en la interfaz.

#inicializar la base de datos
crear_tablas()
insertar_datos()


canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * (event.delta // 120), "units"))

root.mainloop()



