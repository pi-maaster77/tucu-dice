import tkinter as tk
from random import choice

# Mapa de colores
TABLA_COLORES = {
    "#AA0000": "#FF0000",
    "#000066": "#4444FF",
    "#008800": "#33FF33",
    "#AAAA00": "#FFFF00",
    "#00AAAA": "#00FFFF",
    "#AA00AA": "#FF00FF"
}

# Paleta de colores
BG_COLOR = "#2e3440"

FONT_TITLE = ("Comic Sans MS", 24, "bold")
FONT_BUTTON = ("Comic Sans MS", 14)
FONT_FOOTER = ("Comic Sans MS", 10)

class Posicion:
    def __init__(self, row, column):
        self.row = row
        self.column = column

TABLA_DIFICULTAD = {
    "facil":   [Posicion(0, 0), Posicion(1, 1), Posicion(0, 2)],
    "normal":  [Posicion(0, 1), Posicion(1, 0), Posicion(1, 3), Posicion(2, 1)],
    "dificil": [Posicion(0, 1), Posicion(0, 2), Posicion(1, 0), Posicion(1, 3), Posicion(2, 1), Posicion(2, 2)]
}

class MainGame(tk.Toplevel):
    def __init__(self, dificultad, parent, paleta):
        super().__init__(parent)
        self.geometry("400x350")
        self.config(bg=paleta.bg)
        self.api = GameAPI(dificultad, self, paleta)
        self.api.iniciar_juego()
        imagen = tk.PhotoImage(file="tucu.png")
        tucu_label = tk.Label(self, image=imagen, bg=paleta.bg, width=160, height=160)
        tucu_label.place(relx=1, rely=1, anchor="se")
        self.tucu_label = tucu_label
        self.imagen = imagen  # Mantener referencia para evitar garbage collection
        self.protocol("WM_DELETE_WINDOW", self.back_to_menu)

    def back_to_menu(self):
        self.destroy()
        self.master.deiconify()

class BotonJuego(tk.Button):
    def __init__(self, color_hex, api, parent):
        super().__init__(parent, width=4, height=2, borderwidth=0, bg=color_hex)
        self.color_hex = color_hex
        self.api = api
        self.config(command=lambda: api.manejar_click(self))

    def iluminar(self, tiempo):
        self.config(bg=TABLA_COLORES[self.color_hex])
        self.after(int(tiempo * 1000), lambda: self.config(bg=self.color_hex))

    def posicionar(self, posicion: Posicion):
        self.grid(row=posicion.row, column=posicion.column, padx=2, pady=2)

class GameAPI:
    TIEMPO_INICIAL = 1.5
    ESCALA_DIFICULTAD = 0.9
    TIEMPO_MINIMO = 0.2

    def __init__(self, dificultad, ventana, paleta):
        self.tiempo = self.TIEMPO_INICIAL
        self.secuencia = []
        self.indice_actual = 0
        self.escalar = True
        self.mostrando = False
        self.ventana = ventana
        self.paleta = paleta

        posiciones = TABLA_DIFICULTAD[dificultad]
        colores = list(TABLA_COLORES.keys())[:len(posiciones)]
        self.marco = tk.Frame(ventana, bg=paleta.bg)
        self.marco.pack(expand=True)
        self.botones = [BotonJuego(color, self, self.marco) for color in colores]
        for boton, posicion in zip(self.botones, posiciones):
            boton.posicionar(posicion)

    def iniciar_juego(self):
        self.nueva_ronda()

    def nueva_ronda(self):
        self.mostrando = True
        self.secuencia.append(choice(self.botones))
        self._deshabilitar_botones()
        for i, boton in enumerate(self.secuencia):
            self.ventana.after(int(i * 1.2 * self.tiempo * 1000), lambda b=boton: b.iluminar(self.tiempo))
        total_delay = int(len(self.secuencia) * 1.2 * self.tiempo * 1000)
        # Solo habilita los botones después de mostrar la secuencia
        self.ventana.after(total_delay, self._habilitar_botones)
        self.ventana.after(total_delay, lambda: setattr(self, 'mostrando', False))
        self.indice_actual = 0

    def manejar_click(self, boton: BotonJuego):
        if self.mostrando:
            return
        if self.secuencia[self.indice_actual].color_hex == boton.color_hex:
            self.indice_actual += 1
            if self.indice_actual == len(self.secuencia):
                if self.escalar and self.tiempo > self.TIEMPO_MINIMO:
                    self.tiempo *= self.ESCALA_DIFICULTAD
                self.ventana.after(int(self.tiempo * 1200), self.nueva_ronda)
        else:
            self.reiniciar_juego()

    def _deshabilitar_botones(self):
        for boton in self.botones:
            boton.config(state="disabled")

    def _habilitar_botones(self):
        for boton in self.botones:
            boton.config(state="normal")

    def reiniciar_juego(self):
        self.secuencia.clear()
        self.indice_actual = 0
        self.tiempo = self.TIEMPO_INICIAL
        self.escalar = True
        self.ventana.after(2000, self.nueva_ronda)