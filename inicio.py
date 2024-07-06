from tkinter import *
from tkinter import messagebox
import tkinter as tk


class autentificacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Inicio")
        self.geometry("600x400")
        self.resizable(True, True)

        frame = Frame(self)
        frame.pack(expand=True, fill="both")
        frame.config(width=600, height=400)

        label_inicio_sesion = Label(frame, text="Inicio de sesion")
        label_usuario = Label(frame, text="Usuario:")
        label_contraseña = Label(frame, text="Contraseña")

        self.caja_usuario = Entry(frame)
        self.caja_contraseña = Entry(frame, show="*")

        button_login = Button(frame, text="Ingresar", command=self.verificacion)

        label_inicio_sesion.place(x=230, y=30)
        label_usuario.place(x=200, y=80)
        label_contraseña.place(x=200, y=120)
        self.caja_usuario.place(x=200, y=50)
        self.caja_contraseña.place(x=200, y=160)
        button_login.place(x=300, y=200)
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
        ventana_principal.mainloop()
class VentanaPrincipal(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Ventana Principal")
        self.geometry("600x400")
        self.parent = parent

        label = Label(self, text="Bienvenido a la Ventana Principal")
        label.pack(pady=20)

        boton = Button(self, text="Logout", command=self.logout)
        boton.pack(pady=20)

    def logout(self):
        self.destroy()
        self.parent.deiconify()

if __name__ == "__main__":
    app = autentificacion()
    app.mainloop()



