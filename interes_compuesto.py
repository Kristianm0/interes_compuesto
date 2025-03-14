# @Kristianmartinezcolina  -> Programación en Python
"📌 Ejercicio de interés compuesto -> ¿Cómo calcular el valor futuro de una inversión?"

""" Ejemplo con Gru de Mi Villano Favorito  
Gru decide invertir $1,000 en una cuenta bancaria que ofrece un 3% de interés compuesto mensual.  
Si deja su dinero en la cuenta durante 1 año ¿Cuál será el valor futuro de la inversión de Gru después de 1 año?  
"""

# --- Fórmula del Valor Futuro en Interés Compuesto ---  
# VF = VP * (1 + i)^n

"""Datos  
# VP -> Capital inicial = $1,000  
# i -> Tasa de interés mensual en decimal (divide entre 100) = 3% = 0.03  
# n -> Tiempo en meses = 18  
"""  

from decimal import Decimal

def calcular_interes_compuesto():
    try:
        # Pedir el capital inicial
        valor_presente = Decimal(input("Dame el Valor Presente: "))

        # Pedir al usuario cómo está expresada la tasa de interés
        tipo_tasa = int(input("""
        Elige cómo está expresada la tasa de interés:
        1. Tasa anual
        2. Tasa mensual
        3. Tasa diaria
        Opción: """))

        # Pedir la tasa de interés y convertirla a decimal
        tasa_interes = Decimal(input("Dame la tasa de interés sin el %: ").replace(",", ".")) / 100

        # Pedir el tiempo en la unidad correspondiente a la tasa de interés
        if tipo_tasa == 1:
            tiempo = Decimal(input("Dame el tiempo en años: "))
        elif tipo_tasa == 2:
            tiempo = Decimal(input("Dame el tiempo en meses: "))  # Mantener en meses
        elif tipo_tasa == 3:
            tiempo = Decimal(input("Dame el tiempo en días: "))  # Mantener en días
        else:
            raise ValueError("Opción no válida. Debes elegir 1, 2 o 3.")

        # Calcular la tasa y tiempo en la misma unidad
        if tipo_tasa == 1:
            tasa_interes = tasa_interes  # La tasa ya está en años
            n = tiempo  # Tiempo en años
        elif tipo_tasa == 2:
            tasa_interes = tasa_interes / 12  # Convertimos a tasa mensual
            tiempo = tiempo  # Mantener tiempo en meses
        elif tipo_tasa == 3:
            tasa_interes = tasa_interes / 365  # Convertimos a tasa diaria
            tiempo = tiempo  # Mantener tiempo en días
        
        # Aplicar la fórmula de interés compuesto
        valor_futuro = valor_presente * (1 + tasa_interes) ** tiempo

        # Mostrar resultado con dos decimales
        print(f"El valor futuro de la inversión es: ${valor_futuro:.2f}")

    except Exception as e:
        print("😔 Se ha producido un error inesperado.")
        print(f"Detalles del error: {e}")

# Llamar la función para calcular interés compuesto
calcular_interes_compuesto()
