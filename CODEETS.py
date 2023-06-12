import tkinter as tk
from tkinter import messagebox


def calcular_probabilidad_ets():
    syphilis = syphilis_var.get()
    gonorrhea = gonorrhea_var.get()
    hiv = hiv_var.get()
    hpv = hpv_var.get()
    num_personas = int(num_personas_entry.get())
    genero = genero_var.get()

    # Cálculo de probabilidad (valores ficticios)
    prob_syphilis_masculino = 0.04
    prob_syphilis_femenino = 0.022
    prob_gonorrhea_masculino = 0.019
    prob_gonorrhea_femenino = 0.003
    prob_hiv_masculino = 0.045
    prob_hiv_femenino = 0.022
    prob_hpv_masculino = 16
    prob_hpv_femenino = 16

    # Calcular la probabilidad según enfermedades y género
    probabilidad_syphilis = prob_syphilis_masculino * num_personas if genero == "Masculino" else prob_syphilis_femenino * num_personas
    probabilidad_gonorrhea = prob_gonorrhea_masculino * num_personas if genero == "Masculino" else prob_gonorrhea_femenino * num_personas
    probabilidad_hiv = prob_hiv_masculino * num_personas if genero == "Masculino" else prob_hiv_femenino * num_personas
    probabilidad_hpv = prob_hpv_masculino * num_personas if genero == "Masculino" else prob_hpv_femenino * num_personas

    # Mostrar la probabilidad en un cuadro de mensaje
    mensaje = ""
    probabilidad_total = round(probabilidad_syphilis + probabilidad_gonorrhea + probabilidad_hiv + probabilidad_hpv, 6)
    probabilidad_syphilis = round(probabilidad_syphilis, 6)
    probabilidad_gonorrhea = round(probabilidad_gonorrhea, 6)
    probabilidad_hiv = round(probabilidad_hiv, 6)
    probabilidad_hpv = round(probabilidad_hpv, 6)
    
    mensaje += "La probabilidad de estar contagiado de alguna ETS es: " + str(probabilidad_total) + "%" + "\n"
    mensaje += "Probabilidad por enfermedad:\n"
    mensaje += "Sífilis: " + str(probabilidad_syphilis) + "%" + "\n"
    mensaje += "Gonorrea: " + str(probabilidad_gonorrhea) + "%" + "\n"
    mensaje += "VIH: " + str(probabilidad_hiv) + "%" + "\n"
    mensaje += "Papiloma humano: " + str(probabilidad_hpv) + "%" + "\n"

    messagebox.showinfo("Probabilidad ETS", mensaje)


# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora de Probabilidad de ETS Chile")

# Etiqueta y campo de entrada para el número de personas
num_personas_label = tk.Label(window, text="Cantidad de personas con las que has tenido relaciones sexuales:")
num_personas_label.pack()
num_personas_entry = tk.Entry(window)
num_personas_entry.pack()

# Opciones para las enfermedades
syphilis_label = tk.Label(window, text="Sífilis:")
syphilis_label.pack()
syphilis_var = tk.IntVar()
syphilis_checkbox = tk.Checkbutton(window, text="dentro del cálculo", variable=syphilis_var)
syphilis_checkbox.pack()

gonorrhea_label = tk.Label(window, text="Gonorrea:")
gonorrhea_label.pack()
gonorrhea_var = tk.IntVar()
gonorrhea_checkbox = tk.Checkbutton(window, text="dentro del cálculo", variable=gonorrhea_var)
gonorrhea_checkbox.pack()

hiv_label = tk.Label(window, text="VIH:")
hiv_label.pack()
hiv_var = tk.IntVar()
hiv_checkbox = tk.Checkbutton(window, text="dentro del cálculo", variable=hiv_var)
hiv_checkbox.pack()

hpv_label = tk.Label(window, text="Papiloma humano:")
hpv_label.pack()
hpv_var = tk.IntVar()
hpv_checkbox = tk.Checkbutton(window, text="dentro del cálculo", variable=hpv_var)
hpv_checkbox.pack()

# Opciones para el género
genero_label = tk.Label(window, text="Género de las parejas sexuales:")
genero_label.pack()
genero_var = tk.StringVar(window)
genero_var.set("Masculino")
genero_option = tk.OptionMenu(window, genero_var, "Masculino", "Femenino")
genero_option.pack()

# Botón para calcular la probabilidad
calcular_button = tk.Button(window, text="Calcular Probabilidad", command=calcular_probabilidad_ets)
calcular_button.pack()

# Ejecutar la ventana principal
window.mainloop()
