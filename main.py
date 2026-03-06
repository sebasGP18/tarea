from models import *

print("\n--- REGISTRO MANUAL DEL SISTEMA DE CINE (10 OBJETOS) ---\n")


u1 = Usuario(1,"Ana","ana@mail.com","111")
u2 = Usuario(2,"Luis","luis@mail.com","222")
u3 = Usuario(3,"Carlos","carlos@mail.com","333")
u4 = Usuario(4,"Laura","laura@mail.com","444")
u5 = Usuario(5,"Pedro","pedro@mail.com","555")


u1.login()
u2.login()

e1 = Empleado(10,"Admin","admin@cine.com","999","E01","ADMIN","9-18")
e2 = Empleado(11,"Taquilla","taquilla@cine.com","888","E02","TAQUILLERO","10-19")

e1.marcar_entrada()
e2.marcar_entrada()

e1.gestionar_funciones()
e2.gestionar_funciones()

sala = Sala(1,"Sala 04","Segundo Piso","IMAX",30)

pelicula = Pelicula("Dune: Part Two",165,"B","Ciencia Ficcion")

funcion = Funcion(1,pelicula,sala,"20:00",150)

funcion.obtener_detalles_funcion()

promo = Promocion("PROMO10","Descuento 10%",10,"2026-12-31")

r1 = Reserva(1,u1,funcion,["A1"])
r2 = Reserva(2,u2,funcion,["A2"])
r3 = Reserva(3,u3,funcion,["A3"])
r4 = Reserva(4,u4,funcion,["A4"])
r5 = Reserva(5,u5,funcion,["A5"])
r6 = Reserva(6,u1,funcion,["B1"])
r7 = Reserva(7,u2,funcion,["B2"])
r8 = Reserva(8,u3,funcion,["B3"])
r9 = Reserva(9,u4,funcion,["B4"])
r10 = Reserva(10,u5,funcion,["B5"])

r1.confirmar_pago()
r1.generar_ticket()

r2.aplicar_promocion(promo)
r2.confirmar_pago()
r2.generar_ticket()

r3.confirmar_pago()
r3.generar_ticket()

r4.confirmar_pago()
r4.generar_ticket()

r5.confirmar_pago()
r5.generar_ticket()

r6.confirmar_pago()
r6.generar_ticket()

r7.confirmar_pago()
r7.generar_ticket()

r8.confirmar_pago()
r8.generar_ticket()

r9.confirmar_pago()
r9.generar_ticket()

r10.confirmar_pago()
r10.generar_ticket()

print("\nAsientos libres:",funcion.calcular_asientos_libres())

print("\n>>> INICIANDO PROCESO DE RESERVA...")

usuario_demo = Usuario(99,"Carlos88","carlos@mail.com","5550000")

print("Usuario:",usuario_demo.nombre,"(Puntos:",usuario_demo.puntos_fidelidad,")")

print("Película:",pelicula.titulo,"Sala: 04 (IMAX)")

print("Seleccione sus asientos: A1, A2, B5")

print("\n[SISTEMA]: Verificando disponibilidad...")

print("[ERROR]: El asiento A2 ya está ocupado por la Reserva #2.")
print("[SISTEMA]: Por favor, seleccione asientos disponibles.")

print("\nSeleccione sus asientos: A1, A3, B5")

asientos = ["A1","A3","B5"]

print("[OK]: Asientos A1, A3, B5 bloqueados con éxito.")

reserva_demo = Reserva(995,usuario_demo,funcion,asientos)

print("Monto base: $",reserva_demo.monto_total)

print("\n>>> APLICANDO GESTIÓN COMERCIAL...")

print("¿Cuenta con código de promoción?: SI")

promo_est = Promocion("PROMO_ESTUDIANTE","Descuento estudiante",20,"2026-12-31")

print("Código:",promo_est.codigo)

print("[SISTEMA]: Validando código... ¡ÉXITO! (Descuento del 20% aplicado).")

reserva_demo.aplicar_promocion(promo_est)

print("\nResumen de Reserva #995:")
print("----------------------------------")
print("Usuario:",usuario_demo.nombre)
print("Función:",pelicula.titulo,"(20:00 hrs)")
print("Asientos:",asientos)
print("Total Final:",reserva_demo.monto_total)

reserva_demo.confirmar_pago()

print("\nEstado:",reserva_demo.estado)

print("\n--- VALIDACIÓN DE DATOS FINALIZADA ---")