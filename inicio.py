import customtkinter
from customtkinter import *
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkvideo import tkvideo

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class Autentificacion(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Inicio")
        self.geometry("800x600")
        self.resizable(False, False)  # No permitir redimensionar la ventana

        self.configure(bg="black")

        video_label = Label(self, bg="black")
        video_label.place(relx=0.5, rely=0.5, anchor=CENTER, width=800, height=600)
        video_path = "video/ASTARTES Teaser.mp4"  # Ruta al video dentro de la carpeta media
        player = tkvideo(video_path, video_label, loop=1, size=(800, 600))
        player.play()

        frame = CTkFrame(self, width=400, height=300, corner_radius=10, fg_color=("black", "gray10"))
        frame.place(in_=video_label, relx=0.5, rely=0.5, anchor=CENTER)

        frame.configure(border_color="blue", border_width=2)

        label_inicio_sesion = CTkLabel(frame, text="Inicio de sesión", text_color="red", font=('sans serif', 22))
        label_usuario = CTkLabel(frame, text="Usuario:", text_color="white", font=('sans serif', 16))
        label_contraseña = CTkLabel(frame, text="Contraseña", text_color="white", font=('sans serif', 16))

        self.caja_usuario = CTkEntry(frame, placeholder_text="Nombre de usuario...", fg_color="black", text_color="white")
        self.caja_contraseña = CTkEntry(frame, show="*", placeholder_text="Contraseña...", fg_color="black", text_color="white")

        button_login = CTkButton(frame, text="Ingresar", width=20, command=self.verificacion, fg_color="blue", hover_color="darkblue")

        label_inicio_sesion.place(relx=0.5, y=30, anchor=CENTER)
        label_usuario.place(relx=0.25, y=80, anchor=CENTER)
        self.caja_usuario.place(relx=0.75, y=80, anchor=CENTER)
        label_contraseña.place(relx=0.25, y=140, anchor=CENTER)
        self.caja_contraseña.place(relx=0.75, y=140, anchor=CENTER)
        button_login.place(relx=0.5, y=200, anchor=CENTER)

    def verificacion(self):
        usuario = self.caja_usuario.get()
        contraseña = self.caja_contraseña.get()

        if usuario == "Sarzel" and contraseña == "uaauaañ123":
            self.abrir_ventana_principal()
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrecta")

    def abrir_ventana_principal(self):
        self.withdraw()
        ventana_principal = VentanaPrincipal(self)


class VentanaPrincipal(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ventana Principal")
        self.geometry("800x600")
        self.parent = parent

        label = CTkLabel(self, text="Bienvenido a la Ventana Principal", text_color="yellow", font=('sans serif', 22))
        label.pack(pady=20)

        boton = CTkButton(self, text="Volver al inicio de sesion", command=self.logout, fg_color="red", hover_color="darkred")
        boton.pack(pady=20)

    def logout(self):
        self.destroy()
        self.parent.deiconify()


if __name__ == "__main__":
    app = Autentificacion()
    app.mainloop()
