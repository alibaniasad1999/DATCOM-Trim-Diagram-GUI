import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title("DATCOM-GUI")
root.geometry("900x500")
tabControl = ttk.Notebook(root)

control_cards = ttk.Frame(tabControl)

tabControl.add(control_cards,
			   text='Control Cards')
tabControl.pack(expand=1, fill="both")
tk.Label(control_cards,
		 text="Digital DATCOM Graphical User Interface",
		 font=('Arial', 25)).grid(column=1, row=0, sticky=tk.EW)
# Control Cards frames
# Dimensions unit

Dimensions = tk.Frame(control_cards,
				highlightbackground="black",
				highlightthickness=1)
Dimensions.grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
ttk.Label(Dimensions, text="Dimensions Unit:").grid(column=0, row=0, columnspan=2, sticky=tk.N)
dim_unit_var = tk.IntVar()
dim_unit_var.set(1)
tk.Radiobutton(Dimensions, text="Imperial", padx=20, variable=dim_unit_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(Dimensions, text="Metric", padx=20, variable=dim_unit_var, value=2).grid(column=0, row=2, sticky=tk.W)

# Derivations unit
Derivations = tk.Frame(control_cards,
				highlightbackground="black",
				highlightthickness=1)
Derivations.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)
ttk.Label(Derivations, text="Derivations Unit:").grid(column=0, row=0, columnspan=2, sticky=tk.N)
der_unit_var = tk.IntVar()
der_unit_var.set(1)
tk.Radiobutton(Derivations, text="Degree", padx=20, variable=der_unit_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(Derivations, text="Radian", padx=20, variable=der_unit_var, value=2).grid(column=0, row=2, sticky=tk.W)

# Other Options
Other_options = tk.Frame(control_cards,
				highlightbackground="black",
				highlightthickness=1)
Other_options.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=tk.W)
dyn_der_var = tk.IntVar()
dyn_der_var.set(1)
part_var = tk.IntVar()
part_var.set(0)
build_var = tk.IntVar()
build_var.set(0)
tk.Checkbutton(Other_options, text="Dynamic Derivation(Advice: make it on)",
			   variable=dyn_der_var).grid(column=0, row=0, sticky=tk.W)
tk.Checkbutton(Other_options, text="Part Module",
			   variable=part_var).grid(column=0, row=1, sticky=tk.W)
tk.Checkbutton(Other_options, text="Build Module",
			   variable=build_var).grid(column=0, row=2, sticky=tk.W)

# Flight Conditions frames
flight_condition = ttk.Frame(tabControl)

tabControl.add(flight_condition,
			   text='Flight Conditions')
tabControl.pack(expand=1, fill="both")
tk.Label(flight_condition, text="Take Off Weight").grid(column=0, row=0, padx=10, pady=10)
take_off_weight = tk.Entry(flight_condition)
take_off_weight.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)

# Mach
mach_number = tk.Frame(flight_condition,
				highlightbackground="black",
				highlightthickness=1)
mach_number.grid(column=0, row=1, columnspan=2, padx=10, pady=10, sticky=tk.W)
tk.Label(mach_number, text="Minimum Mach Number").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
min_mach = tk.Entry(mach_number)
min_mach.grid(column=1, row=0, padx=10, pady=10, sticky=tk.E)
tk.Label(mach_number, text="Maximum Mach Number").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
max_mach = tk.Entry(mach_number)
max_mach.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)
tk.Label(mach_number, text="Number of Mach number(max = 20)").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
num_mach = tk.Entry(mach_number)
num_mach.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)
# Altitude
altitude = tk.Frame(flight_condition,
				highlightbackground="black",
				highlightthickness=1)
altitude.grid(column=3, row=1, columnspan=2, padx=10, pady=10, sticky=tk.EW)
tk.Label(altitude, text="Minimum Altitude").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
min_alt = tk.Entry(altitude)
min_alt.grid(column=1, row=0, padx=10, pady=10, sticky=tk.E)
tk.Label(altitude, text="Maximum Altitude").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
max_alt = tk.Entry(altitude)
max_alt.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)
tk.Label(altitude, text="Number of Altitude(max = 20)").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
num_alt = tk.Entry(altitude)
num_alt.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)
# Angle
angle = tk.Frame(flight_condition,
				highlightbackground="black",
				highlightthickness=1)
angle.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=tk.EW)
tk.Label(angle, text="Minimum angle").grid(column=0, row=0, padx=38, pady=10, sticky=tk.W)
min_ang = tk.Entry(angle)
min_ang.grid(column=1, row=0, padx=0, pady=10, sticky=tk.E)
tk.Label(angle, text="Maximum angle").grid(column=0, row=1, padx=38, pady=10, sticky=tk.W)
max_ang = tk.Entry(angle)
max_ang.grid(column=1, row=1, padx=0, pady=10, sticky=tk.E)
tk.Label(angle, text="Number of angle(max = 20)").grid(column=0, row=2, padx=38, pady=10, sticky=tk.W)
num_ang = tk.Entry(angle)
num_ang.grid(column=1, row=2, padx=0, pady=10, sticky=tk.E)

# program looping control
looping = tk.Frame(flight_condition,
				highlightbackground="black",
				highlightthickness=1)
looping.grid(column=3, row=2, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
ttk.Label(looping, text="Program Looping Control").grid(column=0, row=0, columnspan=2, sticky=tk.N, pady=10)
looping_var = tk.IntVar()
looping_var.set(1)
tk.Radiobutton(looping, text="Vary Altitude and Mach together", padx=20,
			   variable=looping_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(looping, text="Vary Mach at fixed Altitude", padx=20,
			   variable=looping_var, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(looping, text="Vary Altitude at fixed Mach", padx=20,
			   variable=looping_var, value=3).grid(column=0, row=3, sticky=tk.W)


root.mainloop()
