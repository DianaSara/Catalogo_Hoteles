# clases.py

class Habitacion:
    def __init__(self, tipo, descripcion, capacidad, precio):
        self.tipo = tipo
        self.descripcion = descripcion
        self.capacidad = capacidad
        self.precio = precio


class Hotel:
    def __init__(self, nombre, estrellas, precio, descripcion, servicios, ubicacion, imagen):
        self.nombre = nombre
        self.estrellas = estrellas
        self.precio = precio
        self.descripcion = descripcion
        self.servicios = servicios
        self.ubicacion = ubicacion
        self.imagen = imagen
        self.habitaciones = []  # Lista para almacenar habitaciones

    def agregar_habitacion(self, habitacion):
        """Agrega una habitación al hotel."""
        self.habitaciones.append(habitacion)



class Catalogo:
    def __init__(self):
        self.hoteles = []  # Lista para almacenar hoteles

    def agregar_hotel(self, hotel):
        """Agrega un hotel al catálogo."""
        self.hoteles.append(hotel)


    def mostrar_catalogo(self):
        for hotel in self.hoteles:
            print(f"Hotel: {hotel.nombre}, Estrellas: {hotel.estrellas}, Precio desde: {hotel.precio}")
            print(f"Descripción: {hotel.descripcion}")
            print(f"Servicios: {', '.join(hotel.servicios)}")
            print(f"Ubicación: {hotel.ubicacion}")
            print("Habitaciones:")
            for habitacion in hotel.habitaciones:
                print(f"  - {habitacion.tipo}: {habitacion.descripcion}, Capacidad: {habitacion.capacidad}, Precio: ${habitacion.precio}")
            print("\n")
