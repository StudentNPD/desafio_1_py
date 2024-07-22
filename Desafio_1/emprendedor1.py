import math
precio_suscripcion=int(input("Ingrese el precio de suscripción:\n"))
usuarios = int(input("Ingrese número de usuarios:\n"))
gasto_total= int(input("Ingrese el gasto total:\n"))

utilidades = (precio_suscripcion * usuarios) - gasto_total
print(f'Las utilidades son:\n{utilidades}')

