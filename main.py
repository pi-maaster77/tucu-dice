import tkinter as tk
from juego import MainGame as mn

# Estilos y paleta de colores
FONT_TITLE = ("Comic Sans MS", 24, "bold")
FONT_BUTTON = ("Comic Sans MS", 14)
FONT_FOOTER = ("Comic Sans MS", 10)

class Paleta:
    tbg = "#000000"
    bg = "#2e3440"
    btn = "#88c0d0"
    text = "#eceff4"

paleta = Paleta()

def cambiar_color_fondo(color, main, tucu_label):
    paleta.bg = color
    main.config(bg=color)
    tucu_label.config(bg=color)

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú de Inicio")
        self.geometry("500x400")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        self.tucu_label = None
        self.create_widgets()

    def create_widgets(self):
        # Título
        tk.Label(self, text="__________ Tucu Dice __________", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20)

        # Botones principales
        self._crear_boton("Jugar", self.open_difficulty_menu)
        self._crear_boton("Tutorial", self.open_tutorial_menu)
        self._crear_boton("Opciones", self.open_opciones_menu)
        self._crear_boton("Salir", self.quit, bg="#bf616a")

        # Área para nombres de creadores
        footer_frame = tk.Frame(self, bg=paleta.tbg)
        footer_frame.pack(side="bottom", fill="x", pady=10)
        tk.Label(
            footer_frame,
            text="_______________  Creado por: Dante Parola, Leonel Schonnevald y Yair Soley  _______________",
            font=FONT_FOOTER, bg=paleta.tbg, fg=paleta.text
        ).pack()

    def _crear_boton(self, texto, comando, bg=None):
        color = bg if bg else paleta.btn
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=color, command=comando, width=7)
        btn.pack(pady=10)

    def open_difficulty_menu(self):
        self.withdraw()
        DifficultyMenu(self)

    def open_tutorial_menu(self):
        self.withdraw()
        TutorialMenu(self)

    def open_opciones_menu(self):
        self.withdraw()
        OpcionesMenu(self)

class DifficultyMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Seleccionar Dificultad")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.back_to_menu)

    def create_widgets(self):
        tk.Label(self, text="____________ Elige la dificultad ____________", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20)
        self._crear_boton("Fácil", lambda: self.seleccionar_dificultad("facil"))
        self._crear_boton("Normal", lambda: self.seleccionar_dificultad("normal"))
        self._crear_boton("Difícil", lambda: self.seleccionar_dificultad("dificil"))
        self._crear_boton("Volver", self.back_to_menu, bg="#a3be8c", pady=20)

    def _crear_boton(self, texto, comando, bg=None, pady=5):
        color = bg if bg else paleta.btn
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=color, command=comando, width=7)
        btn.pack(pady=pady)

    def seleccionar_dificultad(self, dificultad):
        self.withdraw()
        mn(dificultad, self.parent, paleta)

    def back_to_menu(self):
        self.withdraw()
        self.master.deiconify()

class TutorialMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Tutorial")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="____________ Tutorial ____________", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20)
        tk.Label(self, text="Presiona los botones \n en la secuencia en \n la que se van iluminando", font=FONT_BUTTON, bg=paleta.bg, fg=paleta.text).pack(pady=20)
        self._crear_boton("Volver", self.back_to_menu, bg="#a3be8c", pady=20)

    def _crear_boton(self, texto, comando, bg=None, pady=10):
        color = bg if bg else paleta.btn
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=color, command=comando, width=7)
        btn.pack(pady=pady)

    def back_to_menu(self):
        self.withdraw()
        self.master.deiconify()

class OpcionesMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Opciones")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="____________ Color del fondo ____________", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20)
        colores = [("Rojo", "#6e0101"), ("Azul", "#000275"), ("Verde", "#007510")]
        for texto, color in colores:
            self._crear_boton_color(texto, color)
        self._crear_boton("Volver", self.back_to_menu, bg="#a3be8c", pady=20)

    def _crear_boton_color(self, texto, color):
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=paleta.btn,
                        command=lambda: cambiar_color_fondo(color, self.master, self.master.tucu_label), width=7)
        btn.pack(pady=10)

    def _crear_boton(self, texto, comando, bg=None, pady=10):
        color = bg if bg else paleta.btn
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=color, command=comando, width=7)
        btn.pack(pady=pady)

    def back_to_menu(self):
        self.withdraw()
        self.master.deiconify()

if __name__ == "__main__":
    main = MainMenu()
    imagen = tk.PhotoImage(file="tucu.png")
    tucu_label = tk.Label(main, image=imagen, bg=paleta.bg, width=160, height=160)
    tucu_label.place(x=320, y=140)
    tucu_label.lower()
    main.tucu_label = tucu_label  # Referencia para cambiar color desde Opciones
    main.mainloop()