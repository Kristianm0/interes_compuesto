# 📌 Ejercicios de Interés Compuesto en Python

Este repositorio contiene ejercicios de interés compuesto explicados con ejemplos divertidos basados en personajes animados.

---

## 📈 Cálculos de Interés Compuesto

### 🔥 Tasa de una Inversión
Mario guarda **$5,000** y después de **3 años** tiene **$6,500**. ¿Cuál es la tasa de interés anual?

```python
from decimal import Decimal
import math

def tasas_interes_compuesto():
    valor_futuro = Decimal(input("Valor futuro: "))
    valor_presente = Decimal(input("Valor presente: "))
    numero_tiempo = Decimal(input("Tiempo en años: "))
    tasa = (valor_futuro / valor_presente) ** (1 / numero_tiempo) - 1
    print(f"Tasa anual: {tasa * 100:.2f}%")

tasas_interes_compuesto()
```

### 💰 Valor Futuro de una Inversión
Kevin invierte **$1,000** al **8% anual** durante **3 años**.

```python
from decimal import Decimal 

def interes_compuesto():
    vp = Decimal(input("Valor presente: "))
    n = Decimal(input("Tiempo en años: "))
    i = Decimal(input("Tasa (%): ")) / 100
    vf = vp * (1 + i) ** n
    print(f"Valor futuro: ${vf:,.2f} USD")

interes_compuesto()
```

### ⏳ Tiempo Necesario para Alcanzar una Meta
El Macho quiere **$80,000**, pero solo tiene **$25,000**. ¿Cuánto tiempo tardará al **7% anual**?

```python
from decimal import Decimal
from math import log

def tiempo_interes_compuesto():
    vf = Decimal(input("Valor futuro: "))
    vp = Decimal(input("Valor presente: "))
    i = Decimal(input("Tasa (%): ")) / 100
    n = log(vf / vp) / log(1 + i)
    print(f"Tiempo estimado: {n:.2f} años")

tiempo_interes_compuesto()
```

---

## 📌 Conéctate conmigo
Más contenido sobre Python y Finanzas en:
🔹 GitHub: [https://github.com/Kristianm0/](https://github.com/Kristianm0/)
🔹 Instagram: [/kristianmartinezcolina](https://instagram.com/kristianmartinezcolina)
🔹 TikTok: [/kristianmartinezcolina](https://www.tiktok.com/@kristianmartinezcolina)
🔹 LinkedIn: [/kristianmartinezcolina](https://www.linkedin.com/in/kristianmartinezcolina)

👉 Todos los enlaces: [https://kristianmartinezcolina.carrd.co/](https://kristianmartinezcolina.carrd.co/)

