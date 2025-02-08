import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

# Configuración de la ventana principal
class PerceptronGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Perceptrón")

        # Inicializa variables: puntos y pesos
        self.points = []
        self.weights = None

        # Crear el gráfico (Plano)
        self.figure, self.ax = plt.subplots()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)

        # Configurar la cuadrícula y los ejes
        self.ax.set_xticks(np.arange(-10, 11, 1))
        self.ax.set_yticks(np.arange(-10, 11, 1))
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)

        # Agregar gráfico a la interfaz
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)

        # Clic del ratón para agregar puntos
        self.canvas.mpl_connect('button_press_event', self.add_point)

        # Crear entrada de texto para pesos y bias
        entry_frame = tk.Frame(self)
        entry_frame.pack()

        tk.Label(entry_frame, text="Peso w1:").grid(row=0, column=0)
        self.w1_entry = tk.Entry(entry_frame)
        self.w1_entry.grid(row=0, column=1)

        tk.Label(entry_frame, text="Peso w2:").grid(row=1, column=0)
        self.w2_entry = tk.Entry(entry_frame)  
        self.w2_entry.grid(row=1, column=1)

        tk.Label(entry_frame, text="Bias w0:").grid(row=2, column=0)
        self.bias_entry = tk.Entry(entry_frame)
        self.bias_entry.grid(row=2, column=1)

        # Botones de control
        control_frame = tk.Frame(self)
        control_frame.pack()

        tk.Button(control_frame, text="Clasificar Puntos",
                  command=self.classify_points).pack(side=tk.LEFT)

        # Manejo de cierre
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    # Marcar puntos en el hiperplano
    def add_point(self, event):
        if event.inaxes:
            x, y = round(event.xdata), round(event.ydata)
            self.points.append((x, y))
            self.ax.plot(x, y, 'ko', markersize=12)
            self.canvas.draw()

    # Clasificar puntos y dibujar hiperplano
    def classify_points(self):
        try:
            w1 = float(self.w1_entry.get())
            w2 = float(self.w2_entry.get())
            bias = float(self.bias_entry.get())
        except ValueError:
            messagebox.showwarning("Error para continuar", "Ingresa los valores (Números) para los pesos y el bias.")
            return

        self.weights = (w1, w2, bias)

        # Redibujar puntos y clasificar
        self.ax.clear()
        self.ax.set_xlim(-10, 10)
        self.ax.set_ylim(-10, 10)
        self.ax.set_xticks(np.arange(-10, 11, 1))
        self.ax.set_yticks(np.arange(-10, 11, 1))
        self.ax.grid(True, which='both', linestyle='--', linewidth=0.5)
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)

        # Rojo y azul para las dos clases
        for x, y in self.points:
            result = w1 * x + w2 * y + bias
            color = 'bo' if result >= 0 else 'ro'
            self.ax.plot(x, y, color, markersize=12)
