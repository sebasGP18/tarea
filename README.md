class Persona:
    def __init__(self, id_persona, nombre, email):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email
    
    def login(self):
        print(self.nombre + " inició sesión")
    
    def actualizar_perfil(self):
        print("Perfil de " + self.nombre + " actualizado")


class Cliente(Persona):
    def __init__(self, id_persona, nombre, email):
        super().__init__(id_persona, nombre, email)
        self.puntos = 0
        self.pedidos = []
    
    def hacer_pedido(self, productos):
        num = len(self.pedidos) + 1
        p = Pedido(num, productos, self)
        self.pedidos.append(p)
        return p
    
    def ver_historial(self):
        print("\n--- Historial de " + self.nombre + " ---")
        for p in self.pedidos:
            print("  Pedido #" + str(p.id) + " - $" + str(p.total) + " - " + p.estado)
    
    def usar_puntos(self, pts):
        if self.puntos >= pts:
            self.puntos = self.puntos - pts
            print("Puntos usados. Te quedan: " + str(self.puntos))
            return True
        else:
            print("No tienes suficientes puntos. Tienes: " + str(self.puntos))
            return False


class Empleado(Persona):
    def __init__(self, id_persona, nombre, email, id_emp, rol):
        super().__init__(id_persona, nombre, email)
        self.id_empleado = id_emp
        self.rol = rol
    
    def agregar_ingrediente(self, inv, ing, cant):
        if ing in inv.ingredientes:
            inv.ingredientes[ing] = inv.ingredientes[ing] + cant
        else:
            inv.ingredientes[ing] = cant
        print(self.nombre + " agregó " + str(cant) + " de " + ing)
    
    def cambiar_estado(self, pedido, estado):
        pedido.estado = estado
        print("Pedido #" + str(pedido.id) + " ahora: " + estado)


class Producto:
    def __init__(self, id_prod, nombre, precio):
        self.id = id_prod
        self.nombre = nombre
        self.precio = precio


class Bebida(Producto):
    def __init__(self, id_prod, nombre, precio, tamaño, temp):
        super().__init__(id_prod, nombre, precio)
        self.tamaño = tamaño
        self.temperatura = temp
        self.extras = []
    
    def agregar_extra(self, extra):
        self.extras.append(extra)
        print("  Extra agregado: " + extra)
    
    def precio_final(self):
        total = self.precio
        if self.tamaño == "mediano":
            total = total + 10
        elif self.tamaño == "grande":
            total = total + 20
        total = total + (len(self.extras) * 5)
        return total


class Postre(Producto):
    def __init__(self, id_prod, nombre, precio, vegano, gluten):
        super().__init__(id_prod, nombre, precio)
        self.vegano = vegano
        self.sin_gluten = gluten


class Pedido:
    def __init__(self, id_pedido, productos, cliente):
        self.id = id_pedido
        self.productos = productos
        self.cliente = cliente
        self.estado = "PENDIENTE"
        total = 0
        for p in productos:
            if isinstance(p, Bebida):
                total = total + p.precio_final()
            else:
                total = total + p.precio
        self.total = total


class Inventario:
    def __init__(self):
        self.ingredientes = {}
    
    def quitar(self, ing, cant):
        if ing in self.ingredientes:
            if self.ingredientes[ing] >= cant:
                self.ingredientes[ing] = self.ingredientes[ing] - cant
                print("Se quitaron " + str(cant) + " de " + ing + " (quedan " + str(self.ingredientes[ing]) + ")")
                if self.ingredientes[ing] < 5:
                    print("  ⚠️ ALERTA: Stock bajo de " + ing)
                return True
            else:
                print("No hay suficiente " + ing + ". Disponible: " + str(self.ingredientes[ing]))
                return False
        else:
            print(ing + " no existe")
            return False
    
    def mostrar(self):
        print("\n--- INVENTARIO ---")
        for i in self.ingredientes:
            print("  " + i + ": " + str(self.ingredientes[i]))
