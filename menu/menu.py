import tkinter as tk
import subprocess

def abrir_quicksort():
    subprocess.Popen(['python', 'quicksort_tkinter.py'])

def abrir_quini():
    subprocess.Popen(['python', 'quini_tkinter.py'])

# Configuración de la ventana principal
ventana_menu = tk.Tk()
ventana_menu.title("Menú Principal")

# Botones para abrir los otros archivos
boton_quicksort = tk.Button(ventana_menu, text="Abrir QuickSort", command=abrir_quicksort, bg="sea green",font=("Times", 12, "bold italic"))
boton_quicksort.pack(pady=20)

boton_quini = tk.Button(ventana_menu, text="Abrir Quini", command=abrir_quini, bg="sea green",font=("Times", 12, "bold italic"))
boton_quini.pack(pady=20)

# Configurar la acción al cerrar la ventana principal
def cerrar_ventana():
    print("Cerrando la aplicación.")
    ventana_menu.destroy()

ventana_menu.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Iniciar el bucle principal
ventana_menu.geometry("400x300")
ventana_menu.mainloop()
