import matplotlib.pyplot as plt

# Datos
datos = [
    {"fecha": "02 de Enero - 2024", 
     "peso": 225, 
     "brazo": {"izquierdo": 13.5, "derecho": 13}, 
     "cintura": {"min": 38, "max": 41.3}, 
     "pliegues": {"min": 44.2, "max": 30}, 
     "pantorrillas": {"izquierda": 17.1, "derecha": 17}, 
     "pierna": {"izquierda": 27, "derecha": 26.3}},
    
    {"fecha": "02 de Febrero - 2024", 
     "peso": 225.6, 
     "brazo": {"izquierdo": 15, "derecho": 14}, 
     "cintura": {"min": 37.1, "max": 39.7}, 
     "pliegues": {"min": 30.3, "max": 30}, 
     "pantorrillas": {"izquierda": 17.3, "derecha": 17.3}, 
     "pierna": {"izquierda": 27.2, "derecha": 27}},
    
    {"fecha": "02 de Marzo - 2024", 
     "peso": 219.5, 
     "brazo": {"izquierdo": 15, "derecho": 14.4}, 
     "cintura": {"min": 39.6, "max": 40}, 
     "pliegues": {"min": 28, "max": 20}, 
     "pantorrillas": {"izquierda": 16.6, "derecha": 17}, 
     "pierna": {"izquierda": 27.3, "derecha": 27.3}},
    
    {"fecha": "02 de Abril - 2024", 
     "peso": 216.3, 
     "brazo": {"izquierdo": 14.1, "derecho": 14.3}, 
     "cintura": {"min": 35.3, "max": 39}, 
     "pliegues": {"min": 20, "med": 30, "max": 20.3}, 
     "pantorrillas": {"izquierda": 16.4, "derecha": 16.5}, 
     "pierna": {"izquierda": 27, "derecha": 27}},
    
    {"fecha": "02 de Mayo - 2024", 
     "peso": 218.8, 
     "brazo": {"izquierdo": 14.1, "derecho": 14.3}, 
     "cintura": {"min": 35.3, "max": 38}, 
     "pliegues": {"min": 20, "med": 20, "max": 20}, 
     "pantorrillas": {"izquierda": 16.5, "derecha": 16.6}, 
     "pierna": {"izquierda": 27, "derecha": 26.9}},
    
    {"fecha": "02 de Junio - 2024", 
     "peso": 214.5, 
     "brazo": {"izquierdo": 14.4, "derecho": 14.0}, 
     "cintura": {"min": 34.5, "max": 37.4}, 
     "pliegues": {"min": 19, "med": 20, "max": 19}, 
     "pantorrillas": {"izquierda": 16.3, "derecha": 16.4}, 
     "pierna": {"izquierda": 26.6, "derecha": 26.1}, 
     "pecho": 41},
    
    {"fecha": "02 de Julio - 2024", 
     "peso": 213.2, 
     "brazo": {"izquierdo": 14, "derecho": 13.7}, 
     "cintura": {"min": 34, "max": 37}, 
     "pliegues": {"min": 18.5, "med": 20, "max": 18.5}, 
     "pantorrillas": {"izquierda": 16.4, "derecha": 16.5}, 
     "pierna": {"izquierda": 26, "derecha": 26.2}, 
     "pecho": 41.1},
    
    {"fecha": "02 de Agosto - 2024", 
     "peso": 211.6, 
     "brazo": {"izquierdo": 14.1, "derecho": 14.1}, 
     "cintura": {"min": 33.7, "max": 36.4}, 
     "pliegues": {"min": 20.2, "max": None}, 
     "pantorrillas": {"izquierda": 16.7, "derecha": 16.6}, 
     "pierna": {"izquierda": 26.1, "derecha": 27}, 
     "pecho": 40},
    
    {"fecha": "02 de Septiembre - 2024", 
     "peso": 212.6, 
     "brazo": {"izquierdo": 14.3, "derecho": 14.3}, 
     "cintura": {"min": 35, "max": 38}, 
     "pliegues": {"min": 20.2, "max": None}, 
     "pantorrillas": {"izquierda": 16.4, "derecha": 16.4}, 
     "pierna": {"izquierda": 27, "derecha": 27}, 
     "pecho": 40},
    
    {"fecha": "02 de Octubre - 2024", 
     "peso": 215, 
     "brazo": {"izquierdo": 15, "derecho": 15}, 
     "cintura": {"min": 36, "max": 37.4}, 
     "pliegues": {"min": 20.4, "max": None}, 
     "pantorrillas": {"izquierda": 17.2, "derecha": 17.2}, 
     "pierna": {"izquierda": 27.1, "derecha": 27.3}, 
     "pecho": 42.5},

    {"fecha": "02 de Noviembre - 2024",
        "peso": 214.8,
        "brazo": {"izquierdo": 15.7, "derecho": 15.4},
        "cintura": {"min": 35, "max": 38.1},
        "pliegues": {"min": 20.3, "max": None},
        "pantorrillas": {"izquierda": 16.7, "derecha": 17},
        "pierna": {"izquierda": 26.4, "derecha": 26.7},
        "pecho": 41},

    {"fecha": "02 de Diciembre - 2024",
        "peso": 206.1,
        "brazo": {"izquierdo": 15, "derecho": 14.7},
        "cintura": {"min": 34, "max": 37.7},
        "pliegues": {"min": 20.2, "max": None},
        "pantorrillas": {"izquierda": 16.4, "derecha": 16.4},
        "pierna": {"izquierda": 25.7, "derecha": 25.7},
        "pecho": 42.3}
    
]


# Fechas para el eje x
fechas = [dato["fecha"] for dato in datos]

# Función para graficar cada métrica
def graficar_progreso(titulo, valores, ylabel):
    plt.figure(figsize=(10, 5))
    plt.plot(fechas, valores, marker='o')
    plt.title(titulo)
    plt.xlabel('Fecha')
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# 1. Peso
peso = [dato["peso"] for dato in datos]
graficar_progreso("Progreso de Peso", peso, "Peso (lbs)")

# 2. Brazo (promedio de izquierdo y derecho)
brazo = [(dato["brazo"]["izquierdo"] + dato["brazo"]["derecho"]) / 2 for dato in datos]
graficar_progreso("Progreso del Brazo", brazo, "Brazo (pulgadas)")

# 3. Cintura (promedio de min y max)
cintura = [(dato["cintura"]["min"] + dato["cintura"]["max"]) / 2 for dato in datos]
graficar_progreso("Progreso de Cintura", cintura, "Cintura (pulgadas)")

# 4. Pliegues (promedio si hay varios valores)
pliegues = []
for dato in datos:
    valores_pliegues = list(dato["pliegues"].values())
    valores_pliegues = [v for v in valores_pliegues if v is not None]  # Ignorar valores None
    promedio_pliegues = sum(valores_pliegues) / len(valores_pliegues)
    pliegues.append(promedio_pliegues)
graficar_progreso("Progreso de Pliegues", pliegues, "Pliegues (mm)")

# 5. Pantorrillas (promedio de izquierda y derecha)
pantorrillas = [(dato["pantorrillas"]["izquierda"] + dato["pantorrillas"]["derecha"]) / 2 for dato in datos]
graficar_progreso("Progreso de Pantorrillas", pantorrillas, "Pantorrillas (pulgadas)")

# 6. Pierna (promedio de izquierda y derecha)
pierna = [(dato["pierna"]["izquierda"] + dato["pierna"]["derecha"]) / 2 for dato in datos]
graficar_progreso("Progreso de Pierna", pierna, "Pierna (pulgadas)")

# 7. Pecho
pecho = [dato.get("pecho", None) for dato in datos]  # Usar None si no hay dato
graficar_progreso("Progreso de Pecho", pecho, "Pecho (pulgadas)")