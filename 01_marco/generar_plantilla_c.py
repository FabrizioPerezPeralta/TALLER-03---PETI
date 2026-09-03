import pandas as pd

# Leer los objetivos del PGD generados en el paso B
try:
    pgd_obj = pd.read_csv("MP03_objetivos_pgd.csv")
    objetivos_pgd = pgd_obj['codigo'].tolist()
except:
    objetivos_pgd = ["OGD 1", "OGD 2", "OGD 3", "OGD 4", "OGD 5", "OGD 6", "OGD 7"]

# Crear el DataFrame vacío con las columnas solicitadas en el Paso C
columnas = [
    "Objetivo del PGD", 
    "¿Declara articulación con el PEI?", 
    "Objetivo del PEI al que se articula", 
    "¿La articulación es verificable en el texto?", 
    "¿Tiene indicador?", 
    "¿Tiene línea base?", 
    "¿Tiene meta anual?", 
    "Proyectos asociados"
]

df = pd.DataFrame(columns=columnas)
df["Objetivo del PGD"] = objetivos_pgd

# Guardar a CSV
df.to_csv("MP04_articulacion.csv", index=False, encoding='utf-8')
print("Plantilla MP04_articulacion.csv generada con éxito.")
