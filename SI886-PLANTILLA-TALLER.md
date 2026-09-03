UNIVERSIDAD PRIVADA DE TACNA

FACULTAD DE INGENIERÍA

ESCUELA PROFESIONAL DE INGENIERÍA DE SISTEMAS

INFORME DE LABORATORIO N.º 03

PLANEAMIENTO ESTRATÉGICO DE TI · SI-886

TALLER - Análisis comparado del PEI y del Plan de Gobierno Digital de una entidad real

Semana N.º 03    ·    Unidad 1    ·    Grupo N.º __

Integrantes

Fabrizio Salvador Elias Perez Peralta (2023077476)

Docente

Dr. Oscar Juan Jimenez Flores

Tacna, Perú

---

# 1. Información sobre el evento práctico

## 1.1 Título del evento práctico
Análisis documental comparado del Plan Estratégico Institucional y del Plan de Gobierno Digital de una entidad pública peruana, con verificación de su articulación y construcción del mapa de instrumentos de planeamiento aplicable a la organización objeto de estudio.

## 1.2 Objetivos
- Localizar y descargar el PEI y el PGD vigentes de una entidad pública peruana, ambos documentos públicos.
- Verificar la articulación entre ambos. Rastrear cada objetivo del PGD hasta un objetivo del PEI.
- Evaluar el PGD contra la estructura exigida por los Lineamientos de la RSGD 005-2018-PCM/SEGDI.
- Construir el mapa de instrumentos de planeamiento aplicable a la organización objeto de estudio.
- Determinar el objetivo superior de enganche del PETI (Plan Estratégico de Tecnologías de Información) que se está construyendo.
- Redactar la Sección 1.2 del PETI. Marco de planeamiento y articulación.

## 1.3 Tiempo de duración
100 minutos: 60 de taller guiado y 40 de avance asistido.

## 1.4 Resultados de aprendizaje
- **RA1** Aplica la dirección estratégica, definiendo la misión y visión.
- **RA2** Desarrolla el análisis FODA.

## 1.5 Recursos

| Recurso | Detalle |
|---|---|
| **Portal del Estado Peruano** | https://www.gob.pe — sección de transparencia de la SUNAT |
| **CEPLAN** | https://www.gob.pe/ceplan — *Guía para el Planeamiento Institucional* |
| **Lineamientos del PGD** | https://cdn.www.gob.pe/uploads/document/file/356863/Anexo_I_Lineamientos_PGD.pdf |
| **Normativa de gobierno digital** | https://www.gob.pe/institucion/pcm/colecciones/147-normativa-sobre-gobierno-digital |
| **Python 3.11+ con pdfplumber, pandas** | Extracción de texto de los PDF |
| **draw.io / Python** | Mapa de instrumentos |
| **LibreOffice Calc / Excel** | Matriz de articulación |

## 1.6 Seguridad
1. Los PEI y PGD son documentos públicos; se descargaron de los portales institucionales de transparencia (SUNAT). Se registra la URL y la fecha de descarga.
2. El análisis se realizó sobre el documento vigente aprobado por resolución.
3. El análisis fue académico y metodológico, evaluando la estructura y la articulación del documento.

# 2. Procedimiento o metodología

## Paso A — Localizar los documentos
Se seleccionó a la Superintendencia Nacional de Aduanas y de Administración Tributaria (SUNAT). Se procedió a descargar desde gob.pe el Plan Estratégico Institucional (PEI) 2026-2030 (Aprobado por Res. 000395-2025) y el Plan de Gobierno Digital (PGD) 2025-2027 (Aprobado por Res. 000301-2024). Los archivos PDF de los Anexos se guardaron en la carpeta `evidencias/`.

## Paso B — Extraer la estructura de los documentos
Se ejecutaron los scripts de Python `MP02_extraccion.py` y `MP03_objetivos.py` provistos por el taller, haciendo uso de la librería `pdfplumber` para leer ambos PDFs. Se logró identificar 24 objetivos en el PEI y 5 Objetivos de Gobierno Digital (OGD) en el PGD. Los resultados se guardaron en la carpeta `01_marco/` en archivos `.csv`.

## Paso C — Verificar la articulación
Utilizando los objetivos extraídos, se analizó la "Matriz de Vinculación" presente en el PGD (páginas 63-66). Se llenó la tabla `MP04_articulacion.csv` confirmando qué OEI del PEI corresponde a cada OGD. Finalmente, se ejecutó el script `MP05_calidad.py` arrojando un 100% de objetivos completos (articulados, con indicador, línea base y meta).

## Paso D — Mapa de instrumentos de la organización propia
Se construyó el diagrama `mapa_instrumentos.png` mostrando la jerarquía de instrumentos para la SUNAT (pública). Asimismo, se llenó la tabla `MP07_instrumentos_organizacion.csv` con la vigencia y el estado de aprobación formal de cada uno.

## Paso E — Redactar la Sección 1.2 del PETI
Con toda la información recolectada y analizada, se redactó el archivo `1.2_marco_planeamiento.md` incluyendo la justificación del objetivo superior de enganche, el esquema normativo y la lección aprendida del análisis comparado.

# 3. Resultados

| # | Resultado esperado | ¿Se logró? | Evidencia |
|---|---|---|---|
| 1 | PEI y PGD localizados, con resolución de aprobación | Sí | [URL del CSV en GitHub] |
| 2 | Estructura de ambos documentos extraída | Sí | [URL de MP02_estructura_*.csv en GitHub] |
| 3 | Objetivos del PEI y del PGD identificados | Sí | [URL de MP03_objetivos_*.csv en GitHub] |
| 4 | Matriz de articulación completa | Sí | [URL de MP04_articulacion.csv en GitHub] |
| 5 | Porcentaje de objetivos completos calculado | Sí | [URL de salida de consola en GitHub] |
| 6 | Evaluación del PGD contra los 9 componentes de Lineamientos | Sí | [URL de MP06_estructura_lineamientos.csv en GitHub] |
| 7 | Mapa de instrumentos de la organización propia | Sí | [URL de graficos/mapa_instrumentos.png en GitHub] |
| 8 | Tabla de instrumentos de la organización | Sí | [URL de MP07_instrumentos_organizacion.csv en GitHub] |
| 9 | Objetivo superior de enganche identificado | Sí | [URL de 1.2_marco_planeamiento.md en GitHub] |
| 10 | Declaración de enfoque estratégico con cláusula de exclusión | Sí | [URL de 1.2_marco_planeamiento.md en GitHub] |
| 11 | Sección 1.2 redactada | Sí | [URL de 1.2_marco_planeamiento.md en GitHub] |
| 12 | Etiqueta v0.3 en Git | Sí | [URL de etiqueta en GitHub] |

*(Nota: Sustituir los textos "[URL...]" por los enlaces reales a tu repositorio de GitHub antes de exportar a PDF).*

# 4. Conclusiones

1. La articulación entre planes en la SUNAT es altamente medible y verificable. El análisis nos demostró que la institución cuenta con un **100% de calidad en su matriz de vinculación**, donde cada OGD tiene un sustento en el PEI, indicadores explícitos, líneas base y metas.
2. Un objetivo de TI (como un OGD) sin un ancla en un objetivo institucional compite por presupuesto sin argumentos sólidos. La forma en que la SUNAT amarra sus proyectos tecnológicos directamente al OEI principal de recaudación asegura su viabilidad financiera.
3. El enfoque estratégico real se revela en lo que la organización financia (Pilar 2 de la SUNAT). Construir un Plan de Gobierno Digital desconectado de este pilar produciría un plan inviable e inútil para la entidad.

# 5. Cuestionario

*(La guía de esta semana no incluye cuestionario a resolver).*

# 6. Referencias bibliográficas

- Superintendencia Nacional de Aduanas y de Administración Tributaria (2024). *Resolución de Superintendencia N.º 000301-2024/SUNAT*. Aprueba el Plan de Gobierno Digital 2025-2027 de la SUNAT.
- Superintendencia Nacional de Aduanas y de Administración Tributaria (2025). *Resolución de Superintendencia N.º 000395-2025/SUNAT*. Aprueba el Plan Estratégico Institucional para el período 2026-2030 de la SUNAT.
- Presidencia del Consejo de Ministros (2018). *Resolución de Secretaría de Gobierno Digital 005-2018-PCM/SEGDI*. Lineamientos para la formulación del Plan de Gobierno Digital.

# 7. Anexos

- Anexo A: `01_marco/MP04_articulacion.csv`
- Anexo B: `graficos/mapa_instrumentos.png`
- Anexo C: `01_marco/1.2_marco_planeamiento.md`
