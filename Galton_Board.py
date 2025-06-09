import random
import matplotlib.pyplot as plt

def simulate_galton_board(balls, levels):
    '''
    Simula una Galton Board (máquina de Galton) donde una cantidad de bolitas 
    caen a través de varios niveles, decidiendo aleatoriamente en cada nivel 
    si se mueven a la izquierda o a la derecha.

    Parámetros:
    balls (int): Número de bolitas a simular.
    levels (int): Número de niveles (filas de pines) por los que cae cada bolita.

    Retorna:
    list: Lista con la cantidad de bolitas que cayeron en cada bin (posición final).
    '''
    bins = [0] * (levels + 1)  # Se crean bins para niveles + 1 posiciones posibles

    for i in range(balls):
        position = 0  # posición inicial de la bola (0)
        
        for j in range(levels):
            if random.random() < 0.5:
                position += 1  # se mueve a la derecha
        
        bins[position] += 1  # registra en qué bin cayó la bola

    return bins

def graficar(bins):
    '''
    Genera un gráfico de barras a partir de los resultados de la simulación 
    de una Galton Board, mostrando cuántas bolitas cayeron en cada bin.

    Parámetros:
    bins (list): Lista con la cantidad de bolitas que cayeron en cada posición final.

    Retorna:
    None: Solo muestra la gráfica en pantalla.
    '''
    posiciones = list(range(len(bins)))  # posiciones de los bins
    
    plt.figure(figsize=(10, 6))
    plt.bar(posiciones, bins, color='skyblue', edgecolor='black')
    plt.title('Simulación de Galton Board (12 niveles, 3000 bolitas)')
    plt.xlabel('Bin (posición final)')
    plt.ylabel('Cantidad de bolitas')
    plt.grid(axis='y', alpha=0.5)
    plt.xticks(posiciones)
    plt.show()

# Simulamos 3000 bolas y 12 niveles
resultado = simulate_galton_board(3000, 12)

# Mostramos cuántas bolas cayeron en cada bin
for bin_number in range(len(resultado)):
    print(f"Bin {bin_number}: {resultado[bin_number]} bolas")

# Graficamos el resultado
graficar(resultado)
