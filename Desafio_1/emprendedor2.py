import math
precio_suscripcion=int(input("Ingrese el precio de suscripción:\n"))
usuario_normal = int(input("Ingrese número de usuarios normales:\n"))
usuario_premium = int(input("Ingrese número de usuarios premiun:\n"))
gasto_total= int(input("Ingrese el gasto total:\n"))

utilidades = (precio_suscripcion * usuario_normal * usuario_premium) - gasto_total
print(f'Utilidades son:\n{utilidades}')
