import math
gravedad= float(input("Ingrese la constante g:\n>"))
radio=float(input("Ingrese el radio en Kilómetros:\n>"))

# radio * 1000 es para hacer la conversión de km a m
v_escape= math.sqrt(2*radio*1000*gravedad)
redondeado=round(v_escape,1)
print(f'La velocidad de escape es:\n{redondeado}[m/s]')