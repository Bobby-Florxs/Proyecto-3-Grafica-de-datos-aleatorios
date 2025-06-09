# 🎲 Simulación de Galton Board 

Este proyecto consiste en una simulación de una **Galton Board** (también conocida como máquina de Galton o máquina de los frijoles), utilizando Python. La máquina simula el comportamiento de bolitas que caen a través de una serie de niveles y deciden aleatoriamente moverse a la izquierda o a la derecha, acumulándose al final en diferentes posiciones.

---

## 📖 Descripción

En este proyecto:
- Se simulan **3000 bolitas** que atraviesan **12 niveles**.
- Cada bolita tiene una probabilidad del **50% de ir a la izquierda o a la derecha** en cada nivel.
- Al finalizar su recorrido, se registra en qué bin (posición final) cayó cada bolita.
- Se grafica un histograma que muestra la distribución final de bolitas en los bins.

Se espera como resultado una **distribución aproximadamente normal** (curva de campana) debido a la naturaleza estadística del proceso.

---

## 📦 Tecnologías y Librerías

- **Python 3**
- **random** (módulo estándar)
- **matplotlib** (para graficar)

---

## 📁 Estructura del código

El proyecto consta de dos funciones principales:

- `simulate_galton_board(balls, levels)`
  - Simula la caída de las bolitas.
  - Retorna una lista con la cantidad de bolitas que cayeron en cada bin.
  
- `graficar(bins)`
  - Recibe los resultados de la simulación.
  - Genera una gráfica de barras que muestra la distribución de bolitas.

Cada función está debidamente documentada con **docstrings** para facilitar su comprensión.

---

## 🚀 Cómo ejecutar el proyecto

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git
   cd tu_repositorio
