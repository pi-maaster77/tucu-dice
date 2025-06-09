import tkinter as tk
from random import choice

# Mapa de colores
tablaColores = {
    "#AA0000" : "#FF0000",
    "#000066" : "#4444FF",
    "#008800" : "#33FF33",
    "#AAAA00" : "#FFFF00",
    "#00AAAA" : "#00FFFF",
    "#AA00AA" : "#FF00FF"
}

# Paleta de colores
bg = "#2e3440"

FONT_TITLE = ("Comic Sans MS", 24, "bold")
FONT_BUTTON = ("Comic Sans MS", 14)
FONT_FOOTER = ("Comic Sans MS", 10)

class Posicion:
    def __init__(self, row, column):
        self.row = row
        self.column = column
tabla_dificultad = {
    "facil" : [Posicion(0, 0), Posicion(1, 1), Posicion(0, 2)],
    "normal" : [Posicion(0, 1), Posicion(1, 0), Posicion(1, 3), Posicion(2, 1)],
    "dificil" : [Posicion(0, 1), Posicion(0, 2), Posicion(1, 0), Posicion(1, 3), Posicion(2, 1), Posicion(2, 2)]
}
class maingame(tk.Toplevel):

    def __init__(self, dificultad, parent, paleta):
        super().__init__(parent)
        self.geometry("400x350")
        self.api = API(dificultad, self, paleta)
        self.config(bg=paleta.bg)
        self.api.bucle_de_juego()
        imagen = tk.PhotoImage(file="tucu.png")
        tucu_label2 = tk.Label(self, image=imagen, bg=paleta.bg, width=160, height=160)
        tucu_label2.place(relx=1, rely=1, anchor="se")

        self.protocol("WM_DELETE_WINDOW", self.back_to_menu)
    def back_to_menu(self):
        self.destroy()
        self.master.deiconify()  # Muestra de nuevo el menú principal

class Boton(tk.Button):
    def __init__(self, colorHEX, api, ventana):
        self.ventana = ventana 
        super().__init__(self.ventana)
        self.config(width=4, height=2, borderwidth=0)
        self.colorHEX = colorHEX
        self.api = api
        self.config(bg=self.colorHEX, command=lambda: api.funcionActual(self))

    def iluminar(self):
        print(f"Iluminando: {self.colorHEX}")
        self.config(bg=tablaColores[self.colorHEX])
        # Convertir tiempo a entero
        self.ventana.after(int(self.api.tiempo * 1000), lambda: self.config(bg=self.colorHEX))  # Convertir a entero en milisegundos
    def posicionar(self, posicion:Posicion):
        self.grid(row=posicion.row, column=posicion.column, padx=2, pady=2)

class API:
    tiempo = 1.5  # Tiempo entre botones al ser iluminados
    secuencia: list[Boton] = []
    numeroActual = 0
    ESCALADEDIFICULTAD = 0.9
    escalar = True
    mostrando = True
    def __init__(self, dificultad, ventana, paleta):
        self.tiempo = 1.5  # Tiempo entre botones al ser iluminados
        self.secuencia: list[Boton] = []
        self.numeroActual = 0
        self.ESCALADEDIFICULTAD = 0.9
        self.escalar = True
        mostrando = True
        posicionBotones= tabla_dificultad[dificultad]
        self.ventana = ventana
        marco = tk.Frame(ventana)
        marco.config(bg=paleta.bg)
        marco.pack(expand=True)
        colores = list(tablaColores.keys())[:len(posicionBotones)]
        self.botones = [Boton(color, self, marco) for color in colores]
        for boton , posicion in zip(self.botones, posicionBotones):
            boton.posicionar(posicion)
        

    def bucle_de_juego(self):

        self.mostrando = True
            
        # Agregar un nuevo color a la secuencia de manera ordenada
        self.secuencia.append(choice(self.botones))

        for boton in self.botones:
            boton.config(state="disabled")

        # Iluminar los botones en la secuencia con retraso entre ellos
        for i, boton in enumerate(self.secuencia):
            self.ventana.after(int(i * 1.2 * self.tiempo * 1000), boton.iluminar)  # Convertir el tiempo total en milisegundos

        # Rehabilitar los botones después de que se muestre la secuencia
        total_delay = int(len(self.secuencia)-1 * self.tiempo * 1200)  # El tiempo de espera total hasta la última iluminación
        self.ventana.after(total_delay, lambda: [b.config(state="normal") for b in self.botones])
        self.mostrando = False


    def funcionActual(self, boton: Boton):
        if self.mostrando:
            return
        else:

            print(f"{boton.colorHEX} Apretado")

            # Si el botón presionado es el correcto, incrementar el número de la secuencia
            if self.secuencia[self.numeroActual].colorHEX == boton.colorHEX:
                self.numeroActual += 1
                print(f"Secuencia correcta. Avanzando: {self.numeroActual}/{len(self.secuencia)}")

                # Si el jugador completa la secuencia, pasar a la siguiente ronda
                if self.numeroActual == len(self.secuencia):
                    print(f"Nivel de dificultad: {self.tiempo}")
                    self.numeroActual = 0
                    if self.escalar:
                        self.escalar = self.tiempo > 0.2
                        self.tiempo *= self.ESCALADEDIFICULTAD  # Disminuir el tiempo entre luces
                    self.ventana.after(int(self.tiempo * 1200), self.bucle_de_juego)  # Llamamos al siguiente nivel
            else:
                self.fin()
                self.ventana.after(2000, self.bucle_de_juego)
    def fin(self):
        print("Juego terminado. Reiniciando...")
        self.secuencia = []  # Reiniciar la secuencia
        self.numeroActual = 0  # Reiniciar el contador
        self.tiempo = API.tiempo
        self.escalar = True
        