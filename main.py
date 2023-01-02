import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class TemperatureConverter:
    @staticmethod
    def fahrenheitToCelsius(f, format = True):
        result = (f - 32) * 5 / 9
        if format:
            return f'{f} Fahrenheit = {result:.2f} Celsius'
        return result

    @staticmethod
    def celsiusToFahrenheit(c, format = True):
        result = c * 9 / 5 + 32
        if format:
            return f'{c} Celsius = {result:.2f} Fahrenheit'
        return result


class ConverterFrame(ttk.Frame):
    def __init__(self, container, unitFrom, converter):
        super().__init__(container)

        self.unitFrom = unitFrom
        self.converter = converter

        options = {'padx': 5, 'pady': 0}

        self.temperatureLabel = ttk.Label(self, text=self.unitFrom)
        self.temperatureLabel.grid(column = 0, row = 0, sticky = 'w', **options)

        self.temperature = tk.StringVar()
        self.temperatureEntry = ttk.Entry(self, textvariable = self.temperature)
        self.temperatureEntry.grid(column = 1, row = 0, sticky = 'w', **options)
        self.temperatureEntry.focus()

        self.convertButton = ttk.Button(self, text = 'Convert')
        self.convertButton.grid(column = 2, row = 0, sticky = 'w', **options)
        self.convertButton.configure(command = self.convert)

        self.resultLabel = ttk.Label(self)
        self.resultLabel.grid(row = 1, columnspan = 3, **options)

        self.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "nsew")

    def convert(self, event=None):
        try:
            inputValue = float(self.temperature.get())
            result = self.converter(inputValue)
            self.resultLabel.config(text = result)
        except ValueError as error:
            showerror(title = 'Error', message = error)

    def reset(self):
        self.temperatureEntry.delete(0, "end")
        self.resultLabel.text = ''


class ControlFrame(ttk.LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        self['text'] = 'Options'

        # radio buttons
        self.selectedValue = tk.IntVar()

        ttk.Radiobutton(
            self,
            text = 'F to C',
            value = 0,
            variable = self.selectedValue,
            command = self.changeFrame
        ).grid(column = 0, row = 0, padx = 5, pady = 5)

        ttk.Radiobutton(
            self,
            text = 'C to F',
            value = 1,
            variable = self.selectedValue,
            command = self.changeFrame
        ).grid(column = 1, row = 0, padx = 5, pady = 5)

        self.grid(column = 0, row = 1, padx = 5, pady = 5, sticky = 'ew')

        # initialize frames
        self.frames = {}
        self.frames[0] = ConverterFrame(
            container,
            'Fahrenheit',
            TemperatureConverter.fahrenheitToCelsius)
        self.frames[1] = ConverterFrame(
            container,
            'Celsius',
            TemperatureConverter.celsiusToFahrenheit)

        self.changeFrame()

    def changeFrame(self):
        frame = self.frames[self.selectedValue.get()]
        frame.reset()
        frame.tkraise()


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Temperature Converter')
        self.geometry('300x120+800+400')
        self.resizable(False, False)


if __name__ == "__main__":
    app = App()
    ControlFrame(app)
    app.mainloop()

