import math
precio_suscripcion=int(input("Ingrese el precio de suscripción:\n"))
usuarios = int(input("Ingrese número de usuarios:\n"))
gasto_total= int(input("Ingrese el gasto total:\n"))
utilidades_año_anterior=int(input("Ingrese utilidades del año anterior:\n"))

utilidades = (precio_suscripcion * usuarios) - gasto_total
# Crecimiento entre año pasado y año actual
razon = utilidades / utilidades_año_anterior 
razon_redondeada = round(razon,2)
print(f'Utilidades son:\n{utilidades}')
print(f'Razón utlidades año actual, año anterior:\n{razon_redondeada}')

