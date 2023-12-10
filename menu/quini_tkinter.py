import tkinter as tk
import random

# Últimos números acertados y cantidad de ganadores para cada premio
ultimos_numeros_acertados = [2, 3, 8, 11, 13, 14, 15, 20, 30, 32, 34, 36, 37, 38, 44, 7, 17, 21, 25, 29, 30, 8, 13, 15, 34, 37, 44, 3, 14, 20, 32, 37, 38, 2, 11, 20, 30, 36, 37]

# Función para generar números personalizados
def generate_custom_numbers():
    # Establecer la semilla del generador de números aleatorios
    random.seed()  # Utiliza una semilla por defecto (basada en el tiempo, pero sin importar time)

    numeros_generados_acertados = []

    for _ in range(6):
        # Elegir si se usará un número proporcionado o aleatorio
        usar_proveido = random.uniform(0, 1) < 0.5

        if usar_proveido and ultimos_numeros_acertados:
            numero_elegido = random.choice(ultimos_numeros_acertados)
        else:
            numero_elegido = random.randint(0, 45)

        numeros_generados_acertados.append(numero_elegido)

    # Mezclar los números generados
    random.shuffle(numeros_generados_acertados)
    
    probabilidad_total = random.uniform(0, 1)  # Modifica esto según tu lógica de probabilidad
    
    return numeros_generados_acertados, probabilidad_total

# Función para manejar el botón de generación
def generar_numeros():
    # Obtener los números generados y la probabilidad
    numeros_generados_personalizados, probabilidad_total = generate_custom_numbers()

    # Actualizar la etiqueta con los resultados y la probabilidad
    resultado_texto = f"Números generados: {numeros_generados_personalizados}\nProbabilidad total: {probabilidad_total:.2%}"
    etiqueta_resultado.config(text=resultado_texto, font=("Times", 8, "bold italic"))

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Números Quini 6")

# Crear botón para generar números
boton_generar = tk.Button(ventana, text="Generar Números", command=generar_numeros, pady=5, padx=10, bg="azure4", font=("Times", 12, "bold italic"))
boton_generar.pack(pady=20)

# Crear etiqueta para mostrar los resultados
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=20)

# Iniciar el bucle principal
ventana.geometry("400x300")
ventana.mainloop()
