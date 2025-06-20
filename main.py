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
        self.tucu_label:tk.Label
        self.create_widgets()

    def create_widgets(self):
        # Título
        tk.Label(self, text="Tucu Dice", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20, fill="x")

        # Botones principales
        self._crear_boton("Jugar", self.open_difficulty_menu)
        self._crear_boton("Tutorial", self.open_tutorial_menu)
        self._crear_boton("Opciones", self.open_opciones_menu)
        self._crear_boton("Records", self.open_record_menu)
        self._crear_boton("Salir", self.quit, bg="#bf616a")

        # Área para nombres de creadores
        footer_frame = tk.Frame(self, bg=paleta.tbg)
        footer_frame.pack(side="bottom", fill="x", pady=10)
        tk.Label(
            footer_frame,
            text="Creado por: Dante Parola, Leonel Schonnevald y Yair Soley",
            font=FONT_FOOTER, bg=paleta.tbg, fg=paleta.text
        ).pack(fill="x")

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
    
    def open_record_menu(self):
        self.withdraw()
        RecordMenu(self)

class DifficultyMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", parent.quit)
        self.title("Seleccionar Dificultad")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        self.create_widgets()
        self.protocol("WM_DELETE_WINDOW", self.back_to_menu)

    def create_widgets(self):
        tk.Label(self, text="Elige la dificultad", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20, fill="x")
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
        self.parent.deiconify()

class TutorialMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.protocol("WM_DELETE_WINDOW", parent.quit)
        self.parent = parent
        self.title("Tutorial")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Tutorial", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20, fill="x")
        tk.Label(self, text="Presiona los botones \n en la secuencia en \n la que se van iluminando", font=FONT_BUTTON, bg=paleta.bg, fg=paleta.text).pack(pady=20)
        self._crear_boton("Volver", self.back_to_menu, bg="#a3be8c", pady=20)

    def _crear_boton(self, texto, comando, bg=None, pady=10):
        color = bg if bg else paleta.btn
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=color, command=comando, width=7)
        btn.pack(pady=pady)

    def back_to_menu(self):
        self.withdraw()
        self.parent.deiconify()

class OpcionesMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.parent.quit)
        self.title("Opciones")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="Color del fondo", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20, fill="x")
        colores = [("Rojo", "#6e0101"), ("Azul", "#000275"), ("Verde", "#007510")]
        for texto, color in colores:
            self._crear_boton_color(texto, color)
        self._crear_boton("Volver", self.back_to_menu, bg="#a3be8c", pady=20)

    def _crear_boton_color(self, texto, color):
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=paleta.btn,
                        command=lambda: cambiar_color_fondo(color, self.parent, self.parent.tucu_label), width=7)
        btn.pack(pady=10)

    def _crear_boton(self, texto, comando, bg=None, pady=10):
        color = bg if bg else paleta.btn
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=color, command=comando, width=7)
        btn.pack(pady=pady)

    def back_to_menu(self):
        self.withdraw()
        self.parent.deiconify()

class RecordMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.protocol("WM_DELETE_WINDOW", self.parent.quit)
        self.title("Records")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        with open("records.txt", "r") as f:
            self.records = eval(f"[{f.read()}]")  # Aquí podrías mostrar los records en la interfaz
        self.create_widgets()
            
    def create_widgets(self):
        tk.Label(self, text="Records", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text).pack(pady=20, fill="x")

        tabla_frame = tk.Frame(self, bg=paleta.bg)
        tabla_frame.pack(pady=10)

        # Encabezados
        tk.Label(tabla_frame, text="Nombre", font=FONT_BUTTON, bg=paleta.tbg, fg=paleta.text, width=15, borderwidth=1, relief="solid").grid(row=0, column=0, padx=2, pady=2)
        tk.Label(tabla_frame, text="Puntos", font=FONT_BUTTON, bg=paleta.tbg, fg=paleta.text, width=10, borderwidth=1, relief="solid").grid(row=0, column=1, padx=2, pady=2)

        # Filas de records (máximo 10)
        for i, record in enumerate(self.records[:10]):
            tk.Label(tabla_frame, text=record["nombre"], font=FONT_BUTTON, bg=paleta.bg, fg=paleta.text, width=15, borderwidth=1, relief="solid").grid(row=i+1, column=0, padx=2, pady=2)
            tk.Label(tabla_frame, text=record["puntos"], font=FONT_BUTTON, bg=paleta.bg, fg=paleta.text, width=10, borderwidth=1, relief="solid").grid(row=i+1, column=1, padx=2, pady=2)

        self._crear_boton("Volver", self.back_to_menu, bg="#a3be8c", pady=20)

    def _crear_boton(self, texto, comando, bg=None, pady=10):
        color = bg if bg else paleta.btn
        btn = tk.Button(self, text=texto, font=FONT_BUTTON, bg=color, command=comando, width=7)
        btn.pack(pady=pady)

    def back_to_menu(self):
        self.withdraw()
        self.parent.deiconify()

if __name__ == "__main__":
    main = MainMenu()
    imagen = tk.PhotoImage(file="tucu.png")
    tucu_label = tk.Label(main, image=imagen, bg=paleta.bg, width=160, height=160)
    tucu_label.place(x=320, y=140)
    tucu_label.lower()
    main.tucu_label = tucu_label  # Referencia para cambiar color desde Opciones
    main.mainloop()