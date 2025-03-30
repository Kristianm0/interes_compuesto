# @Kristianmartinezcolina  -> Programación en Python

"""Como sacar el tiempo en interes compuesto explicado con el macho de mi villano favorito
El Macho quiere $80,000 para su suero de guacamole explosivo. Actualmente tiene $25,000 y lo invierte al 7% de interés compuesto anual.

¿Cuántos años necesita esperar para alcanzar su meta?
"""
""" Fórmula utilizada:
    n = log(vf / vp) / log(1 + i)

Donde:
    - n  -> Número de periodos de tiempo
    - vf -> Valor futuro (Monto esperado)
    - vp -> Valor presente (Monto inicial)
    - i  -> Tasa de interés (en decimal)
"""

from decimal import Decimal
from math import log

#Pasamos tiempo a una tupla con años y meses
def convertir_tiempo(tiempo_sin_formato): 
     #Extraemos los años 
     años = int(tiempo_sin_formato) 
     #Pasa la parte decimal a meses
     meses = int((tiempo_sin_formato % 1) * 12)
     return años, meses 

def tiempo_interes_compuesto():
    try: 
        valor_futuro = Decimal(input("Dame el valor futuro: "))
        valor_presente = Decimal(input("Dame el valor presente: "))
        tasa_interes = Decimal(input("Dame la tasa de interes: ")) / 100

        formula_tiempo_i_c = log(valor_futuro / valor_presente) / log(1 + tasa_interes)

        años, meses = convertir_tiempo(formula_tiempo_i_c)

        print(f"El tiempo segun los valores es de {años} años {meses} meses")

    except Exception as error: 
          print(f"⚠️ Hubo un error: {error}")

tiempo_interes_compuesto()