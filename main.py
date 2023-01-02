import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

class TemperatureConverter:
    @staticmethod
    def fahrenheitToCelsius(f):
        return (f - 32) * 5 / 9

class ConverterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        options = {'padx': 5, 'pady': 5}

        self.temperatureLabel = ttk.Label(self, text="Fahrenheit")
        self.temperatureLabel.grid(column = 0, row = 0, sticky = tk.W, **options)

        self.temperature = tk.StringVar()
        self.temperatureEntry = ttk.Entry(self, textvariable = self.temperature)
        self.temperatureEntry.grid(column = 1, row = 0, **options)
        self.temperatureEntry.focus()

        self.convertButton = ttk.Button(self, text = "Converter")
        self.convertButton['command'] = self.convert
        self.convertButton.grid(column = 2, row = 0, sticky= tk.W, **options)

        self.resultLabel = ttk.Label(self)
        self.resultLabel.grid(row = 1, columnspan = 3, **options)

        self.grid(padx = 10, pady = 10, sticky = tk.NSEW)

    def convert(self):
        try:
            f = float(self.temperature.get())
            c = TemperatureConverter.fahrenheitToCelsius(f)
            result = f"{f} Fahrenheit = {c:.2f} Celsius"
            self.resultLabel.config(text = result)
        except ValueError as error:
            showerror(title = "Error", message = error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Conversor de temperaturas")
        self.geometry("300x70+750+350")
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    ConverterFrame(app)
    app.mainloop()