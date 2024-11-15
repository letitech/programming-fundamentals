def es_fecha_valida(dia, mes, año):
    # Comprobar si el mes está en el rango válido
    if mes < 1 or mes > 12:
        return False
    
    # Lista de días máximos para cada mes
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Comprobar si el año es bisiesto y ajustar febrero a 29 días si lo es
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        dias_por_mes[1] = 29

    # Comprobar si el día está en el rango válido para el mes
    if dia < 1 or dia > dias_por_mes[mes - 1]:
        return False

    return True

# Solicitar al usuario que ingrese el día, mes y año
try:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))

    # Validar la fecha ingresada
    if es_fecha_valida(dia, mes, año):
        print("La fecha ingresada es válida.")
    else:
        print("La fecha ingresada no es válida.")
except ValueError:
    print("Por favor, ingrese valores numéricos válidos para el día, mes y año.")
