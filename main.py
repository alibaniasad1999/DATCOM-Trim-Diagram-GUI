from audioop import reverse
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import filedialog
from tkinter import messagebox
from matplotlib import cm
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import csv
import numpy as np


root = tk.Tk()
root.title("DATCOM-GUI")
root.iconbitmap("logo.ico")
root.geometry("1000x650")
tabControl = ttk.Notebook(root)

control_cards = ttk.Frame(tabControl)

tabControl.add(control_cards,
               text='Control Cards')
tabControl.pack(expand=1, fill="both")
tk.Label(control_cards,
         text="Digital DATCOM Graphical User Interface",
         font=('Arial', 25)).grid(column=1, row=0, columnspan=8, sticky=tk.EW)
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
Other_options.grid(column=0, row=2, columnspan=4, padx=10, pady=10, sticky=tk.W)
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
tk.Label(mach_number, text="Number of Mach number (max = 20)").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
num_mach = tk.Entry(mach_number)
num_mach.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)
tk.Label(mach_number, text="Trim Mach").grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
trim_mach = tk.Entry(mach_number)
trim_mach.grid(column=1, row=3, padx=10, pady=10, sticky=tk.E)
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
tk.Label(altitude, text="Number of Altitude (max = 20)").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
num_alt = tk.Entry(altitude)
num_alt.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)

tk.Label(altitude, text="Trim Altitude").grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
trim_alt = tk.Entry(altitude)
trim_alt.grid(column=1, row=3, padx=10, pady=10, sticky=tk.E)
# Angle of attacl
angle = tk.Frame(flight_condition,
                 highlightbackground="black",
                 highlightthickness=1)
angle.grid(column=0, row=2, columnspan=2, padx=10, pady=10, sticky=tk.EW)
tk.Label(angle, text="Minimum AOA").grid(column=0, row=0, padx=38, pady=10, sticky=tk.W)
min_ang = tk.Entry(angle)
min_ang.grid(column=1, row=0, padx=0, pady=10, sticky=tk.E)
tk.Label(angle, text="Maximum AOA").grid(column=0, row=1, padx=38, pady=10, sticky=tk.W)
max_ang = tk.Entry(angle)
max_ang.grid(column=1, row=1, padx=0, pady=10, sticky=tk.E)
tk.Label(angle, text="Number of AOA (max = 20)").grid(column=0, row=2, padx=38, pady=10, sticky=tk.W)
num_ang = tk.Entry(angle)
num_ang.grid(column=1, row=2, padx=0, pady=10, sticky=tk.E)

tk.Label(angle, text="Trim AOA").grid(column=0, row=3, padx=38, pady=10, sticky=tk.W)
trim_ang = tk.Entry(angle)
trim_ang.grid(column=1, row=3, padx=0, pady=10, sticky=tk.E)

# program looping control
looping = tk.Frame(flight_condition,
                   highlightbackground="black",
                   highlightthickness=1)
looping.grid(column=3, row=2, columnspan=2, padx=10, pady=10, sticky=tk.NSEW)
ttk.Label(looping, text="Program Looping Control").grid(column=0, row=0, columnspan=2, sticky=tk.E, pady=10)
looping_var = tk.IntVar()
looping_var.set(1)
tk.Radiobutton(looping, text="Vary Altitude and Mach together", padx=40,
               variable=looping_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(looping, text="Vary Mach at fixed Altitude", padx=40,
               variable=looping_var, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(looping, text="Vary Altitude at fixed Mach", padx=40,
               variable=looping_var, value=3).grid(column=0, row=3, sticky=tk.W)
# options
options = ttk.Frame(tabControl)

tabControl.add(options,
               text='Options')
tk.Label(options, text="Reference Area").grid(column=0, row=0, padx=10, pady=10)
reference_area = tk.Entry(options)
reference_area.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)

tk.Label(options, text="Mean Aerodynamic Chord").grid(column=0, row=1, padx=10, pady=10)
mean_aerodynamic_chord = tk.Entry(options)
mean_aerodynamic_chord.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)

tk.Label(options, text="Wing Span").grid(column=0, row=2, padx=10, pady=10)
wing_span = tk.Entry(options)
wing_span.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)

tk.Label(options, text="Surface Roughness").grid(column=0, row=3, padx=10, pady=10)
surface_roughness = tk.Entry(options)
surface_roughness.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)

# Synthesis
synthesis = ttk.Frame(tabControl)

tabControl.add(synthesis,
               text='Synthesis')
tabControl.pack(expand=1, fill="both")

tk.Label(synthesis, text="XCG").grid(column=0, row=0, padx=10, pady=10)
XCG = tk.Entry(synthesis)
XCG.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Longitudinal Location of CG").grid(column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ZCG").grid(column=0, row=1, padx=10, pady=10)
ZCG = tk.Entry(synthesis)
ZCG.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Vertical Location of CG relative to reference plane").grid(
    column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="XW").grid(column=0, row=2, padx=10, pady=10)
XW = tk.Entry(synthesis)
XW.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Longitudinal Location of theoretical wing Apex").grid(
    column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ZW").grid(column=0, row=3, padx=10, pady=10)
ZW = tk.Entry(synthesis)
ZW.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Vertical Location of theoretical wing Apex relative to reference plane").grid(
    column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ALIW").grid(column=0, row=4, padx=10, pady=10)
ALIW = tk.Entry(synthesis)
ALIW.grid(column=1, row=4, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Wing root chord incidence angle measured from reference plane").grid(
    column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ALIH").grid(column=0, row=5, padx=10, pady=10)
ALIH = tk.Entry(synthesis)
ALIH.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Horizontal tail root chord incidence angle measured from reference plane").grid(
    column=2, row=5, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="XH").grid(column=0, row=6, padx=10, pady=10)
XH = tk.Entry(synthesis)
XH.grid(column=1, row=6, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Longitudinal Location of theoretical horizontal tail Apex").grid(
    column=2, row=6, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ZH").grid(column=0, row=7, padx=10, pady=10)
ZH = tk.Entry(synthesis)
ZH.grid(column=1, row=7, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Vertical Location of theoretical horizontal tail Apex relative to reference plane").grid(
    column=2, row=7, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="XV").grid(column=0, row=8, padx=10, pady=10)
XV = tk.Entry(synthesis)
XV.grid(column=1, row=8, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Longitudinal Location of theoretical vertical tail Apex").grid(
    column=2, row=8, padx=10, pady=10, sticky=tk.W)

tk.Label(synthesis, text="ZV").grid(column=0, row=9, padx=10, pady=10)
ZV = tk.Entry(synthesis)
ZV.grid(column=1, row=9, padx=0, pady=10, sticky=tk.W)
tk.Label(synthesis, text="Vertical Location of theoretical vertical tail Apex").grid(
    column=2, row=9, padx=10, pady=10, sticky=tk.W)

# vertup_frame = tk.Frame(synthesis,
# 				highlightbackground="black",
# 				highlightthickness=1)
# vertup_frame.grid(column=3, row=0, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
# tk.Label(vertup_frame, text="Vertical plane above ref plane").grid(column=0, row=0)
# vertup = tk.StringVar()
# vertup.set(".TRUE.")
# tk.Radiobutton(vertup_frame, text="True", padx=20,
# 			   variable=vertup, value=".TRUE.").grid(column=0, row=1, sticky=tk.W)
# tk.Radiobutton(vertup_frame, text="False", padx=20,
# 			   variable=vertup, value=".FALSE.").grid(column=0, row=2, sticky=tk.W)
#
tk.Label(synthesis, text="Scale Factor").grid(column=0, row=10, padx=10, pady=10)
SCALE = tk.Entry(synthesis)
SCALE.grid(column=1, row=10, padx=0, pady=10, sticky=tk.EW)

# Body
body = ttk.Frame(tabControl)
tabControl.add(body,
               text='Body')
body_nose = tk.Frame(body,
                           highlightbackground="black",
                           highlightthickness=1)
body_nose.grid(column=0, row=0, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
tk.Label(body_nose, text="Nose Type").grid(column=0, row=0)

body_nose_type = tk.IntVar()
body_nose_type.set(1)
tk.Radiobutton(body_nose, text="Conical Nose", padx=20,
               variable=body_nose_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(body_nose, text="Ogive Nose", padx=20,
               variable=body_nose_type, value=2).grid(column=0, row=2, sticky=tk.W)

nose_len = tk.Entry(body)
nose_len.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(body, text="Length of body nose").grid(
    column=0, row=2, padx=10, pady=10, sticky=tk.W)

body_tail = tk.Frame(body,
                           highlightbackground="black",
                           highlightthickness=1)
body_tail.grid(column=0, row=3, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
tk.Label(body_tail, text="Tail Type").grid(column=0, row=0)

body_tail_type = tk.IntVar()
body_tail_type.set(1)
tk.Radiobutton(body_tail, text="Conical Tail", padx=20,
               variable=body_tail_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(body_tail, text="Ogive Tail", padx=20,
               variable=body_tail_type, value=2).grid(column=0, row=2, sticky=tk.W)


cylindrical_after_body_len = tk.Entry(body)
cylindrical_after_body_len.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(body, text="Length of cylindrical after body").grid(
    column=0, row=5, padx=10, pady=10, sticky=tk.W)

body_type_frame = tk.Frame(body,
                           highlightbackground="black",
                           highlightthickness=1)
body_type_frame.grid(column=0, row=10, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
tk.Label(body_type_frame, text="Body Type").grid(column=0, row=0)
body_type = tk.IntVar()
body_type.set(3)
tk.Radiobutton(body_type_frame, text="straight wing, no area rule", padx=20,
               variable=body_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(body_type_frame, text="swept wing, no area rule", padx=20,
               variable=body_type, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(body_type_frame, text="swept wing, area rule", padx=20,
               variable=body_type, value=3).grid(column=0, row=3, sticky=tk.W)

body_method_frame = tk.Frame(body,
                           highlightbackground="black",
                           highlightthickness=1)
body_method_frame.grid(column=2, row=0, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.NSEW)
tk.Label(body_method_frame, text="Body Method").grid(column=0, row=0)
body_method = tk.IntVar()
body_method.set(2)
tk.Radiobutton(body_method_frame, text="use exiting methods", padx=20,
               variable=body_method, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(body_method_frame, text="use jorgensen methon", padx=20,
               variable=body_method, value=2).grid(column=0, row=2, sticky=tk.W)

# body CSV
body_CSV = tk.Frame(body,
                           highlightbackground="black",
                           highlightthickness=1)
body_CSV.grid(column=2, row=2, padx=10, pady=10, rowspan=10, columnspan=2, sticky=tk.EW)
tk.Label(body_CSV, text="Insert your data to Body.csv\n first insert variable then your aircraft data\nVariables:\nX : Array of longitudinal Distance\nZU: Upper body\nZL:Lower body\nP: Section Equivalent Radius\nP: Section Area\nS:Section Periphery\n from R, S and P you shoul choice at least one and maximum two\nsample:\nX,1,2,3,4,5").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)


# Wing
wing = ttk.Frame(tabControl)

tabControl.add(wing,
               text='Wing')
# tabControl.pack(expand=1, fill="both")
tk.Label(wing, text="CHRDTP").grid(column=0, row=0, padx=10, pady=10)

WCHRDTP = tk.Entry(wing)
WCHRDTP.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Chord at the Tip").grid(
    column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="CHRDR").grid(column=0, row=1, padx=10, pady=10)
WCHRDR = tk.Entry(wing)
WCHRDR.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Chord at the Root").grid(
    column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="SSPNE").grid(column=0, row=2, padx=10, pady=10)
WSSPNE = tk.Entry(wing)
WSSPNE.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Semi Span (Exposed)").grid(
    column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="SSPN").grid(column=0, row=3, padx=10, pady=10)
WSSPN = tk.Entry(wing)
WSSPN.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Semi Span (Theoretical)").grid(
    column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="SAVSI").grid(column=0, row=4, padx=10, pady=10)
WSAVSI = tk.Entry(wing)
WSAVSI.grid(column=1, row=4, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Sweep Angle").grid(
    column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="CHSTAT").grid(column=0, row=5, padx=10, pady=10)
WCHSTAT = tk.Entry(wing)
WCHSTAT.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Reference chord station for inboard and outboard panel sweep angles, fraction of chord ").grid(
    column=2, row=5, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="TWISTA").grid(column=0, row=6, padx=10, pady=10)
WTWISTA = tk.Entry(wing)
WTWISTA.grid(column=1, row=6, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Twist angle (negative L.E rotated down) ").grid(
    column=2, row=6, padx=10, pady=10, sticky=tk.W)

tk.Label(wing, text="DHDADI").grid(column=0, row=7, padx=10, pady=10)
WDHDADI = tk.Entry(wing)
WDHDADI.grid(column=1, row=7, padx=0, pady=10, sticky=tk.W)
tk.Label(wing, text="Dihedral Angle").grid(
    column=2, row=7, padx=10, pady=10, sticky=tk.W)

wing_type_frame = tk.Frame(wing,
                           highlightbackground="black",
                           highlightthickness=1)
wing_type_frame.grid(column=0, row=8, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
tk.Label(wing_type_frame, text="Wing Type").grid(column=0, row=0)
wing_type = tk.IntVar()
wing_type.set(1)
tk.Radiobutton(wing_type_frame, text="straight tapered platform", padx=20,
               variable=wing_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(wing_type_frame, text="double delta platform AR<3", padx=20,
               variable=wing_type, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(wing_type_frame, text="Cranked platform AR>3", padx=20,
               variable=wing_type, value=3).grid(column=0, row=3, sticky=tk.W)

# Horizontal Tail
horizontal_tail = ttk.Frame(tabControl)

tabControl.add(horizontal_tail,
               text='Horizontal Tail')
tabControl.pack(expand=1, fill="both")

tk.Label(horizontal_tail, text="CHRDTP").grid(column=0, row=0, padx=10, pady=10)

HCHRDTP = tk.Entry(horizontal_tail)
HCHRDTP.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Chord at the Tip").grid(
    column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="CHRDR").grid(column=0, row=1, padx=10, pady=10)
HCHRDR = tk.Entry(horizontal_tail)
HCHRDR.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Chord at the Root").grid(
    column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="SSPNE").grid(column=0, row=2, padx=10, pady=10)
HSSPNE = tk.Entry(horizontal_tail)
HSSPNE.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Semi Span (Exposed)").grid(
    column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="SSPN").grid(column=0, row=3, padx=10, pady=10)
HSSPN = tk.Entry(horizontal_tail)
HSSPN.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Semi Span (Theoretical)").grid(
    column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="SAVSI").grid(column=0, row=4, padx=10, pady=10)
HSAVSI = tk.Entry(horizontal_tail)
HSAVSI.grid(column=1, row=4, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Sweep Angle").grid(
    column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="CHSTAT").grid(column=0, row=5, padx=10, pady=10)
HCHSTAT = tk.Entry(horizontal_tail)
HCHSTAT.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail,
         text="Reference chord station for inboard and outboard panel sweep angles, fraction of chord ").grid(
    column=2, row=5, padx=10, pady=10, columnspan=2, sticky=tk.W)

tk.Label(horizontal_tail, text="TWISTA").grid(column=0, row=6, padx=10, pady=10)
HTWISTA = tk.Entry(horizontal_tail)
HTWISTA.grid(column=1, row=6, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Twist angle (negative L.E rotated down) ").grid(
    column=2, row=6, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="DHDADI").grid(column=0, row=7, padx=10, pady=10)
HDHDADI = tk.Entry(horizontal_tail)
HDHDADI.grid(column=1, row=7, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Dihedral Angle").grid(
    column=2, row=7, padx=10, pady=10, sticky=tk.W)

tk.Label(horizontal_tail, text="Airfoil").grid(column=0, row=8, padx=10, pady=10)
Hairfoil = tk.Entry(horizontal_tail)
Hairfoil.grid(column=1, row=8, padx=0, pady=10, sticky=tk.W)
tk.Label(horizontal_tail, text="Write airfoil name like: \"NACA-H-4-0012\"").grid(
    column=2, row=8, padx=10, pady=10, sticky=tk.W)

horizontal_tail_type_frame = tk.Frame(horizontal_tail,
                                      highlightbackground="black",
                                      highlightthickness=1)
horizontal_tail_type_frame.grid(column=3, row=8, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.EW)
tk.Label(horizontal_tail_type_frame, text="Horizontal Tail Type").grid(column=0, row=0)
horizontal_tail_type = tk.IntVar()
horizontal_tail_type.set(1)
tk.Radiobutton(horizontal_tail_type_frame, text="straight tapered platform", padx=20,
               variable=horizontal_tail_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(horizontal_tail_type_frame, text="double delta platform AR<3", padx=20,
               variable=horizontal_tail_type, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(horizontal_tail_type_frame, text="Cranked platform AR>3", padx=20,
               variable=horizontal_tail_type, value=3).grid(column=0, row=3, sticky=tk.W)

# Vertical Tail
vertical_tail = ttk.Frame(tabControl)

tabControl.add(vertical_tail,
               text='Vertical Tail')
# tabControl.pack(expand=1, fill="both")

tk.Label(vertical_tail, text="CHRDTP").grid(column=0, row=0, padx=10, pady=10)
VCHRDTP = tk.Entry(vertical_tail)
VCHRDTP.grid(column=1, row=0, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Chord at the Tip").grid(
    column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="CHRDR").grid(column=0, row=1, padx=10, pady=10)
VCHRDR = tk.Entry(vertical_tail)
VCHRDR.grid(column=1, row=1, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Chord at the Root").grid(
    column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="SSPNE").grid(column=0, row=2, padx=10, pady=10)
VSSPNE = tk.Entry(vertical_tail)
VSSPNE.grid(column=1, row=2, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Semi Span (Exposed)").grid(
    column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="SSPN").grid(column=0, row=3, padx=10, pady=10)
VSSPN = tk.Entry(vertical_tail)
VSSPN.grid(column=1, row=3, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Semi Span (Theoretical)").grid(
    column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="SAVSI").grid(column=0, row=4, padx=10, pady=10)
VSAVSI = tk.Entry(vertical_tail)
VSAVSI.grid(column=1, row=4, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Sweep Angle").grid(
    column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="CHSTAT").grid(column=0, row=5, padx=10, pady=10)
VCHSTAT = tk.Entry(vertical_tail)
VCHSTAT.grid(column=1, row=5, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail,
         text="Reference chord station for inboard and outboard panel sweep angles, fraction of chord ").grid(
    column=2, row=5, padx=10, pady=10, columnspan=2, sticky=tk.W)

tk.Label(vertical_tail, text="TWISTA").grid(column=0, row=6, padx=10, pady=10)
VTWISTA = tk.Entry(vertical_tail)
VTWISTA.grid(column=1, row=6, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Twist angle (negative L.E rotated down) ").grid(
    column=2, row=6, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="DHDADI").grid(column=0, row=7, padx=10, pady=10)
VDHDADI = tk.Entry(vertical_tail)
VDHDADI.grid(column=1, row=7, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Dihedral Angle").grid(
    column=2, row=7, padx=10, pady=10, sticky=tk.W)

tk.Label(vertical_tail, text="Airfoil").grid(column=0, row=8, padx=10, pady=10)
Vairfoil = tk.Entry(vertical_tail)
Vairfoil.grid(column=1, row=8, padx=0, pady=10, sticky=tk.W)
tk.Label(vertical_tail, text="Write airfoil name like: \"NACA-V-4-0012\"").grid(
    column=2, row=8, padx=10, pady=10, sticky=tk.W)

vertical_tail_type_frame = tk.Frame(vertical_tail,
                                    highlightbackground="black",
                                    highlightthickness=1)
vertical_tail_type_frame.grid(column=3, row=8, padx=10, pady=10, rowspan=2, columnspan=2, sticky=tk.W)
tk.Label(vertical_tail_type_frame, text="Vertical Tail Type").grid(column=0, row=0)

vertical_tail_type = tk.IntVar()
vertical_tail_type.set(1)
tk.Radiobutton(vertical_tail_type_frame, text="straight tapered platform", padx=20,
               variable=vertical_tail_type, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(vertical_tail_type_frame, text="double delta platform AR<3", padx=20,
               variable=vertical_tail_type, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(vertical_tail_type_frame, text="Cranked platform AR>3", padx=20,
               variable=vertical_tail_type, value=3).grid(column=0, row=3, sticky=tk.W)


# elevator 
# with tail flap work as elevator
elevator = ttk.Frame(tabControl)
tabControl.add(elevator,
               text='Elevator')

tabControl.pack(expand=1, fill="both")


elevator_type = tk.Frame(elevator,
                      highlightbackground="black",
                      highlightthickness=1)

elevator_type.grid(column=1, row=2, padx=10, pady=20, sticky=tk.W)

tk.Label(elevator_type, text="Elevator Type:").grid(column=0, row=0, padx=10, pady=10)

ele_type_var = tk.IntVar()
ele_type_var.set(1)

tk.Radiobutton(elevator_type, text="plian flaps", padx=20, variable=dim_unit_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(elevator_type, text="single sloted flaps", padx=20, variable=dim_unit_var, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(elevator_type, text="fowler flaps", padx=20, variable=dim_unit_var, value=3).grid(column=0, row=3, sticky=tk.W)
tk.Radiobutton(elevator_type, text="double sloted flaps", padx=20, variable=dim_unit_var, value=4).grid(column=0, row=4, sticky=tk.W)
tk.Radiobutton(elevator_type, text="split flaps", padx=20, variable=dim_unit_var, value=5).grid(column=0, row=5, sticky=tk.W)
tk.Radiobutton(elevator_type, text="leading edge flaps", padx=20, variable=dim_unit_var, value=6).grid(column=0, row=6, sticky=tk.W)
tk.Radiobutton(elevator_type, text="lesding edge slats", padx=20, variable=dim_unit_var, value=7).grid(column=0, row=7, sticky=tk.W)
tk.Radiobutton(elevator_type, text="kruger", padx=20, variable=dim_unit_var, value=8).grid(column=0, row=8, sticky=tk.W)

# elevator angle

elevator_angle = tk.Frame(elevator,
                       highlightbackground="black",
                       highlightthickness=1)
elevator_angle.grid(column=0, row=2, columnspan=1, padx=10, pady=10, sticky=tk.W)

tk.Label(elevator_angle, text="Minimum Elevator Angle").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
min_ele_ang = tk.Entry(elevator_angle)
min_ele_ang.grid(column=1, row=0, padx=10, pady=10, sticky=tk.E)

tk.Label(elevator_angle, text="Maximum Elevator Angle").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
max_ele_ang = tk.Entry(elevator_angle)
max_ele_ang.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)


tk.Label(elevator_angle, text="Number of Elevator angle (max = 9)").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
num_ele_ang = tk.Entry(elevator_angle)
num_ele_ang.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)

# elevator data
elevator_data = tk.Frame(elevator,
                      highlightbackground="black",
                      highlightthickness=1)
elevator_data.grid(column=0, row=1, columnspan=10, padx=10, pady=10, sticky=tk.W)


tk.Label(elevator_data, text="CHRDFI").grid(column=0, row=0, padx=10, pady=10, sticky=tk.W)
CHRDFI = tk.Entry(elevator_data)
CHRDFI.grid(column=1, row=0, padx=10, pady=10, sticky=tk.E)
tk.Label(elevator_data, text="Flap chord at inboard end of flap, measured parallel to longitudinal axis").grid(column=2, row=0, padx=10, pady=10, sticky=tk.W)

tk.Label(elevator_data, text="CHRDFO").grid(column=0, row=1, padx=10, pady=10, sticky=tk.W)
CHRDFO = tk.Entry(elevator_data)
CHRDFO.grid(column=1, row=1, padx=10, pady=10, sticky=tk.E)
tk.Label(elevator_data, text="Flap chord at outboard end of flap, measured parallel to longitudinal axis").grid(column=2, row=1, padx=10, pady=10, sticky=tk.W)

tk.Label(elevator_data, text="SPANFI").grid(column=0, row=2, padx=10, pady=10, sticky=tk.W)
SPANFI = tk.Entry(elevator_data)
SPANFI.grid(column=1, row=2, padx=10, pady=10, sticky=tk.E)
tk.Label(elevator_data, text="Span location of inboard end of flap, measured perpendicular to vertical plane of symmetry").grid(column=2, row=2, padx=10, pady=10, sticky=tk.W)

tk.Label(elevator_data, text="SPANFO").grid(column=0, row=3, padx=10, pady=10, sticky=tk.W)
SPANFO = tk.Entry(elevator_data)
SPANFO.grid(column=1, row=3, padx=10, pady=10, sticky=tk.E)
tk.Label(elevator_data, text="Span location of outboard end of flap, measured perpendicular to vertical plane of symmetry").grid(column=2, row=3, padx=10, pady=10, sticky=tk.W)

tk.Label(elevator_data, text="CB").grid(column=0, row=4, padx=10, pady=10, sticky=tk.W)
CB = tk.Entry(elevator_data)
CB.grid(column=1, row=4, padx=10, pady=10, sticky=tk.E)
tk.Label(elevator_data, text="Average chord of the balance").grid(column=2, row=4, padx=10, pady=10, sticky=tk.W)

tk.Label(elevator_data, text="TC").grid(column=0, row=5, padx=10, pady=10, sticky=tk.W)
TC = tk.Entry(elevator_data)
TC.grid(column=1, row=5, padx=10, pady=10, sticky=tk.E)
tk.Label(elevator_data, text="Average thickness of the control at hinge line").grid(column=2, row=5, padx=10, pady=10, sticky=tk.W)

elevator_nose_type = tk.Frame(elevator,
                      highlightbackground="black",
                      highlightthickness=1)

elevator_nose_type.grid(column=3, row=2, padx=10, pady=20, sticky=tk.W)

tk.Label(elevator_nose_type, text="Elevator nose Type:").grid(column=0, row=0, padx=10, pady=10)

ele_nose_type_var = tk.IntVar()
ele_nose_type_var.set(1)

tk.Radiobutton(elevator_nose_type, text="round nose flap", padx=20, variable=dim_unit_var, value=1).grid(column=0, row=1, sticky=tk.W)
tk.Radiobutton(elevator_nose_type, text="elliptic nose flap", padx=20, variable=dim_unit_var, value=2).grid(column=0, row=2, sticky=tk.W)
tk.Radiobutton(elevator_nose_type, text="sharp nose flap", padx=20, variable=dim_unit_var, value=3).grid(column=0, row=3, sticky=tk.W)


###### Trim diagram ######
trim = ttk.Frame(tabControl)
tabControl.add(trim,
               text='Trim Diagram')

tk.Label(trim, text="This app use current data so first make sure data is loaded correctly").grid(column=0, row=0, padx=10, pady=10)

trim_data_ploter = tk.Frame(trim,
                      highlightbackground="black",
                      highlightthickness=1)
trim_data_ploter.grid(column=0, row=1, padx=10, pady=20, sticky=tk.W)

tk.Label(trim_data_ploter, text="c_l_alpha").grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
c_l_alpha_E = tk.Entry(trim_data_ploter)
c_l_alpha_E.grid(column=1, row=0, padx=5, pady=5, sticky=tk.E)

tk.Label(trim_data_ploter, text="c_l_zero").grid(column=0, row=1, padx=5, pady=5, sticky=tk.W)
c_l_zero_E = tk.Entry(trim_data_ploter)
c_l_zero_E.grid(column=1, row=1, padx=5, pady=5, sticky=tk.E)

tk.Label(trim_data_ploter, text="c_l_ih").grid(column=0, row=2, padx=5, pady=5, sticky=tk.W)
c_l_ih_E = tk.Entry(trim_data_ploter)
c_l_ih_E.grid(column=1, row=2, padx=5, pady=5, sticky=tk.E)

tk.Label(trim_data_ploter, text="c_l_delta_elevator").grid(column=0, row=3, padx=5, pady=5, sticky=tk.W)
c_l_delta_elevator_E = tk.Entry(trim_data_ploter)
c_l_delta_elevator_E.grid(column=1, row=3, padx=5, pady=5, sticky=tk.E)

tk.Label(trim_data_ploter, text="c_m_alpha").grid(column=0, row=4, padx=5, pady=5, sticky=tk.W)
c_m_alpha_E = tk.Entry(trim_data_ploter)
c_m_alpha_E.grid(column=1, row=4, padx=5, pady=5, sticky=tk.E)

tk.Label(trim_data_ploter, text="c_m_zero").grid(column=0, row=5, padx=5, pady=5, sticky=tk.W)
c_m_zero_E = tk.Entry(trim_data_ploter)
c_m_zero_E.grid(column=1, row=5, padx=5, pady=5, sticky=tk.E)

tk.Label(trim_data_ploter, text="c_m_ih").grid(column=0, row=6, padx=5, pady=5, sticky=tk.W)
c_m_ih_E = tk.Entry(trim_data_ploter)
c_m_ih_E.grid(column=1, row=6, padx=5, pady=5, sticky=tk.E)

tk.Label(trim_data_ploter, text="c_m_delta_elevator").grid(column=0, row=7, padx=5, pady=5, sticky=tk.W)
c_m_delta_elevator_E = tk.Entry(trim_data_ploter)
c_m_delta_elevator_E.grid(column=1, row=7, padx=5, pady=5, sticky=tk.E)

# tk.Label(trim_data_ploter, text="ih").grid(column=0, row=8, padx=5, pady=5, sticky=tk.W)
# ih_E = tk.Entry(trim_data_ploter)
# ih_E.grid(column=1, row=8, padx=5, pady=5, sticky=tk.E)

# tk.Label(trim_data_ploter, text="x_cg").grid(column=0, row=9, padx=5, pady=5, sticky=tk.W)
# x_cg_E = tk.Entry(trim_data_ploter)
# x_cg_E.grid(column=1, row=9, padx=5, pady=5, sticky=tk.E)

# c_l_alpha = 2.80
# c_l_zero = 0.1
# c_l_ih = 0.25
# c_l_delta_elevator = 0.25
# c_m_alpha = -0.78
# c_m_zero = -0.025
# c_m_ih = -0.38
# c_m_delta_elevator = -0.38
# ih = 0
# x_cg = 0.29

# delta_elevator = np.linspace(-30/180*np.pi, 15/180*np.pi, 10)
# c_l = np.linspace(-1, 2, 30)

# c_m_alpha_c_l_alpha = (c_m_alpha / c_l_alpha)

# c_m_zero_bar = c_m_zero - c_m_alpha_c_l_alpha * c_l_zero

# c_m_delta_elevator_bar = c_m_delta_elevator - c_m_alpha_c_l_alpha * c_l_delta_elevator

# c_m_ih_bar = c_m_ih - c_m_alpha_c_l_alpha * c_l_ih


# c_m = []
# for i in range(int(len(delta_elevator))):
#     c_m.append([])
#     for j in range(len(c_l)):
#         c_m[i].append(c_m_zero_bar + (c_m_alpha / c_l_alpha) * c_l[j] + c_m_delta_elevator_bar * delta_elevator[i]) 
    
# # for i in range(len(c_m)):
# #     c_m[i].reverse()

# fig, ax = plt.subplots()
# # ax.plot(c_m[ 0 ], c_l ,c_m[ 1 ], c_l ,c_m[ 2 ], c_l ,c_m[ 3 ], c_l ,c_m[ 4 ], c_l ,c_m[ 5 ], c_l ,c_m[ 6 ], c_l ,c_m[ 7 ], c_l ,c_m[ 8 ], c_l ,c_m[ 9 ], c_l)
# # ax.plot(c_m[ 0 ], c_l)
# # ax.plot(c_m[ 2 ], c_l )
# for i in c_m:
#     ax.plot(i, c_l)
# fig.legend([str(round(i, 2)) for i in delta_elevator])
# # fig.plot(c_m[ 0 ], c_l ,c_m[ 1 ], c_l ,c_m[ 2 ], c_l ,c_m[ 3 ], c_l ,c_m[ 4 ], c_l ,c_m[ 5 ], c_l ,c_m[ 6 ], c_l ,c_m[ 7 ], c_l ,c_m[ 8 ], c_l ,c_m[ 9 ], c_l)
# # fig.legend(['ele -30.0' ,'ele -25.0' ,'ele -20.0' ,'ele -15.0' ,'ele -10.0' ,'ele -5.0' ,'ele 0.0' ,'ele 5.0' ,'ele 10.0' ,'ele 15.0'])

# fig.set_dpi(100)
# ax.invert_xaxis()
# # fig.invert_xaxis()
# # fig.Figure()
# canvas = FigureCanvasTkAgg(fig, master=trim) 
# canvas.draw()
# canvas.get_tk_widget().grid(column=1, row=1, padx=10, pady=10, sticky=tk.NE)





def load():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        # initialdir='/',
        filetypes=filetypes)

    a = [] # data from saved data
    with open(filename) as data:
        reader = csv.reader(data)
        for i in reader:
            a.append(i)

    # Control cards
    global dim_unit_var
    if a[0][0] == "FT":
        dim_unit_var.set(1)
    else:
        dim_unit_var.set(2)

    global der_unit_var
    if a[0][1] == "DEG":
        der_unit_var.set(1)
    else:
        der_unit_var.set(2)

    global dyn_der_var
    if a[0][2] == "0":
        dyn_der_var.set(0)
    else:
        dyn_der_var.set(1)

    global part_var
    if a[0][3] == "0":
        part_var.set(0)
    else:
        part_var.set(1)

    global build_var
    if a[0][4] == "0":
        build_var.set(0)
    else:
        build_var.set(1)

    # flight condition

    take_off_weight.delete(0, tk.END)
    take_off_weight.insert(0, a[1][0])

    # mach

    min_mach.delete(0, tk.END)
    min_mach.insert(0, a[2][0])

    max_mach.delete(0, tk.END)
    # mach_len = valid_len(a[2]) - 1
    max_mach.insert(0, a[2][1])

    num_mach.delete(0, tk.END)
    num_mach.insert(0, a[2][2])

    # altitude

    min_alt.delete(0, tk.END)
    min_alt.insert(0, a[3][0])

    max_alt.delete(0, tk.END)
    # alt_len = valid_len(a[3]) - 1
    max_alt.insert(0, a[3][1])

    num_alt.delete(0, tk.END)
    num_alt.insert(0, a[3][2])

    # angle od attack

    min_ang.delete(0, tk.END)
    min_ang.insert(0, a[4][0])

    max_ang.delete(0, tk.END)
    # ang_len = valid_len(a[4]) - 1
    max_ang.insert(0, a[4][1])

    num_ang.delete(0, tk.END)
    num_ang.insert(0, a[4][2])


    global looping_var
    if a[5][0] == "1":
        looping_var.set(1)
    elif a[5][0] == "2":
        looping_var.set(2)
    else:
        looping_var.set(3)
    


    # Options

    reference_area.delete(0, tk.END)
    reference_area.insert(0, a[6][0])

    mean_aerodynamic_chord.delete(0, tk.END)
    mean_aerodynamic_chord.insert(0, a[6][1])

    wing_span.delete(0, tk.END)
    wing_span.insert(0, a[6][2])

    surface_roughness.delete(0, tk.END)
    surface_roughness.insert(0, a[6][3])

    # Synthesis

    XCG.delete(0, tk.END)
    XCG.insert(0, a[7][0])

    ZCG.delete(0, tk.END)
    ZCG.insert(0, a[7][1])

    XW.delete(0, tk.END)
    XW.insert(0, a[7][2])

    ZW.delete(0, tk.END)
    ZW.insert(0, a[7][3])

    ALIW.delete(0, tk.END)
    ALIW.insert(0, a[7][4])

    ALIH.delete(0, tk.END)
    ALIH.insert(0, a[7][5])

    XH.delete(0, tk.END)
    XH.insert(0, a[7][6])

    ZH.delete(0, tk.END)
    ZH.insert(0, a[7][7])

    XV.delete(0, tk.END)
    XV.insert(0, a[7][8])

    ZV.delete(0, tk.END)
    ZV.insert(0, a[7][9])

    SCALE.delete(0, tk.END)
    SCALE.insert(0, a[7][10])

    # Wing

    WCHRDTP.delete(0, tk.END)
    WCHRDTP.insert(0, a[8][0])

    WCHRDR.delete(0, tk.END)
    WCHRDR.insert(0, a[8][1])

    WSSPNE.delete(0, tk.END)
    WSSPNE.insert(0, a[8][2])

    WSSPN.delete(0, tk.END)
    WSSPN.insert(0, a[8][3])

    WSAVSI.delete(0, tk.END)
    WSAVSI.insert(0, a[8][4])

    WCHSTAT.delete(0, tk.END)
    WCHSTAT.insert(0, a[8][5])

    WTWISTA.delete(0, tk.END)
    WTWISTA.insert(0, a[8][6])

    WDHDADI.delete(0, tk.END)
    WDHDADI.insert(0, a[8][7])

    global wing_type
    if a[8][8] == "1":
        wing_type.set(1)
    elif a[8][8] == "2":
        wing_type.set(2)
    else:
        wing_type.set(3)

    # Horizontal Tail

    HCHRDTP.delete(0, tk.END)
    HCHRDTP.insert(0, a[9][0])

    HCHRDR.delete(0, tk.END)
    HCHRDR.insert(0, a[9][1])

    HSSPNE.delete(0, tk.END)
    HSSPNE.insert(0, a[9][2])

    HSSPN.delete(0, tk.END)
    HSSPN.insert(0, a[9][3])

    HSAVSI.delete(0, tk.END)
    HSAVSI.insert(0, a[9][4])

    HCHSTAT.delete(0, tk.END)
    HCHSTAT.insert(0, a[9][5])

    HTWISTA.delete(0, tk.END)
    HTWISTA.insert(0, a[9][6])

    HDHDADI.delete(0, tk.END)
    HDHDADI.insert(0, a[9][7])

    global horizontal_tail_type
    if a[9][8] == "1":
        horizontal_tail_type.set(1)
    elif a[9][8] == "2":
        horizontal_tail_type.set(2)
    else:
        horizontal_tail_type.set(3)

    Hairfoil.delete(0, tk.END)
    Hairfoil.insert(0, a[9][9])

    # Vertical Tail

    VCHRDTP.delete(0, tk.END)
    VCHRDTP.insert(0, a[10][0])

    VCHRDR.delete(0, tk.END)
    VCHRDR.insert(0, a[10][1])

    VSSPNE.delete(0, tk.END)
    VSSPNE.insert(0, a[10][2])

    VSSPN.delete(0, tk.END)
    VSSPN.insert(0, a[10][3])

    VSAVSI.delete(0, tk.END)
    VSAVSI.insert(0, a[10][4])

    VCHSTAT.delete(0, tk.END)
    VCHSTAT.insert(0, a[10][5])

    VTWISTA.delete(0, tk.END)
    VTWISTA.insert(0, a[10][6])

    VDHDADI.delete(0, tk.END)
    VDHDADI.insert(0, a[10][7])

    global vertical_tail_type
    if a[10][8] == "1":
        vertical_tail_type.set(1)
    elif a[10][8] == "2":
        vertical_tail_type.set(2)
    else:
        vertical_tail_type.set(3)

    Vairfoil.delete(0, tk.END)
    Vairfoil.insert(0, a[10][9])

    # Body
    global body_nose_type
    if a[11][0] == "1":
        body_nose_type.set(1)
    else:
        body_nose_type.set(2)

    nose_len.delete(0, tk.END)
    nose_len.insert(0, a[11][1])

    global body_tail_type
    if a[11][2] == "1":
        body_tail_type.set(1)
    else:
        body_tail_type.set(2)

    cylindrical_after_body_len.delete(0, tk.END)
    cylindrical_after_body_len.insert(0, a[11][3])

    global body_type
    if a[11][4] == "1":
        body_type.set(1)
    elif a[11][4] == "2":
        body_type.set(2)
    else:
        body_type.set(3)

    global body_method
    if a[11][5] == "1":
        body_method.set(1)
    else:
        body_method.set(2)

    # elevator

    global ele_type_var
    if a[12][0] == "1":
        ele_type_var.set(1)
    elif a[12][0] == "2":
        ele_type_var.set(2)
    elif a[12][0] == "3":
        ele_type_var.set(3)
    elif a[12][0] == "4":
        ele_type_var.set(4)
    elif a[12][0] == "5":
        ele_type_var.set(5)
    elif a[12][0] == "6":
        ele_type_var.set(6)
    elif a[12][0] == "7":
        ele_type_var.set(7)
    else:
        ele_type_var.set(8)


    # elevator degree
    min_ele_ang.delete(0, tk.END)
    min_ele_ang.insert(0, a[12][1])

    max_ele_ang.delete(0, tk.END)
    max_ele_ang.insert(0, a[12][2])

    num_ele_ang.delete(0, tk.END)
    num_ele_ang.insert(0, a[12][3])

    # elevator data
    CHRDFI.delete(0, tk.END)
    CHRDFI.insert(0, a[12][4]) 

    CHRDFO.delete(0, tk.END)
    CHRDFO.insert(0, a[12][5]) 

    SPANFI.delete(0, tk.END)
    SPANFI.insert(0, a[12][6]) 

    SPANFO.delete(0, tk.END)
    SPANFO.insert(0, a[12][7]) 

    CB.delete(0, tk.END)
    CB.insert(0, a[12][8]) 

    TC.delete(0, tk.END)
    TC.insert(0, a[12][9]) 

    global ele_nose_type_var
    if a[12][10] == "1":
        ele_nose_type_var.set(1)
    elif a[12][10] == "2":
        ele_nose_type_var.set(2)
    else:
        ele_nose_type_var.set(3)

        # trim condition

    trim_mach.delete(0, tk.END)
    trim_mach.insert(0, a[13][0])

    trim_alt.delete(0, tk.END)
    trim_alt.insert(0, a[13][1])

    trim_ang.delete(0, tk.END)
    trim_ang.insert(0, a[13][2])


    



def save():
    data_saver = [[]]

    # Control Cards

    global dim_unit_var
    if dim_unit_var.get() == 1:
        data_saver[0].append("FT")
    else:
        data_saver[0].append("M")

    global der_unit_var
    if der_unit_var.get() == 1:
        data_saver[0].append("DEG")
    else:
        data_saver[0].append("RAD")

    global dyn_der_var
    if der_unit_var.get() == 0:
        data_saver[0].append("0")
    else:
        data_saver[0].append("1")

    global part_var
    if part_var.get() == 0:
        data_saver[0].append("0")
    else:
        data_saver[0].append("1")

    global build_var
    if build_var.get() == 0:
        data_saver[0].append("0")
    else:
        data_saver[0].append("1")

    # Flight condition

    data_saver.append([])
    data_saver[1].append(take_off_weight.get())

    # Mach
    data_saver.append([min_mach.get(), max_mach.get(), num_mach.get()])

    # Altitude
    data_saver.append([min_alt.get(), max_alt.get(), num_alt.get()])

    # Angle of Attack
    data_saver.append([min_ang.get(), max_ang.get(), num_ang.get()])

    # looping
    global looping_var
    if looping_var.get() == 1:
        data_saver.append("1")
    elif looping_var.get() == 2:
        data_saver.append("2")
    else:
        data_saver.append("3")

    # Options
    data_saver.append([])

    data_saver[6].append(reference_area.get())

    data_saver[6].append(mean_aerodynamic_chord.get())

    data_saver[6].append(wing_span.get())

    data_saver[6].append(surface_roughness.get())

    # Synthesis
    data_saver.append([])

    data_saver[7].append(XCG.get())

    data_saver[7].append(ZCG.get())

    data_saver[7].append(XW.get())

    data_saver[7].append(ZW.get())

    data_saver[7].append(ALIW.get())

    data_saver[7].append(ALIH.get())

    data_saver[7].append(XH.get())

    data_saver[7].append(ZH.get())

    data_saver[7].append(XV.get())

    data_saver[7].append(ZV.get())

    data_saver[7].append(SCALE.get())

    # Wing

    data_saver.append([])

    data_saver[8].append(WCHRDTP.get())

    data_saver[8].append(WCHRDR.get())

    data_saver[8].append(WSSPNE.get())

    data_saver[8].append(WSSPN.get())

    data_saver[8].append(WSAVSI.get())

    data_saver[8].append(WCHSTAT.get())

    data_saver[8].append(WTWISTA.get())

    data_saver[8].append(WDHDADI.get())

    global wing_type
    if wing_type.get() == 1:
        data_saver[8].append("1")
    elif wing_type.get() == 2:
        data_saver[8].append("2")
    else:
        data_saver[8].append("3")

    # Horizontal Tail

    data_saver.append([])

    data_saver[9].append(HCHRDTP.get())

    data_saver[9].append(HCHRDR.get())

    data_saver[9].append(HSSPNE.get())

    data_saver[9].append(HSSPN.get())

    data_saver[9].append(HSAVSI.get())

    data_saver[9].append(HCHSTAT.get())

    data_saver[9].append(HTWISTA.get())

    data_saver[9].append(HDHDADI.get())

    global horizontal_tail_type
    if horizontal_tail_type.get() == 1:
        data_saver[9].append("1")
    elif horizontal_tail_type.get() == 2:
        data_saver[9].append("2")
    else:
        data_saver[9].append("3")

    data_saver[9].append(Hairfoil.get())

    # Vertical Tail

    data_saver.append([])

    data_saver[10].append(VCHRDTP.get())

    data_saver[10].append(VCHRDR.get())

    data_saver[10].append(VSSPNE.get())

    data_saver[10].append(VSSPN.get())

    data_saver[10].append(VSAVSI.get())

    data_saver[10].append(VCHSTAT.get())

    data_saver[10].append(VTWISTA.get())

    data_saver[10].append(VDHDADI.get())

    global vertical_tail_type
    if vertical_tail_type.get() == 1:
        data_saver[10].append("1")
    elif vertical_tail_type.get() == 2:
        data_saver[10].append("2")
    else:
        data_saver[10].append("3")

    data_saver[10].append(Vairfoil.get())

    # Body

    data_saver.append([])

    global body_nose_type
    data_saver[11].append(body_nose_type.get())

    data_saver[11].append(nose_len.get())

    global body_tail_type
    data_saver[11].append(body_tail_type.get())

    data_saver[11].append(cylindrical_after_body_len.get())

    global body_type
    data_saver[11].append(body_type.get())

    global body_method
    data_saver[11].append(body_method.get())

    # elevator

    data_saver.append([])

    data_saver[12].append(str(ele_type_var.get()))

    data_saver[12].append(min_ele_ang.get())

    data_saver[12].append(max_ele_ang.get())

    data_saver[12].append(num_ele_ang.get())
    
    data_saver[12].append(CHRDFI.get())

    data_saver[12].append(CHRDFO.get())

    data_saver[12].append(SPANFI.get())

    data_saver[12].append(SPANFO.get())

    data_saver[12].append(CB.get())

    data_saver[12].append(TC.get())

    data_saver[12].append(str(ele_nose_type_var.get()))

    # trim data
    # trim condition

    data_saver.append([])

    data_saver[13].append(trim_mach.get())

    data_saver[13].append(trim_alt.get())

    data_saver[13].append(trim_ang.get())


    # Write data
    f = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
    # f = open('save_data.csv', 'w', newline='')
    writer = csv.writer(f)
    for row in data_saver:
        writer.writerow(row)
    f.close()


def loop_writer(name, list_of_num, file):
    counter = 0
    file.write('%s(1) = ' % name)
    for i in list_of_num:
        file.write('%s, ' % str(i))
        counter = counter + 1
        if counter == 8:
            file.write('\n\t\t ')
            counter = 0
    file.write('\n\t\t ')


def airfoil_writer(dat_file):
    file = open('Airfoil.txt', 'r')
    airfoil = []
    for line in file:
        airfoil.append(list(map(float, line.split())))
    file.close()
    airfoil_down = []
    airfoil_up = []
    for i in airfoil[int(len(airfoil) / 2):]:
        airfoil_down.append(i)
    for i in airfoil[0:int(len(airfoil) / 2) + 1]:
        airfoil_up.append(i)
    airfoil_up.reverse()
    XCORD = []
    YUPPER = []
    YLOWER = []
    for i in range(len(airfoil)):
        if i % 2 == 1:
            continue
        if len(YLOWER) == 49:
            XCORD.append(airfoil_up[-1][0])
            YUPPER.append(airfoil_up[-1][1])
            YLOWER.append(airfoil_down[-1][1])
            break
        XCORD.append(airfoil_up[i][0])
        YUPPER.append(airfoil_up[i][1])
        YLOWER.append(airfoil_down[i][1])

    TYPEIN = 1.0
    NPTS = 50.0
    DWASH = 1.0

    dat_file.write(' $WGSCHR ')
    dat_file.write('TYPEIN = %s, ' % str(TYPEIN))
    dat_file.write('NPTS = %s, ' % str(NPTS))
    dat_file.write('DWASH = %s, \n\t\t ' % str(DWASH))
    loop_writer('XCORD', XCORD, dat_file)
    loop_writer('YUPPER', YUPPER, dat_file)
    loop_writer('YLOWER', YLOWER, dat_file)
    dat_file.write('$\n')


def make_datcom():
    file = filedialog.asksaveasfile(mode='w', defaultextension=".dcm")
    global dim_unit_var
    if dim_unit_var.get() == 1:
        DIM = "FT"
    else:
        DIM = "M"
    # Derivatives Unit DEG = degree
    global der_unit_var
    if der_unit_var.get() == 1:
        DERIV = "DEG"
    else:
        DERIV = "RAD"

    file.write('DIM %s\n' % DIM)
    # Derivatives Unit
    file.write('DERIV %s\n' % DERIV)

    # Dynamic Derivatives
    global dyn_der_var
    if dyn_der_var.get() == 1:
        file.write('DAMP\n')

    # Add Part
    global part_var
    if part_var.get() == 1:
        file.write('PART\n')

    # Add build
    global build_var
    if build_var.get() == 1:
        file.write('BUILD\n')

    # flight condition

    # Take of weight
    WT = round(float(take_off_weight.get()), 2)

    # Mach
    NMACH = round(float(num_mach.get()), 2)

    # Array of Mach numbers

    mach_temp = np.linspace(float(min_mach.get()), float(max_mach.get()), int(num_mach.get()))
    mach_temp = mach_temp.tolist()
    MACH = [round(float(i), 3) for i in mach_temp]

    # Altitude

    NALT = round(float(num_alt.get()), 2)

    # Array of altitudes

    alt_temp = np.linspace(float(min_alt.get()), float(max_alt.get()), int(num_alt.get()))
    alt_temp = alt_temp.tolist()
    ALT = [round(float(i), 2) for i in alt_temp]

    # Angle of Attack

    NALPHA = NALT = round(float(num_ang.get()), 2)

    # Array of angle of attacks
    ang_temp = np.linspace(float(min_ang.get()), float(max_ang.get()), int(num_ang.get()))
    ang_temp = ang_temp.tolist()
    ALSCHD = [round(float(i), 2) for i in ang_temp]

    # Loop control

    global looping_var
    if looping_var.get() == 1:
        LOOP = 1.0
    elif looping_var.get() == 2:
        LOOP = 2.0
    else:
        LOOP = 3.0
    # Name list
    file.write(' $FLTCON ')
    # Take-off Weight
    file.write('WT = %s, ' % str(WT))
    # Program Looping Control
    file.write('LOOP = %s,\n\t\t ' % str(LOOP))
    # Number of Mach numbers
    file.write('NMACH = %s, ' % str(NMACH))
    # Array of Mach numbers
    loop_writer('MACH', MACH, file)
    # Number of altitudes
    file.write('NALT = %s, ' % str(NALT))
    # Array of altitudes
    loop_writer('ALT', ALT, file)
    # Number of angle of attacks
    file.write('NALPHA = %s, ' % str(NALPHA))
    # Array of angle of attacks
    loop_writer('ALSCHD', ALSCHD, file)
    # End of File
    file.write('$\n')

    # Options

    SREF = round(float(reference_area.get()), 2)
    # Mean Aerodynamic chord
    CBARR = round(float(mean_aerodynamic_chord.get()), 4)
    # Wing Span
    BLREF = round(float(wing_span.get()), 2)
    # Surface Roughness
    ROUGFC = round(float(surface_roughness.get()), 7)

    # Name list
    file.write(' $OPTINS ')
    # Refrence Area
    file.write('SREF = %s, ' % str(SREF))
    # Mean Aerodynamic chord
    file.write('CBARR = %s, ' % str(CBARR))
    # Wing Span
    file.write('BLREF = %s, ' % str(BLREF))
    # Surface Roughness
    file.write('ROUGFC = %s, ' % str(ROUGFC))
    # End of File
    file.write(' $\n')

    # Synthesis

    # Longitudinal Location of CG
    XCG_w = round(float(XCG.get()), 4)
    # Vertical Location of CG relative to reference plane
    ZCG_w = round(float(ZCG.get()), 4)
    # Longitudinal Location of theoretical wing Apex
    XW_w= round(float(XW.get()), 4)
    # Vertical Location of theoretical wing Apex relative to reference plane
    ZW_w = round(float(ZW.get()), 4)
    # wing root chord incidence angle measured from reference plane
    ALIW_w = round(float(ALIW.get()), 4)
    # horizontal tail root chord incidence angle measured from reference plane
    ALIH_w = round(float(ALIH.get()), 4)
    # Longitudinal Location of theoretical horizontal tail Apex
    XH_w = round(float(XH.get()), 4)
    # Vertical Location of theoretical horizontal tail Apex relative to reference plane
    ZH_w = round(float(ZH.get()), 4)
    # Longitudinal Location of theoretical vertical tail Apex
    XV_w = round(float(XV.get()), 4)
    # Vertical Location of theoretical vertical tail Apex
    ZV_w = round(float(ZV.get()), 4)
    # Scale factor
    SCALE_w = round(float(SCALE.get()), 4)

    # Name list
    file.write(' $SYNTHS ')
    # Longitudinal Location of CG
    file.write('XCG = %s, ' % str(XCG_w))
    # Vertical Location of CG relative to reference plane
    file.write('ZCG = %s, \n\t\t ' % str(ZCG_w))
    # Longitudinal Location of theoretical wing Apex
    file.write('XW = %s, ' % str(XW_w))
    # Vertical Location of theoretical wing Apex relative to reference plane
    file.write('ZW = %s, ' % str(ZW_w))
    # wing root chord incidence angle measured from reference plane
    file.write('ALIW = %s, \n\t\t ' % str(ALIW_w))
    # Longitudinal Location of theoretical horizontal tail Apex
    file.write('XH = %s, ' % str(XH_w))
    # Vertical Location of theoretical horizontal tail Apex relative to reference plane
    file.write('ZH = %s, ' % str(ZH_w))
    # horizontal tail root chord incidence angle measured from reference plane
    file.write('ALIH = %s, \n\t\t ' % str(ALIH_w))
    # Longitudinal Location of theoretical vertical tail Apex
    file.write('XV = %s, ' % str(XV_w))
    # Vertical Location of theoretical vertical tail Apex
    file.write('ZV = %s, \n\t\t ' % str(ZV_w))
    # Scale factor
    file.write('SCALE = %s, \n\t\t ' % str(SCALE_w))
    # Vertup
    # file.write('VERTUP = %s, ' % VERTUP)
    # End of File
    file.write(' $\n')

    # Body

    body_data = []
    with open('Body.csv', 'r') as body_file:
        body_reader = csv.reader(body_file)
        for row in body_reader:
            body_data.append(row)

    # BNOSE 1.0 conical nose, BNOSE = 2.0 ogive Nose
    global body_nose_type
    BNOSE = round(float(body_nose_type.get()), 2)
    # Length of body nose
    BLN = round(float(nose_len.get()), 4)
    # BTAIL 1.0 conical tail, BNOSE = 2.0 ogive tail
    global body_tail_type
    BTAIL = round(float(body_tail_type.get()), 4)
    # Length of cylindrical after body
    BLA = round(float(cylindrical_after_body_len.get()), 4)
    # ITYPE = 1 straight wing, no area rule
    # ITYPE = 2 swept wing, no area rule
    # ITYPE = 3 swept wing, area rule
    global body_type
    ITYPE = round(float(body_type.get()), 4)
    # Method = 1 use exiting methods
    # Method = 2 use jorgensen methon
    global body_method
    METHOD = round(float(body_method.get()), 4)

    NX = float(len(body_data[0])-1)

    # Name list
    file.write(' $BODY ')
    # Number of Sections
    file.write('NX = %s, \n\t\t ' % str(NX))
    # Body Shape
    for row in body_data:
        loop_writer(row[0], row[1:], file)

    file.write('BLN = %s, \n\t\t ' % str(BLN))

    file.write('BTAIL = %s, ' % str(BTAIL))

    file.write('ITYPE = %s, ' % str(ITYPE))

    file.write('METHOD = %s, ' % str(METHOD))

    file.write('$\n')

    # Wing

    # Chord Tip
    CHRDTP = round(float(WCHRDTP.get()), 4)
    # Chord Root
    CHRDR = round(float(WCHRDR.get()), 4)
    # Semi Span (Exposed)
    SSPNE = round(float(WSSPNE.get()), 4)
    # Semi Span (Theoretical)
    SSPN = round(float(WSSPN.get()), 4)
    # Sweep Angle
    SAVSI = round(float(WSAVSI.get()), 4)
    # Reference chord station for inboard and outboard panel sweep angles, fraction of chord
    CHSTAT = round(float(WCHSTAT.get()), 4)
    # Twist angle (negative L.E rotated down)
    TWISTA = round(float(WTWISTA.get()), 4)
    # Dihedral Angle
    DHDADI = round(float(WDHDADI.get()), 4)
    # TYPE = 1.0 straight tapered platform
    # TYPE = 2.0 double delta platform AR<3
    # TYPE = 3.0 Cranked platform AR>3
    TYPE = round(float(wing_type.get()), 2)

    # Name list
    file.write(' $WGPLNF ')
    file.write('CHRDTP = %s, ' % str(CHRDTP))
    file.write('CHRDR = %s,\n\t\t ' % str(CHRDR))
    file.write('SSPNE = %s, ' % str(SSPNE))
    file.write('SSPN = %s,\n\t\t ' % str(SSPN))
    file.write('SAVSI = %s, ' % str(SAVSI))
    file.write('CHSTAT = %s,\n\t\t ' % str(CHSTAT))
    file.write('TWISTA = %s, ' % str(TWISTA))
    file.write('DHDADI = %s,\n\t\t ' % str(DHDADI))
    file.write('TYPE = %s,' % str(TYPE))
    # End of File
    file.write('$\n')

    airfoil_writer(file)

    # Horizontal tail

    # Chord Tip
    CHRDTP = round(float(HCHRDTP.get()), 4)
    # Chord Root
    CHRDR = round(float(HCHRDR.get()), 4)
    # Semi Span (Exposed)
    SSPNE = round(float(HSSPNE.get()), 4)
    # Semi Span (Theoretical)
    SSPN = round(float(HSSPN.get()), 4)
    # Sweep Angle
    SAVSI = round(float(HSAVSI.get()), 4)
    # Reference chord station for inboard and outboard panel sweep angles, fraction of chord
    CHSTAT = round(float(HCHSTAT.get()), 4)
    # Twist angle (negative L.E rotated down)
    TWISTA = round(float(HTWISTA.get()), 4)
    # Dihedral Angle
    DHDADI = round(float(HDHDADI.get()), 4)
    # TYPE = 1.0 straight tapered platform
    # TYPE = 2.0 double delta platform AR<3
    # TYPE = 3.0 Cranked platform AR>3
    TYPE = round(float(horizontal_tail_type.get()), 2)
    HorizontalTailAirfoil = Hairfoil.get()

    # Name list
    file.write(' $HTPLNF ')
    file.write('CHRDTP = %s, ' % str(CHRDTP))
    file.write('CHRDR = %s,\n\t\t ' % str(CHRDR))
    file.write('SSPNE = %s, ' % str(SSPNE))
    file.write('SSPN = %s,\n\t\t ' % str(SSPN))
    file.write('SAVSI = %s, ' % str(SAVSI))
    file.write('CHSTAT = %s,\n\t\t ' % str(CHSTAT))
    file.write('TWISTA = %s, ' % str(TWISTA))
    file.write('DHDADI = %s,\n\t\t ' % str(DHDADI))
    file.write('TYPE = %s,' % str(TYPE))
    # End of File
    file.write('$\n')
    file.write(HorizontalTailAirfoil)
    file.write('\n')

    # Vertical tail

    # Chord Tip
    CHRDTP = round(float(VCHRDTP.get()), 4)
    # Chord Root
    CHRDR = round(float(VCHRDR.get()), 4)
    # Semi Span (Exposed)
    SSPNE = round(float(VSSPNE.get()), 4)
    # Semi Span (Theoretical)
    SSPN = round(float(VSSPN.get()), 4)
    # Sweep Angle
    SAVSI = round(float(VSAVSI.get()), 4)
    # Reference chord station for inboard and outboard panel sweep angles, fraction of chord
    CHSTAT = round(float(VCHSTAT.get()), 4)
    # Twist angle (negative L.E rotated down)
    TWISTA = round(float(VTWISTA.get()), 4)
    # Dihedral Angle
    DHDADI = round(float(VDHDADI.get()), 4)
    # TYPE = 1.0 straight tapered platform
    # TYPE = 2.0 double delta platform AR<3
    # TYPE = 3.0 Cranked platform AR>3
    TYPE = round(float(vertical_tail_type.get()), 2)
    VerticalTailAirfoil = Vairfoil.get()

    # Name list
    file.write(' $VTPLNF ')
    file.write('CHRDTP = %s, ' % str(CHRDTP))
    file.write('CHRDR = %s,\n\t\t ' % str(CHRDR))
    file.write('SSPNE = %s, ' % str(SSPNE))
    file.write('SSPN = %s,\n\t\t ' % str(SSPN))
    file.write('SAVSI = %s, ' % str(SAVSI))
    file.write('CHSTAT = %s,\n\t\t ' % str(CHSTAT))
    file.write('TWISTA = %s, ' % str(TWISTA))
    file.write('DHDADI = %s,\n\t\t ' % str(DHDADI))
    file.write('TYPE = %s,' % str(TYPE))
    # End of File
    file.write('$\n')
    file.write(VerticalTailAirfoil)
    file.write('\n')

    # elevator 
    # 
    FTYPE = round(float(ele_type_var.get()), 4)
    # Number of deflection MAX 9
    NDELTA = round(float(num_ele_ang.get()), 4)
    # Flap Deflection
    DELTA = np.linspace(float(min_ele_ang.get()), float(max_ele_ang.get()), int(num_ele_ang.get()))
    # Flap chord at inboard end of flap, measured parallel to longitudinal axis
    ECHRDFI =round(float(CHRDFI.get()), 4) 
    # Flap chord at outboard end of flap, measured parallel to longitudinal axis
    ECHRDFO = round(float(CHRDFO.get()), 4)
    # Span location of inboard end of flap, measured perpendicular to vertical plane of symmetry
    ESPANFI = round(float(SPANFI.get()), 4)
    # Span location of outboard end of flap, measured perpendicular to vertical plane of symmetry
    ESPANFO = round(float(SPANFO.get()), 4)
    # Average chord of the balance
    ECB = round(float(CB.get()), 4)
    # Average thickness of the control at hinge line
    ETC = round(float(TC.get()), 4)
    # NTYPE = 1.0 round nose flap
    # NTYPE = 2.0 elliptic nose flap
    # NTYPE = 3.0 sharp nose flap
    ENTYPE = round(float(ele_nose_type_var.get()), 4)


    file.write(' $SYMFLP ')
    file.write('FTYPE = %s,\n\t\t ' % str(FTYPE))
    file.write('NDELTA = %s,\n\t\t ' % str(NDELTA))
    loop_writer('DELTA', DELTA, file)
    file.write('CHRDFI = %s, ' % str(ECHRDFI))
    file.write('CHRDFO = %s,\n\t\t ' % str(ECHRDFO))
    file.write('SPANFI = %s, ' % str(ESPANFI))
    file.write('SPANFO = %s,\n\t\t ' % str(ESPANFO))
    file.write('CB = %s, ' % str(ECB))
    file.write('TC = %s, ' % str(ETC))
    file.write('NTYPE = %s, ' % str(ENTYPE))
    # End of File
    file.write('$\n')

    messagebox.showinfo(title="Saved", message="Done")

def load_trim_data():
    file = open('Trim_diag.dcm', 'w')
    global dim_unit_var
    if dim_unit_var.get() == 1:
        DIM = "FT"
    else:
        DIM = "M"
    # Derivatives Unit DEG = degree
    global der_unit_var
    if der_unit_var.get() == 1:
        DERIV = "DEG"
    else:
        DERIV = "RAD"

    file.write('DIM %s\n' % DIM)
    # Derivatives Unit
    file.write('DERIV %s\n' % DERIV)

    # Dynamic Derivatives
    file.write('DAMP\n')

    # Add Part
    file.write('PART\n')

    # Add build
    file.write('BUILD\n')

    # flight condition

    # Take of weight
    WT = round(float(take_off_weight.get()), 2)

    # Mach
    NMACH = round(float(1), 2)

    # Array of Mach numbers

    mach_temp = np.linspace(float(trim_mach.get()), float(trim_mach.get()), 1)
    mach_temp = mach_temp.tolist()
    MACH = [round(float(i), 3) for i in mach_temp]

    # Altitude

    NALT = round(float(num_alt.get()), 2)

    # Array of altitudes

    alt_temp = np.linspace(float(trim_alt.get()), float(trim_alt.get()), 1)
    alt_temp = alt_temp.tolist()
    ALT = [round(float(i), 2) for i in alt_temp]

    # Angle of Attack

    NALPHA = NALT = round(float(num_ang.get()), 2)

    # Array of angle of attacks
    ang_temp = np.linspace(0.0, float(trim_ang.get()), 2)
    ang_temp = ang_temp.tolist()
    ALSCHD = [round(float(i), 2) for i in ang_temp]

    # Loop control

    global looping_var

    LOOP = 1.0

    # Name list
    file.write(' $FLTCON ')
    # Take-off Weight
    file.write('WT = %s, ' % str(WT))
    # Program Looping Control
    file.write('LOOP = %s,\n\t\t ' % str(LOOP))
    # Number of Mach numbers
    file.write('NMACH = %s, ' % str('1.0'))
    # Array of Mach numbers
    loop_writer('MACH', MACH, file)
    # Number of altitudes
    file.write('NALT = %s, ' % str('1.0'))
    # Array of altitudes
    loop_writer('ALT', ALT, file)
    # Number of angle of attacks
    file.write('NALPHA = %s, ' % str('2.0'))
    # Array of angle of attacks
    loop_writer('ALSCHD', ALSCHD, file)
    # End of File
    file.write('$\n')

    # Options

    SREF = round(float(reference_area.get()), 2)
    # Mean Aerodynamic chord
    CBARR = round(float(mean_aerodynamic_chord.get()), 4)
    # Wing Span
    BLREF = round(float(wing_span.get()), 2)
    # Surface Roughness
    ROUGFC = round(float(surface_roughness.get()), 7)

    # Name list
    file.write(' $OPTINS ')
    # Refrence Area
    file.write('SREF = %s, ' % str(SREF))
    # Mean Aerodynamic chord
    file.write('CBARR = %s, ' % str(CBARR))
    # Wing Span
    file.write('BLREF = %s, ' % str(BLREF))
    # Surface Roughness
    file.write('ROUGFC = %s, ' % str(ROUGFC))
    # End of File
    file.write(' $\n')

    # Synthesis

    # Longitudinal Location of CG
    XCG_w = round(float(XCG.get()), 4)
    # Vertical Location of CG relative to reference plane
    ZCG_w = round(float(ZCG.get()), 4)
    # Longitudinal Location of theoretical wing Apex
    XW_w= round(float(XW.get()), 4)
    # Vertical Location of theoretical wing Apex relative to reference plane
    ZW_w = round(float(ZW.get()), 4)
    # wing root chord incidence angle measured from reference plane
    ALIW_w = round(float(ALIW.get()), 4)
    # horizontal tail root chord incidence angle measured from reference plane
    ALIH_w = round(float(ALIH.get()), 4)
    # Longitudinal Location of theoretical horizontal tail Apex
    XH_w = round(float(XH.get()), 4)
    # Vertical Location of theoretical horizontal tail Apex relative to reference plane
    ZH_w = round(float(ZH.get()), 4)
    # Longitudinal Location of theoretical vertical tail Apex
    XV_w = round(float(XV.get()), 4)
    # Vertical Location of theoretical vertical tail Apex
    ZV_w = round(float(ZV.get()), 4)
    # Scale factor
    SCALE_w = round(float(SCALE.get()), 4)

    # Name list
    file.write(' $SYNTHS ')
    # Longitudinal Location of CG
    file.write('XCG = %s, ' % str(XCG_w))
    # Vertical Location of CG relative to reference plane
    file.write('ZCG = %s, \n\t\t ' % str(ZCG_w))
    # Longitudinal Location of theoretical wing Apex
    file.write('XW = %s, ' % str(XW_w))
    # Vertical Location of theoretical wing Apex relative to reference plane
    file.write('ZW = %s, ' % str(ZW_w))
    # wing root chord incidence angle measured from reference plane
    file.write('ALIW = %s, \n\t\t ' % str(ALIW_w))
    # Longitudinal Location of theoretical horizontal tail Apex
    file.write('XH = %s, ' % str(XH_w))
    # Vertical Location of theoretical horizontal tail Apex relative to reference plane
    file.write('ZH = %s, ' % str(ZH_w))
    # horizontal tail root chord incidence angle measured from reference plane
    file.write('ALIH = %s, \n\t\t ' % str(ALIH_w))
    # Longitudinal Location of theoretical vertical tail Apex
    file.write('XV = %s, ' % str(XV_w))
    # Vertical Location of theoretical vertical tail Apex
    file.write('ZV = %s, \n\t\t ' % str(ZV_w))
    # Scale factor
    file.write('SCALE = %s, \n\t\t ' % str(SCALE_w))
    # Vertup
    # file.write('VERTUP = %s, ' % VERTUP)
    # End of File
    file.write(' $\n')

    # Body

    body_data = []
    with open('Body.csv', 'r') as body_file:
        body_reader = csv.reader(body_file)
        for row in body_reader:
            body_data.append(row)

    # BNOSE 1.0 conical nose, BNOSE = 2.0 ogive Nose
    global body_nose_type
    BNOSE = round(float(body_nose_type.get()), 2)
    # Length of body nose
    BLN = round(float(nose_len.get()), 4)
    # BTAIL 1.0 conical tail, BNOSE = 2.0 ogive tail
    global body_tail_type
    BTAIL = round(float(body_tail_type.get()), 4)
    # Length of cylindrical after body
    BLA = round(float(cylindrical_after_body_len.get()), 4)
    # ITYPE = 1 straight wing, no area rule
    # ITYPE = 2 swept wing, no area rule
    # ITYPE = 3 swept wing, area rule
    global body_type
    ITYPE = round(float(body_type.get()), 4)
    # Method = 1 use exiting methods
    # Method = 2 use jorgensen methon
    global body_method
    METHOD = round(float(body_method.get()), 4)

    NX = float(len(body_data[0])-1)

    # Name list
    file.write(' $BODY ')
    # Number of Sections
    file.write('NX = %s, \n\t\t ' % str(NX))
    # Body Shape
    for row in body_data:
        loop_writer(row[0], row[1:], file)

    file.write('BLN = %s, \n\t\t ' % str(BLN))

    file.write('BTAIL = %s, ' % str(BTAIL))

    file.write('ITYPE = %s, ' % str(ITYPE))

    file.write('METHOD = %s, ' % str(METHOD))

    file.write('$\n')

    # Wing

    # Chord Tip
    CHRDTP = round(float(WCHRDTP.get()), 4)
    # Chord Root
    CHRDR = round(float(WCHRDR.get()), 4)
    # Semi Span (Exposed)
    SSPNE = round(float(WSSPNE.get()), 4)
    # Semi Span (Theoretical)
    SSPN = round(float(WSSPN.get()), 4)
    # Sweep Angle
    SAVSI = round(float(WSAVSI.get()), 4)
    # Reference chord station for inboard and outboard panel sweep angles, fraction of chord
    CHSTAT = round(float(WCHSTAT.get()), 4)
    # Twist angle (negative L.E rotated down)
    TWISTA = round(float(WTWISTA.get()), 4)
    # Dihedral Angle
    DHDADI = round(float(WDHDADI.get()), 4)
    # TYPE = 1.0 straight tapered platform
    # TYPE = 2.0 double delta platform AR<3
    # TYPE = 3.0 Cranked platform AR>3
    TYPE = round(float(wing_type.get()), 2)

    # Name list
    file.write(' $WGPLNF ')
    file.write('CHRDTP = %s, ' % str(CHRDTP))
    file.write('CHRDR = %s,\n\t\t ' % str(CHRDR))
    file.write('SSPNE = %s, ' % str(SSPNE))
    file.write('SSPN = %s,\n\t\t ' % str(SSPN))
    file.write('SAVSI = %s, ' % str(SAVSI))
    file.write('CHSTAT = %s,\n\t\t ' % str(CHSTAT))
    file.write('TWISTA = %s, ' % str(TWISTA))
    file.write('DHDADI = %s,\n\t\t ' % str(DHDADI))
    file.write('TYPE = %s,' % str(TYPE))
    # End of File
    file.write('$\n')

    airfoil_writer(file)

    # Horizontal tail

    # Chord Tip
    CHRDTP = round(float(HCHRDTP.get()), 4)
    # Chord Root
    CHRDR = round(float(HCHRDR.get()), 4)
    # Semi Span (Exposed)
    SSPNE = round(float(HSSPNE.get()), 4)
    # Semi Span (Theoretical)
    SSPN = round(float(HSSPN.get()), 4)
    # Sweep Angle
    SAVSI = round(float(HSAVSI.get()), 4)
    # Reference chord station for inboard and outboard panel sweep angles, fraction of chord
    CHSTAT = round(float(HCHSTAT.get()), 4)
    # Twist angle (negative L.E rotated down)
    TWISTA = round(float(HTWISTA.get()), 4)
    # Dihedral Angle
    DHDADI = round(float(HDHDADI.get()), 4)
    # TYPE = 1.0 straight tapered platform
    # TYPE = 2.0 double delta platform AR<3
    # TYPE = 3.0 Cranked platform AR>3
    TYPE = round(float(horizontal_tail_type.get()), 2)
    HorizontalTailAirfoil = Hairfoil.get()

    # Name list
    file.write(' $HTPLNF ')
    file.write('CHRDTP = %s, ' % str(CHRDTP))
    file.write('CHRDR = %s,\n\t\t ' % str(CHRDR))
    file.write('SSPNE = %s, ' % str(SSPNE))
    file.write('SSPN = %s,\n\t\t ' % str(SSPN))
    file.write('SAVSI = %s, ' % str(SAVSI))
    file.write('CHSTAT = %s,\n\t\t ' % str(CHSTAT))
    file.write('TWISTA = %s, ' % str(TWISTA))
    file.write('DHDADI = %s,\n\t\t ' % str(DHDADI))
    file.write('TYPE = %s,' % str(TYPE))
    # End of File
    file.write('$\n')
    file.write(HorizontalTailAirfoil)
    file.write('\n')

    # Vertical tail

    # Chord Tip
    CHRDTP = round(float(VCHRDTP.get()), 4)
    # Chord Root
    CHRDR = round(float(VCHRDR.get()), 4)
    # Semi Span (Exposed)
    SSPNE = round(float(VSSPNE.get()), 4)
    # Semi Span (Theoretical)
    SSPN = round(float(VSSPN.get()), 4)
    # Sweep Angle
    SAVSI = round(float(VSAVSI.get()), 4)
    # Reference chord station for inboard and outboard panel sweep angles, fraction of chord
    CHSTAT = round(float(VCHSTAT.get()), 4)
    # Twist angle (negative L.E rotated down)
    TWISTA = round(float(VTWISTA.get()), 4)
    # Dihedral Angle
    DHDADI = round(float(VDHDADI.get()), 4)
    # TYPE = 1.0 straight tapered platform
    # TYPE = 2.0 double delta platform AR<3
    # TYPE = 3.0 Cranked platform AR>3
    TYPE = round(float(vertical_tail_type.get()), 2)
    VerticalTailAirfoil = Vairfoil.get()

    # Name list
    file.write(' $VTPLNF ')
    file.write('CHRDTP = %s, ' % str(CHRDTP))
    file.write('CHRDR = %s,\n\t\t ' % str(CHRDR))
    file.write('SSPNE = %s, ' % str(SSPNE))
    file.write('SSPN = %s,\n\t\t ' % str(SSPN))
    file.write('SAVSI = %s, ' % str(SAVSI))
    file.write('CHSTAT = %s,\n\t\t ' % str(CHSTAT))
    file.write('TWISTA = %s, ' % str(TWISTA))
    file.write('DHDADI = %s,\n\t\t ' % str(DHDADI))
    file.write('TYPE = %s,' % str(TYPE))
    # End of File
    file.write('$\n')
    file.write(VerticalTailAirfoil)
    file.write('\n')

    # elevator 
    # 
    FTYPE = round(float(ele_type_var.get()), 4)
    # Number of deflection MAX 9
    NDELTA = round(float(num_ele_ang.get()), 4)
    # Flap Deflection
    DELTA = np.linspace(float(min_ele_ang.get()), float(max_ele_ang.get()), int(num_ele_ang.get()))
    # Flap chord at inboard end of flap, measured parallel to longitudinal axis
    ECHRDFI =round(float(CHRDFI.get()), 4) 
    # Flap chord at outboard end of flap, measured parallel to longitudinal axis
    ECHRDFO = round(float(CHRDFO.get()), 4)
    # Span location of inboard end of flap, measured perpendicular to vertical plane of symmetry
    ESPANFI = round(float(SPANFI.get()), 4)
    # Span location of outboard end of flap, measured perpendicular to vertical plane of symmetry
    ESPANFO = round(float(SPANFO.get()), 4)
    # Average chord of the balance
    ECB = round(float(CB.get()), 4)
    # Average thickness of the control at hinge line
    ETC = round(float(TC.get()), 4)
    # NTYPE = 1.0 round nose flap
    # NTYPE = 2.0 elliptic nose flap
    # NTYPE = 3.0 sharp nose flap
    ENTYPE = round(float(ele_nose_type_var.get()), 4)


    file.write(' $SYMFLP ')
    file.write('FTYPE = %s,\n\t\t ' % str(FTYPE))
    file.write('NDELTA = %s,\n\t\t ' % str(NDELTA))
    loop_writer('DELTA', DELTA, file)
    file.write('CHRDFI = %s, ' % str(ECHRDFI))
    file.write('CHRDFO = %s,\n\t\t ' % str(ECHRDFO))
    file.write('SPANFI = %s, ' % str(ESPANFI))
    file.write('SPANFO = %s,\n\t\t ' % str(ESPANFO))
    file.write('CB = %s, ' % str(ECB))
    file.write('TC = %s, ' % str(ETC))
    file.write('NTYPE = %s, ' % str(ENTYPE))
    # End of File
    file.write('$\n')

def plot_trim_data():
    c_l_alpha = float(c_l_alpha_E.get())
    c_l_zero = float(c_l_zero_E.get())
    c_l_ih = float(c_l_ih_E.get())
    c_l_delta_elevator = float(c_l_delta_elevator_E.get())
    c_m_alpha = float(c_m_alpha_E.get())
    c_m_zero = float(c_m_zero_E.get())
    c_m_ih = float(c_m_ih_E.get())
    c_m_delta_elevator = float(c_m_delta_elevator_E.get())
    # ih = float(ih_E.get())
    # x_cg = float(x_cg_E.get())

    delta_elevator = np.linspace(float(min_ele_ang.get()), float(max_ele_ang.get()), int(num_ele_ang.get()))
    c_l = np.linspace(0, 2, 30)

    c_m_alpha_c_l_alpha = (c_m_alpha / c_l_alpha)

    c_m_zero_bar = c_m_zero - c_m_alpha_c_l_alpha * c_l_zero

    c_m_delta_elevator_bar = c_m_delta_elevator - c_m_alpha_c_l_alpha * c_l_delta_elevator

    c_m_ih_bar = c_m_ih - c_m_alpha_c_l_alpha * c_l_ih


    c_m = []
    for i in range(int(len(delta_elevator))):
        c_m.append([])
        for j in range(len(c_l)):
            c_m[i].append(c_m_zero_bar + (c_m_alpha / c_l_alpha) * c_l[j] + c_m_delta_elevator_bar * delta_elevator[i]) 
        


    fig, ax = plt.subplots()

    for i in c_m:
        ax.plot(i, c_l)
    fig.legend([str(round(i, 2)) for i in delta_elevator])

    fig.set_dpi(100)
    ax.invert_xaxis()
    canvas = FigureCanvasTkAgg(fig, master=trim) 
    canvas.draw()
    canvas.get_tk_widget().grid(column=1, row=1, padx=10, pady=10, sticky=tk.NE)
    
    
# save trim data
def save_trim():

    data_saver = []

    data_saver.append(c_l_alpha_E.get())

    data_saver.append(c_l_zero_E.get())

    data_saver.append(c_l_ih_E.get())

    data_saver.append(c_l_delta_elevator_E.get())

    data_saver.append(c_m_alpha_E.get())

    data_saver.append(c_m_zero_E.get())

    data_saver.append(c_m_ih_E.get())

    data_saver.append(c_m_delta_elevator_E.get())

    # Write data
    f = filedialog.asksaveasfile(mode='w', defaultextension=".csv")
    # f = open('save_data.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(data_saver)
    f.close()

def load_trim_file():
    filetypes = (
        ('csv files', '*.csv'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Open a file',
        # initialdir='/',
        filetypes=filetypes)

    a = [] # data from saved data
    with open(filename) as data:
        reader = csv.reader(data)
        for i in reader:
            a.append(i)

    c_l_alpha_E.delete(0, tk.END)
    c_l_alpha_E.insert(0, a[0][0])


    c_l_zero_E.delete(0, tk.END)
    c_l_zero_E.insert(0, a[0][1])

    c_l_ih_E.delete(0, tk.END)
    c_l_ih_E.insert(0, a[0][2])

    c_l_delta_elevator_E.delete(0, tk.END)
    c_l_delta_elevator_E.insert(0, a[0][3])

    c_m_alpha_E.delete(0, tk.END)
    c_m_alpha_E.insert(0, a[0][4])

    c_m_zero_E.delete(0, tk.END)
    c_m_zero_E.insert(0, a[0][5])

    c_m_ih_E.delete(0, tk.END)
    c_m_ih_E.insert(0, a[0][6])

    c_m_delta_elevator_E.delete(0, tk.END)
    c_m_delta_elevator_E.insert(0, a[0][7])

tk.Button(control_cards, text="load", command=load).grid(row=3, column=0, padx=10, pady=10, sticky=tk.EW)

tk.Button(control_cards, text="save", command=save).grid(row=4, column=0, padx=10, pady=10, sticky=tk.EW)

tk.Button(control_cards, text="make DATCOM file", command=make_datcom).grid(row=5, column=0, padx=10, pady=10, sticky=tk.EW)

tk.Button(trim, text="load data", command=load_trim_data).grid(row=2, column=0, padx=5, pady=5)

tk.Button(trim, text="plot trim diagram", command=plot_trim_data).grid(row=3, column=0, padx=5, pady=5)

tk.Button(trim, text="save trim diagram data", command=save_trim).grid(row=4, column=0, padx=5, pady=5)

tk.Button(trim, text="load trim diagram data", command=load_trim_file).grid(row=5, column=0, padx=5, pady=5)


root.mainloop()
