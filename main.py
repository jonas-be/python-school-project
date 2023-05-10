import tkinter as tk

# Conversion Map
conversion_factors = {
    "byte": 1,
    "kilobyte": 1000,
    "Kili": 1024,
    "megabyte": 1000**2,
    "Mibi": 1024**2,
    "gigabyte": 1000**3,
    "Gigi": 1024 ** 3
}

def convert_units(value, from_unit, to_unit):
    bytes = value * conversion_factors[from_unit]
    result = bytes / conversion_factors[to_unit]
    return round(result, 2)

# Create a Tkinter window
window = tk.Tk()
window.title("Unit Converter")

# Create the input field
value_label = tk.Label(window, text="Enter the value:")
value_label.pack()
value_entry = tk.Entry(window)
value_entry.pack()

# Create a label for the input field
from_unit_label = tk.Label(window, text="From:")
from_unit_label.pack()

# Create a dropdown menu for the input unit
from_unit_var = tk.StringVar()
from_unit_var.set("byte")  # Set the default value to byte
from_unit_menu = tk.OptionMenu(window, from_unit_var, *conversion_factors.keys())
from_unit_menu.pack()

# Create a label for the output unit
to_unit_label = tk.Label(window, text="To:")
to_unit_label.pack()

# Create a dropdown menu for the output unit
to_unit_var = tk.StringVar()
to_unit_var.set("byte")  # Set the default value to byte
to_unit_menu = tk.OptionMenu(window, to_unit_var, *conversion_factors.keys())
to_unit_menu.pack()

# Create a label for the output value
result_label = tk.Label(window, text="Result:")
result_label.pack()

# Create a label to display the output value
result_display = tk.Label(window, text="")
result_display.pack()

# Define a function to convert the value and update the display label
def convert_units_and_update_display():
    try:
        value = float(value_entry.get())
        from_unit = from_unit_var.get()
        to_unit = to_unit_var.get()
        result = convert_units(value, from_unit, to_unit)
        result_display.config(text=result)
    except ValueError:
        result_display.config(text="Invalid input")

# Create a button to initiate the conversion
convert_button = tk.Button(window, text="Convert", command=convert_units_and_update_display)
convert_button.pack()

# Run the Tkinter event loop
window.mainloop()