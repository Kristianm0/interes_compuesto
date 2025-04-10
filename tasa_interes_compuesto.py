# @Kristianmartinezcolina  -> Programación en Python
"📌 Ejercicio de interés compuesto -> ¿Cómo calcular la tasa de una inversión?"

""" Ejemplo con Mario Bros de The Super Mario Bros. Movie 
Imagina que Mario guarda $5,000 en su cofre en el Reino Champiñón, y después de 3 años el saldo sube a $6,500. ¿Cuál es la tasa de interés anual de su inversión?
"""

"""Formula
Fórmula: i = raíz(n)(Vf / Vp) - 1
i = Tasa de interés (anual o mensual, dependiendo del periodo de tiempo) ?
Vp = Valor presente (5.000)
Vf = Valor futuro (6.500)
n = Número de periodos de tiempo (puede ser años, meses, etc.)
"""  

from decimal import Decimal
import math

def tasas_interes_compuesto():
    try: 
        valor_futuro = Decimal(input("Dame el valor futuro: "))
        valor_presente = Decimal(input("Dame el valor presente: "))
        numero_tiempo = Decimal(input("Dame el tiempo: ")) 

        tipo_tiempo = int(input("""
        Elige el tipo de tiempo: 
        1. Dias. 
        2. Meses.
        3. Años
        >         
        """))

        if tipo_tiempo == 1:
             tipo_tiempo_nombre = "Diaria"
        elif tipo_tiempo == 2: 
             tipo_tiempo_nombre = "Mensual"
        elif tipo_tiempo == 3:
             tipo_tiempo_nombre = "Anual"
        else: 
             print("No es valido")

        formula_tasa_interes = math.pow(valor_futuro / valor_presente, 1 /numero_tiempo) - 1

        formula_tasa_interes_porcentaje = formula_tasa_interes * 100

        print(f"La tasa es {formula_tasa_interes_porcentaje:.4f}% en un periodo de tiempo {tipo_tiempo_nombre}")
    
    except Exception as error: 
          print(f"⚠️ Hubo un error: {error}")


tasas_interes_compuesto()

