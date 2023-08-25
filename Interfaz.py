import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Interface:
    def __init__(self, root):
        self.root = root
        self.root.title("Imágenes")
        self.root.geometry("500x500")  # Dimensiones de la ventana

        self.claves = []
        self.descripciones = []
        self.imagenes1 = []
        self.imagenes2 = []

        self.create_widgets()

    def create_widgets(self):
        # Crear un estilo personalizado para los widgets
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12))
        style.configure("TEntry", font=("Helvetica", 12))

        self.label_clave = ttk.Label(self.root, text="Clave:")
        self.entry_clave = ttk.Entry(self.root)

        self.label_descripcion = ttk.Label(self.root, text="Descripción:")
        self.entry_descripcion = ttk.Entry(self.root)

        self.button_guardar = ttk.Button(self.root, text="Guardar", command=self.guardar)
        self.button_mostrar = ttk.Button(self.root, text="Mostrar", command=self.mostrar)

        self.label_imagen1 = ttk.Label(self.root, text="Imagen 1:")
        self.label_imagen2 = ttk.Label(self.root, text="Imagen 2:")

        self.image_label1 = ttk.Label(self.root)
        self.image_label2 = ttk.Label(self.root)

        # Disposición en cuadrícula
        self.label_clave.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.entry_clave.grid(row=0, column=1, padx=10, pady=10)
        self.label_descripcion.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.entry_descripcion.grid(row=1, column=1, padx=10, pady=10)
        self.button_guardar.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        self.button_mostrar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.label_imagen1.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        self.image_label1.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        self.label_imagen2.grid(row=6, column=0, columnspan=2, padx=10, pady=10)
        self.image_label2.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def guardar(self):
        clave = self.entry_clave.get()
        descripcion = self.entry_descripcion.get()
        self.claves.append(clave)
        self.descripciones.append(descripcion)

        # Aquí deberías agregar la lógica para guardar las imágenes en las listas imagenes1 y imagenes2

        self.entry_clave.delete(0, tk.END)
        self.entry_descripcion.delete(0, tk.END)

    def mostrar(self):
        # Aquí deberías agregar la lógica para mostrar las imágenes almacenadas en las listas imagenes1 y imagenes2

        # Por ahora, simplemente muestra un mensaje
        for clave, descripcion in zip(self.claves, self.descripciones):
            print(f"Clave: {clave}, Descripción: {descripcion}")


if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()