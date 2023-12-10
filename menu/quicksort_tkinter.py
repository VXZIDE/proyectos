import tkinter as tk

def quicksort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    izquierda = []
    derecha = []

    for i in range(1, len(lista)):
        izquierda.append(lista[i]) if lista[i] < pivote else derecha.append(lista[i])

    return quicksort(izquierda) + [pivote] + quicksort(derecha)

def ordenar_numeros():
    numeros = [int(x) for x in entry_numeros_ordenar.get().split(',')]
    lista_ordenada = quicksort(numeros)
    resultado.config(text=f'Lista Ordenada: {lista_ordenada}')
#configuracion de ventana(root)
ventana = tk.Tk()
ventana.geometry("400x200")
ventana.title("Quicksort GUI")
#instrucciones al entrar los numeros mostrados en panntalla
label_instrucciones = tk.Label(ventana, text="Ingrese números separados por coma:",font=("Times", 14, "bold italic"))
label_instrucciones.pack(pady=10)
#entrada de texto 
entry_numeros_ordenar = tk.Entry(ventana, width=60, font=("Arial", 10),bd=2)
entry_numeros_ordenar.pack(pady=10, ipady=5)
#button para ordenar los numeros
boton_ordenar = tk.Button(ventana, text="Ordenar", padx=10, pady=5, command=ordenar_numeros, bg="azure3", font=("Times", 14, "bold italic"))
boton_ordenar.pack(pady=10)
#mostrar el resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

ventana.mainloop()
