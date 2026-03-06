# persona.py
class Persona:
    def __init__(self, id_persona, nombre, email, telefono):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def login(self):
        print(f"{self.nombre} ha iniciado sesión.")

    def logout(self):
        print(f"{self.nombre} ha cerrado sesión.")

    def actualizar_datos(self, nombre=None, email=None, telefono=None):
        if nombre:
            self.nombre = nombre
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono 
class Usuario(Persona):
    def __init__(self, id_persona, nombre, email, telefono):
        super().__init__(id_persona, nombre, email, telefono)
        self.puntos_fidelidad = 0
        self.historial_reservas = []

    def crear_reserva(self, reserva):
        self.historial_reservas.append(reserva)
        print(f"Reserva creada para {self.nombre}.")

    def consultar_promociones(self):
        print(f"{self.nombre} consulta promociones disponibles.")

    def cancelar_reserva(self, reserva_id):
        self.historial_reservas = [r for r in self.historial_reservas if r.id_reserva != reserva_id]
        print(f"Reserva {reserva_id} cancelada.")
    
class Empleado(Persona):
    def __init__(self, id_persona, nombre, email, telefono, id_empleado, rol, horario):
        super().__init__(id_persona, nombre, email, telefono)
        self.id_empleado = id_empleado
        self.rol = rol  # string simple: "TAQUILLERO", "ADMIN", "LIMPIEZA"
        self.horario = horario

    def marcar_entrada(self):
        print(f"Empleado {self.nombre} ha marcado entrada.")

    def gestionar_funciones(self):
        if self.rol == "ADMIN":
            print(f"{self.nombre} puede gestionar funciones.")
        else:
            print(f"{self.nombre} no tiene permisos para gestionar funciones.")

class Espacio:
    def __init__(self, id_espacio, nombre, ubicacion):
        self.id_espacio = id_espacio
        self.nombre = nombre
        self.ubicacion = ubicacion

    def verificar_disponibilidad(self):
        print(f"Verificando disponibilidad del espacio {self.nombre}.")

    def limpiar_espacio(self):
        print(f"Espacio {self.nombre} limpiado.")

class Sala(Espacio):
    def __init__(self, id_espacio, nombre, ubicacion, tipo, capacidad_total, es_vip=False):
        super().__init__(id_espacio, nombre, ubicacion)
        self.tipo = tipo  # "2D", "3D", "IMAX"
        self.capacidad_total = capacidad_total
        self.asientos_ocupados = []  # lista de strings como "A1", "A2"
        self.es_vip = es_vip

    def ajustar_aforo(self, nuevo_aforo):
        self.capacidad_total = nuevo_aforo
        print(f"Aforo ajustado a {nuevo_aforo} asientos.")

    def obtener_tipo_sala(self):
        return self.tipo
   
class ZonaComida(Espacio):
    def __init__(self, id_espacio, nombre, ubicacion):
        super().__init__(id_espacio, nombre, ubicacion)
        self.lista_productos = []  # lista de nombres de productos
        self.stock_actual = {}  # {"Palomitas": 20, "Refresco": 15}

    def vender_producto(self, producto, cantidad):
        if self.stock_actual.get(producto, 0) >= cantidad:
            self.stock_actual[producto] -= cantidad
            print(f"Se vendieron {cantidad} de {producto}.")
        else:
            print(f"No hay suficiente stock de {producto}.")

    def actualizar_inventario(self, producto, cantidad):
        self.stock_actual[producto] = cantidad
        print(f"Inventario actualizado: {producto} = {cantidad}")
      
class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo = titulo
        self.duracion = duracion  # en minutos
        self.clasificacion = clasificacion
        self.genero = genero

    def obtener_sinopsis(self):
        print(f"Película: {self.titulo}, Género: {self.genero}, Clasificación: {self.clasificacion}")

    def es_apta_para_todo_publico(self):
        return self.clasificacion == "A"

class Funcion:
    def __init__(self, id_funcion, pelicula, sala, horario, precio_base):
        self.id_funcion = id_funcion
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario  # string simple "18:30"
        self.precio_base = precio_base
        self.asientos_reservados = []

    def calcular_asientos_libres(self):
        return self.sala.capacidad_total - len(self.asientos_reservados)

    def obtener_detalles_funcion(self):
        print(f"Funcion de {self.pelicula.titulo} en sala {self.sala.nombre} a las {self.horario}")

class Promocion:
    def __init__(self, codigo, descripcion, porcentaje_descuento, fecha_expiracion):
        self.codigo = codigo
        self.descripcion = descripcion
        self.porcentaje_descuento = porcentaje_descuento
        self.fecha_expiracion = fecha_expiracion  # string "2026-12-31"

    def es_valida(self, usuario):
        return True  # siempre válida en nuestro ejemplo simple

    def aplicar_descuento(self, monto):
        return monto * (1 - self.porcentaje_descuento / 100)

class Reserva:
    def __init__(self, id_reserva, usuario, funcion, asientos):
        self.id_reserva = id_reserva
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos  # lista de strings ["A1","A2"]
        self.monto_total = len(asientos) * funcion.precio_base
        self.estado = "PENDIENTE"

    def confirmar_pago(self):
        self.estado = "PAGADA"
        print(f"Reserva {self.id_reserva} pagada.")

    def generar_ticket(self):
        print(f"Ticket Reserva {self.id_reserva}: Película {self.funcion.pelicula.titulo}, Asientos: {self.asientos}")

    def aplicar_promocion(self, promo):
        if promo.es_valida(self.usuario):
            self.monto_total = promo.aplicar_descuento(self.monto_total)
            print(f"Promoción {promo.codigo} aplicada. Total: {self.monto_total}")