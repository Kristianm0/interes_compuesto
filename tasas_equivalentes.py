#@Kristian Martinez Colina | Programacion Python
"""📘 ¿Qué son las tasas equivalentes?
Son tasas de interés que, aunque están expresadas en periodos diferentes 
(mensual, trimestral, semestral, anual...), producen el mismo rendimiento 
total al final del año si se capitalizan al mismo ritmo.

"""
"""📗 ¿Qué es la TEA?
TEA = Tasa Efectiva Anual

Es cuánto crece tu dinero en un año completo, considerando interés compuesto.
Se expresa como un porcentaje anual, pero con capitalización implícita.
"""
"""📙 ¿Qué es la TPN?
TPS = Tasa Periódica Según el Tiempo

Es cuánto crece tu dinero en cada periodo determinado (mes, trimestre, semestre, etc.).
Por ejemplo, la Tasa Periódica Semestral (TPS) muestra cuánto crece tu dinero cada 6 meses.
"""
"""📐 Fórmula para convertir de TEA a TPS (tasa periódica equivalente):

    TPS = (1 + TEA)^(1/n) - 1

📌 Datos:
- TEA: Tasa Efectiva Anual (en decimal, ej. 12% = 0.12)
- n: número de periodos en un año según la periodicidad:
      "mensual"     → 12
      "bimestral"   → 6
      "trimestral"  → 4 
      "semestral"   → 2 
      "diaria"      → 365
"""

"""Explicado con BoJack Horseman
Las tasas equivalentes son como distintas formas de contar la misma historia.

Puedes ver un episodio por semana o hacer maratón y ver toda la temporada en un día,
pero al final, la historia es la misma, solo cambia cómo y cuándo la ves.

Igual pasa con las tasas: cambian según el periodo (mes, trimestre, año),
pero todas te cuentan cuánto crece tu dinero al final.
"""
"""Ejercicio
BoJack invierte parte de sus regalías en un fondo administrado por Todd que ofrece una TEA (Tasa Efectiva Anual) del 24%.

Princess Carolyn necesita convertir esa tasa a otras periodicidades para analizar distintas oportunidades.

Pregunta: ¿A qué tasa equivale esa TEA del 24% en los siguientes periodos?

Mensual
Bimestral
Trimestral
Semestral
Diaria (suponiendo 365 días al año)
"""


from decimal import Decimal 


def tasas_equivalentes():
    while True:
        try:
            tasa_efectiva_anual = Decimal(input("📈 Dame la tasa efectiva anual (sin el %): ")) / 100

            tipo_periodo_tiempo = int(input("""
📅 Periodo de Capitalización: 
    0. Diaria (365) 
    1. Mensual (12 meses)
    2. Bimestral (2 meses) 
    3. Trimestral (3 meses)
    4. Semestral (6 meses)
                                            
    (Tenga en cuenta usa la cantidad de periodos que tiene un año)
    Ej: En un año hay 2 Semestres, por ende sera igual a 2
-> Selecciona una opción: """))
            
            # Asignar divisor según la elección del usuario
            if tipo_periodo_tiempo == 0:
                capitalizaciones_por_año = 365
                periodicidad = "Diaria"
            elif tipo_periodo_tiempo == 1:
                capitalizaciones_por_año = 12 
                periodicidad = "Mensual"
            elif tipo_periodo_tiempo == 2:
                capitalizaciones_por_año = 6
                periodicidad = "Bimestral"
            elif tipo_periodo_tiempo == 3:
                capitalizaciones_por_año = 4
                periodicidad = "Trimestral"
            elif tipo_periodo_tiempo == 4:
                capitalizaciones_por_año = 2
                periodicidad = "Semestral"
            else:
                print("❌ Opción no válida.")
                continue

            exponente_tiempo = Decimal(capitalizaciones_por_año)

            tasa_periodica = (1 + tasa_efectiva_anual) ** (1 / exponente_tiempo) - 1

            tasa_periodica_porcentaje = tasa_periodica * 100

            tasa_nominal_anual_vencido = tasa_periodica * exponente_tiempo

            tasa_nominal_anual_porcentaje = tasa_nominal_anual_vencido * 100

            print(f"✅ Tasa Periodica es de {tasa_periodica_porcentaje:,.4f}% ({periodicidad})")
 
            print(f"✅ Tasa es de {tasa_nominal_anual_porcentaje:,.4f}% Nominal Anual ({periodicidad}) Vencido")

        except Exception as error:
            print(f"⚠️ Hubo un error: {error}")

        # Preguntar si desea continuar
        continuar = input("¿Deseas calcular otra tasa? (s/n): ").strip().lower()
        if continuar != 's':
            print("👋 ¡Hasta la próxima!")
            break

tasas_equivalentes()











