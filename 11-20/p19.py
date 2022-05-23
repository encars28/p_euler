# PROBLEM 19

# el 1 de enero de 1901 era martes

ano = 1900
dia_semana = 1
count = 0
mes31 = [1, 3, 5, 7, 8, 10, 12]
mes30 = [4, 6, 9, 11]


def bisiesto(a):
    if a % 4 == 0:
        if a % 100 == 0:
            if a % 400 == 0: return True

    return False


while ano <= 2000:
    mes = 1 # reiniciar contador
    while mes <= 12:
        dias_mes = 1 # reiniciar contador
        # determinar los dias que tiene el mes y si el ano es bisiesto
        if mes in mes31: dias = 31
        elif mes in mes30: dias = 30
        elif mes == 2:
            if bisiesto(mes): dias = 29
            else: dias = 28

        while dias_mes <= dias:
            # las siguientes comprobaciones sirven para evitar un bucle infinito en el caso de que
            # el dia de la semana se quiedase en 8 (es decir, que el 1 del siguiente mes cayera en 1)
            # o que se reinicie el contador cada vez que se cambia de mes, lo que provocaria que todos los dia 1
            # fueran lunes y haria imposible el ejercicio
            if dias_mes != 1 or dia_semana > 7: 
                dia_semana = 1 # reiniciar contador dentro del mes
            while dia_semana <= 7:
                # la siguiente comprobacion evita que que se sigan contando dias
                # de la semana una vez que hemos superado el numero de dias del mes, es decir, 
                # una vez que hemos pasado de mes y obliga a salirnos del bucle para poder actualizar esto
                if dias_mes <= dias:
                    dia_semana += 1
                    dias_mes += 1
                else:
                    # en 1901 el 1 es martes, asi q empezamos en 1900 donde el 1 es lunes
                    if dia_semana == 7 and ano != 1900: 
                        count += 1
                        print("yess")
                    break

        mes += 1 

    ano += 1

print(count)
    

    