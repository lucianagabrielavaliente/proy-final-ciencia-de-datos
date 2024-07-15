# Proyecto Final Ciencia de Datos

Este repositorio contiene el código y los archivos relacionados con el proyecto final de la cátedra "Ciencia de Datos" de la carrera de Ingeníeria en Sistemas de Información, en la UTN-FRCU. El objetivo de este proyecto es aplicar los conceptos aprendidos durante el curso para estudiar la incidencia de trastornos del sueño en la población.

## Objetivo General

El proyecto se centra en reducir la incidencia de trastornos de sueño entre la población en un 20% dentro del próximo año.

## Recursos

- **Datos**: Se cuenta con un dataset que incluye información sobre la población, como la duración y calidad del sueño, niveles de actividad física, estrés, entre otros.
- **Tecnologías**: Para el modelado y analisis de dato se utilizaron RapidMiner y Jupyter.

## Objetivos de Minería de Datos
Utilizando información histórica sobre diferentes personas y su estado de salud con trastornos del sueño, el objetivo es:

1. Identificar patrones entre el estrés, el índice BMI, género, nivel de actividad física, ocupación, edad, presión sanguínea, frecuencia cardíaca, cantidad de pasos y la posibilidad de sufrir un trastorno del sueño.
2. Desarrollar un modelo de árbol de decisión para predecir la presencia de apnea del sueño o insomnio tanto para individuos femeninos, masculinos y mixtos.

## Restricciones

- Los trastornos del sueño considerados incluyen únicamente la apnea e insomnio.
- La calidad del sueño es una percepción subjetiva de cada paciente.
- La edad de los sujetos está en el intervalo de 27 a 59 años.
- Todos los individuos forman parte de la población laboral activa, excluyendo a la población desempleada o jubilada.

## Suposiciones

- Las mediciones (Heart Rate, Daily Steps, Blood Pressure) tienen una precisión del 90%.
- Los valores de Sleep Duration, Stress Level y Quality of Sleep se obtuvieron bajo un estudio de polisomnografía.

## Información sobre los Datos

El dataset analizado consta de 374 registros que incluyen información detallada sobre diversas características de salud y estilo de vida. Cada registro se identifica de manera única mediante el campo "Person ID". Los datos se centran en evaluar variables clave como género, edad, ocupación, duración y calidad del sueño, nivel de actividad física, niveles de estrés, categoría de índice de masa corporal (BMI), presión sanguínea, frecuencia cardíaca, pasos diarios y la presencia de trastornos del sueño.

- La edad promedio en el conjunto de datos es de 42.18 años, con una mediana y moda de 43 años.
- El campo "Género" muestra una distribución casi igual entre hombres (188) y mujeres (185).
- La duración promedio del sueño es de 7.13 horas.
- La calidad del sueño se evalúa en una escala del 1 al 10, con una media de 7.51.
- El nivel de actividad física tiene una media de 59.08.
- El nivel de estrés promedio es de 5.39 en una escala del 1 al 10.
- La frecuencia cardíaca promedio es de 70.17 latidos por minuto.
- La presión sanguínea muestra una distribución diversa.

## DataSets

Este repositorio contiene los datasets utilizados en nuestro estudio

1. **Original (Proporcionado por la Cátedra)**:
   - Este dataset es el proporcionado por la cátedra o fuente original. Contiene información sin modificaciones y es la base para nuestro análisis.

2. **Dataset con Separación de Valores Extremos de Presión Sanguínea**:
   - Hemos creado un segundo dataset en el que separamos los valores extremos del parámetro "Blood Pressure" (presión sanguínea). Esto nos permite explorar cómo afectan estos valores atípicos a nuestros resultados.

3. **Dataset Limpio**:
   - El tercer dataset es una versión depurada y procesada. Hemos realizado limpieza de datos, manejo de valores faltantes y otras transformaciones para garantizar la calidad y coherencia de los datos.
  
## Ejecución del Proyecto

### Clonar el repositorio de forma local
git clone https://github.com/lucianagabrielavaliente/proy-final-ciencia-de-datos.git

## Configuración del Entorno Virtual (Python)

Para gestionar las dependencias del proyecto de manera aislada, se recomienda crear un entorno virtual de Python. Utiliza los siguientes comandos en tu terminal

### Crear el entorno virtual

python -m venv pyenv

### Activar el entorno virtual (en Windows)

pyenv\Scripts\activate

### Activar el entorno virtual (en macOS/Linux)

source pyenv/bin/activate

### Instaalación de dependencias

pip install -r requirements.txt

### Ejecución de la API

uvicorn app:app --reload
