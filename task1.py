import tkinter as tk
from tkinter import ttk, messagebox

def conversion():
    try:
        temp = float(entry_temp.get())
        unit = combo_unit.get()

        if unit == "Celsius":
            fahrenheit = (temp * 9/5) + 32
            kelvin = temp + 273.15
            result.set(f"{temp} °C = {fahrenheit:.2f} °F, {kelvin:.2f} K")

        elif unit == "Fahrenheit":
            celsius = (temp - 32) * 5/9
            kelvin = celsius + 273.15
            result.set(f"{temp} °F = {celsius:.2f} °C, {kelvin:.2f} K")

        elif unit == "Kelvin":
            celsius = temp - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result.set(f"{temp} K = {celsius:.2f} °C, {fahrenheit:.2f} °F")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Create the main window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("400x200")
root.resizable(False, False)

# Input field
tk.Label(root, text="USER Temperature:").pack(pady=5)
entry_temp = tk.Entry(root, width=20)
entry_temp.pack()

# Dropdown for unit selection
tk.Label(root, text="Unit:").pack(pady=5)
combo_unit = ttk.Combobox(root, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
combo_unit.current(0)
combo_unit.pack()

# Convert button
tk.Button(root, text="Convert", command=conversion).pack(pady=10)

# Output result
result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12)).pack(pady=10)

# Run the GUI loop
root.mainloop()
