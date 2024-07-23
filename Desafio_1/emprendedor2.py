import math
precio_suscripcion=int(input("Ingrese el precio de suscripción:\n"))
usuario_normal = int(input("Ingrese número de usuarios normales:\n"))
usuario_premium = int(input("Ingrese número de usuarios premiun:\n"))
gasto_total= int(input("Ingrese el gasto total:\n"))


# Aumento en 50%
incremento = (precio_suscripcion * usuario_premium) * 1.5


utilidades = ((precio_suscripcion * usuario_normal) + incremento) - gasto_total
print(f'Las utilidades son:\n{utilidades}')
