# calculadora-nem-python
Script en Python para calcular y proyectar promedios escolares NEM en la educación media chilena.
# Calculadora Proyectiva de NEM 🎓

Herramienta interactiva desarrollada en Python para calcular promedios de Notas de Enseñanza Media (NEM) y proyectar los rendimientos requeridos para alcanzar objetivos académicos en el sistema escolar chileno.

## ⚙️ Funcionalidades Técnicas

* **Lógica Dinámica de Cursos:** Algoritmo estructurado mediante condicionales `if/elif` que ajusta las solicitudes de datos y fórmulas algebraicas según el nivel académico actual del usuario (1° a 4° Medio).
* **Manejo de Excepciones y Caso Borde:** Validación de entradas para prevenir cursos fuera de rango (1-4) y detección automática de metas matemáticamente imposibles (promedios proyectados superiores a 7.0).
* **Formateo y Redondeo:** Implementación de la función `round()` para presentar resultados con precisión decimal de un dígito, adaptado al sistema de notas nacional.

## 🚀 Cómo Ejecutarlo

1. Asegúrate de tener instalado Python 3.
2. Clona o descarga este repositorio.
3. Ejecuta el script desde la terminal:
   ```bash
   python main.py
   ```
