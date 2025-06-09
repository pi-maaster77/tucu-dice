import tkinter as tk
from juego import maingame as mn


# Colores y estilo
FONT_TITLE = ("Comic Sans MS", 24, "bold")
FONT_BUTTON = ("Comic Sans MS", 14)
FONT_FOOTER = ("Comic Sans MS", 10)

class Paleta: 
    tbg = "#000000"
    bg = "#2e3440"
    btn = "#88c0d0"
    text = "#eceff4"
paleta = Paleta()

def comandito ():
    paleta.bg="#6e0101"
    main.config(bg="#6e0101")
    tucu_label.config(bg="#6e0101")

def comandito2 ():
    paleta.bg="#000275"
    main.config(bg="#000275")
    tucu_label.config(bg="#000275")
def comandito3 ():
    paleta.bg="#007510"
    main.config(bg="#007510")
    tucu_label.config(bg="#007510")
class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Menú de Inicio")
        self.geometry("500x400")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):

        # Título
        title_label = tk.Label(self, text="__________ Tucu Dice __________", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text)
        title_label.pack(pady=20)

        # Botón Jugar
        play_button = tk.Button(self, text="Jugar", font=FONT_BUTTON, bg=paleta.btn, command=self.open_difficulty_menu)
        play_button.pack(pady=10)
        play_button.config(width=7)

        # Botón Tutorial
        play_button = tk.Button(self, text="Tutorial", font=FONT_BUTTON, bg=paleta.btn, command=self.open_tutorial_menu)
        play_button.pack(pady=10)
        play_button.config(width=7)

         # Botón Opcines
        play_button = tk.Button(self, text="Opciones", font=FONT_BUTTON, bg=paleta.btn, command=self.open_opciones_menu)
        play_button.pack(pady=10)
        play_button.config(width=7)

        # Botón Salir (corregido)
        quit_button = tk.Button(self, text="Salir", font=FONT_BUTTON, bg="#bf616a", command=self.quit)
        quit_button.pack(pady=10)
        quit_button.config(width=7)

        # Área para nombres de creadores
        footer_frame = tk.Frame(self, bg=paleta.tbg)
        footer_frame.pack(side="bottom", fill="x", pady=10)

        creators_label = tk.Label(footer_frame, text="_______________  Creado por: Dante Parola, Leonel Schonnevald y Yair Soley  _______________",
                                  font=FONT_FOOTER, bg=paleta.tbg, fg=paleta.text)
        creators_label.pack()
        

    def open_difficulty_menu(self):
        self.withdraw()  # Oculta la ventana principal
        DifficultyMenu(self)
    def open_tutorial_menu(self):
        self.withdraw()  # Oculta la ventana principal
        TutorialMenu(self)
    def open_opciones_menu(self):
        self.withdraw()  # Oculta la ventana principal
        OpcionesMenu(self)

class DifficultyMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Seleccionar Dificultad")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)

        # Etiqueta
        label = tk.Label(self, text="____________ Elige la dificultad ____________", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text)
        label.pack(pady=20)

        # Botones de dificultad
        easy_btn = tk.Button(self, text="Fácil", font=FONT_BUTTON, bg=paleta.btn, command=lambda: self.facil())
        normal_btn = tk.Button(self, text="Normal", font=FONT_BUTTON, bg=paleta.btn, command=lambda: self.normal())
        hard_btn = tk.Button(self, text="Difícil", font=FONT_BUTTON, bg=paleta.btn, command=lambda: self.dificil())

        easy_btn.config(width=7)
        normal_btn.config(width=7)
        hard_btn.config(width=7)

        easy_btn.pack(pady=5)
        normal_btn.pack(pady=5)
        hard_btn.pack(pady=5)

        # Botón volver al menú
        back_btn = tk.Button(self, text="Volver", font=FONT_BUTTON, bg="#a3be8c", command=self.back_to_menu)
        back_btn.pack(pady=20)
        back_btn.config(width=7)

        self.protocol("WM_DELETE_WINDOW", self.back_to_menu)

    def facil(self):
        self.withdraw()
        a = mn("facil", self.parent, paleta)

    def normal(self):
        self.withdraw()
        a = mn("normal", self.parent, paleta)

    def dificil(self):
        self.withdraw()
        a = mn("dificil", self.parent, paleta)

    def back_to_menu(self):
        self.withdraw()
        self.master.deiconify()  # Muestra de nuevo el menú principal

class TutorialMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Tutorial")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)

        # Etiqueta
        label = tk.Label(self, text="____________ Tutorial ____________", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text)
        label.pack(pady=20)

        label2 = tk.Label(self, text="Presiona los botones \n en la secuencia en \n la que se van iluminando", font=FONT_BUTTON, bg=paleta.bg, fg=paleta.text)
        label2.pack(pady=20)
        # Botón volver al menú
        back_btn = tk.Button(self, text="Volver", font=FONT_BUTTON, bg="#a3be8c", command=self.back_to_menu)
        back_btn.pack(pady=20)
        back_btn.config(width=7)
    
    def back_to_menu(self):
        self.withdraw()
        self.master.deiconify()  # Muestra de nuevo el menú principal

class OpcionesMenu(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Opciones")
        self.geometry("400x350")
        self.configure(bg=paleta.bg)
        self.resizable(False, False)

        # Título
        title_label = tk.Label(self, text="____________ Color del fondo ____________", font=FONT_TITLE, bg=paleta.tbg, fg=paleta.text)
        title_label.pack(pady=20)

        # Botón rojo
        play_button = tk.Button(self, text="Rojo", font=FONT_BUTTON, bg=paleta.btn, command=comandito)
        play_button.pack(pady=10)
        play_button.config(width=7)

        # Botón azul
        play_button = tk.Button(self, text="Azul", font=FONT_BUTTON, bg=paleta.btn, command=comandito2)
        play_button.pack(pady=10)
        play_button.config(width=7)

         # Botón verde
        play_button = tk.Button(self, text="Verde", font=FONT_BUTTON, bg=paleta.btn, command=comandito3)
        play_button.pack(pady=10)
        play_button.config(width=7)

         # Botón volver al menú
        back_btn = tk.Button(self, text="Volver", font=FONT_BUTTON, bg="#a3be8c", command=self.back_to_menu)
        back_btn.pack(pady=20)
        back_btn.config(width=7)
    
    def back_to_menu(self):
        self.withdraw()
        self.master.deiconify()  # Muestra de nuevo el menú principal



if __name__ == "__main__":
    main = MainMenu()
    imagen = tk.PhotoImage(file="tucu.png")
    tucu_label = tk.Label(main, image=imagen, bg=paleta.bg, width=160, height=160)
    tucu_label.place(x=320, y=140)
    tucu_label.lower()
    main.mainloop()

