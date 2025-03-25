# @Kristianmartinezcolina  -> Programación en Python
"📌 Ejercicio de interés compuesto -> ¿Cómo calcular el valor futuro de una inversión?"

"""¿Que es el interes compuesto?
El interés compuesto es cuando los intereses que ganas se suman a tu dinero inicial y luego generan más intereses. 

Por ejemplo para los Minions, el interés compuesto es como empezar con una pequeña pila de monedas. Con el tiempo, cada moneda extra que ganan ayuda a generar aún más monedas, haciendo que su tesoro crezca más rápido.
"""

""" Ejercicio con Kevin de los Minions 
Kevin de los Minions decidio guardar sus ahorros en el Banco Villano.
 $1,000 con una tasa de interés del 8% anual durante 3 años, con capitalización anual.
"""

# --- Fórmula del Valor Futuro en Interés Compuesto ---  
# VF = VP * (1 + i)^n

"""Datos  
VP -> Valor presente = $1,000.
i -> Tasa de interés anual en decimal (divide entre 100) = 8% = 0.08  
n -> Tiempo años = 3 

Periodo de capitalizacion = Anual
"""  

from decimal import Decimal 
import locale 

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

def formato_usd(valor):
    return f"${valor:,.2f} USD"

def interes_compuesto():
    try: 
        valor_presente = Decimal(input("Dame el valor presente: "))

        unidad_tiempo = int(input("¿Quieres ingresar el tiempo en 1. Meses o 2. Años? "))

        if unidad_tiempo == 1:
            numero_tiempo = Decimal(input("Dame el tiempo en meses: "))
        elif unidad_tiempo == 2:
            numero_tiempo = Decimal(input("Dame el tiempo en años: ")) * 12  
        else:
            print("❌ Opción no válida.")
        
        tasa = Decimal(input("Dame la tasa sin el %: ")) / 100

        tipo_periodo_tiempo = int(input("""Periodo de Capitalizacion: 
        1. Mensual (1 mes)
        2. Bimestral (2 meses)
        3. Trimestral (3 meses) 
        4. Semestral (6 meses)
        5. Anual (12 meses)
        ->                              """))

        if tipo_periodo_tiempo == 1:
            divisor = 1
        elif tipo_periodo_tiempo == 2:
            divisor = 2
        elif tipo_periodo_tiempo == 3:
            divisor = 3
        elif tipo_periodo_tiempo == 4:
            divisor = 6
        elif tipo_periodo_tiempo == 5:
            divisor = 12
        else:
            print("❌ Opción no válida.")

        numero_periodo_tiempo = numero_tiempo / divisor

        f_interes_compuesto = valor_presente * (1 + tasa)** numero_periodo_tiempo

        print(f"✅ El valor futuro de la inversión es: {formato_usd(f_interes_compuesto)}")

    except Exception as error:
        print(f"⚠️ Hubo un error: {error}")
            
interes_compuesto()






















































