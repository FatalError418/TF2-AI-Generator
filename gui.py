import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import subprocess
import sys
import webbrowser
import weapongenerator

# Class for creating tooltips for widgets
class Tooltip:
    def __init__(self, widget, text):
        # Constructor of Tooltip class
        self.widget = widget
        self.text = text
        self.tooltip_window = None

        # Bind widget with Enter and Leave events
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

        # If widget is Combobox, bind with additional events
        if isinstance(self.widget, ttk.Combobox):
            self.widget.bind("<<ComboboxSelected>>", self.hide_tooltip)
            self.widget.bind("<FocusOut>", self.hide_tooltip)

    # Function to show tooltip
    def show_tooltip(self, event):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        # Create a new Toplevel window
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)
        self.tooltip_window.wm_geometry(f"+{x}+{y}")

        # Create label in tooltip window
        label = tk.Label(self.tooltip_window, text=self.text, background="#ffffe0", relief="solid", borderwidth=1)
        label.pack()

    # Function to hide tooltip
    def hide_tooltip(self, event):
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

# Function to run weapon generator script
def run_weapon_generator():
    # Get values
    api_key = entry_api_key.get()
    weapon_idea = text_weapon_idea.get("1.0", tk.END).strip()
    class_ = combobox_class.get()
    slot = combobox_slot.get()
    type = entry_type.get()
    power = combobox_power.get()

    try:
        # Call the weapon generation function from weapongenerator module
        result = weapongenerator.create_weapon(api_key=api_key, weapon_idea=weapon_idea, class_=class_, slot=slot, type=type, power=power)
        result_label.config(text="Result: " + result)
    except Exception as e:
        # Update the result_label with error information if any exception is raised
        result_label.config(text="Error: " + str(e) + " Line: " + e.args.line)


# Function to open weapon card creator website in web browser
def open_weapon_card_website(event):
    webbrowser.open("https://gamepro5.com/programs/tf2_weapon_card_creator/")

# Function to clear the value of a Combobox
def clear_combobox(combobox):
    combobox.set('')

# Function to clear the value of an Entry
def clear_entry(entry):
    entry.delete(0, tk.END)

# Function to toggle visibility of API key in Entry
def toggle_visibility():
    if entry_api_key.cget('show') == '':
        entry_api_key.config(show='*')
    else:
        entry_api_key.config(show='')

# Create main Tkinter window
window = tk.Tk()
window.title("TF2 AI Generator")
exe_dir = sys._MEIPASS  # Get the temporary directory path
icon_path = os.path.join(exe_dir, 'tf2_icon.ico')  # Build the absolute path to the icon file
window.iconbitmap(icon_path)
window.resizable(False, False)

notebook = ttk.Notebook(window)
notebook.pack(fill="both", expand=True)

api_key_tab = ttk.Frame(notebook)
notebook.add(api_key_tab, text="API Key")

# Create labels, entry and button for API Key tab
heading_label = tk.Label(api_key_tab, text="API Key", font=("Arial", 16, "bold"))
heading_label.pack()

label_api_key = tk.Label(api_key_tab, text="API Key (Required):")
label_api_key.pack()

entry_api_key = tk.Entry(api_key_tab, show="*")
entry_api_key.pack()

toggle_button = tk.Button(api_key_tab, text='Toggle Visibility', command=toggle_visibility)
toggle_button.pack()

# Create Weapon Generator tab
weapon_generator_tab = ttk.Frame(notebook)
notebook.add(weapon_generator_tab, text="Weapon Generator")

# Create labels, entries, comboboxes and buttons for Weapon Generator tab
heading_label = tk.Label(weapon_generator_tab, text="Weapon Generator", font=("Arial", 16, "bold"))
heading_label.grid(row=0, column=0, columnspan=3)

description_label = tk.Label(weapon_generator_tab, text="Generate custom TF2 weapon cards using ChatGPT!\nClear a value to allow the AI to choose. All values are optional.\nOnce the weapon is generated, go to the TF2 weapon card\ncreator, scroll down to load, and load\nthe newly created '.weaponcard', which is created in the 'weaponcards' folder.\nSort by date to get the newest weapon card.\nIf it doesn't work first try, remember to:\n1. Provide the correct API key, double check it's actually the correct one.\n2. Try regenerating the weapon card, sometimes it doesn't work first time.")
description_label.grid(row=1, column=0, columnspan=3)

# Create hyperlinked label to open weapon card creator website
link_label = tk.Label(weapon_generator_tab, text="Go to the TF2 Weapon Card Creator", fg="blue", cursor="hand2")
link_label.grid(row=2, column=0, columnspan=3)
link_label.bind("<Button-1>", open_weapon_card_website)

# Create widgets for form fields and bind them with clear functions
label_power = tk.Label(weapon_generator_tab, text="Power:")
label_power.grid(row=3, column=0, sticky=tk.W)

combobox_power = ttk.Combobox(weapon_generator_tab, values=["Extremely Weak", "Very Weak", "Weak", "Balanced", "Strong", "OP", "Extremely OP"], state="readonly")
combobox_power.grid(row=3, column=1)
clear_power_button = tk.Button(weapon_generator_tab, text='Clear', command=lambda: clear_combobox(combobox_power))
clear_power_button.grid(row=3, column=2)

# Create widgets for form fields and bind them with clear functions
label_weapon_idea = tk.Label(weapon_generator_tab, text="Weapon Idea:")
label_weapon_idea.grid(row=4, column=0, sticky=tk.W)

text_weapon_idea = tk.Text(weapon_generator_tab, height=5, width=30)
text_weapon_idea.grid(row=4, column=1, pady=5)
clear_weapon_idea_button = tk.Button(weapon_generator_tab, text='Clear', command=lambda: clear_entry(text_weapon_idea))
clear_weapon_idea_button.grid(row=4, column=2)

# Create widgets for form fields and bind them with clear functions
label_class = tk.Label(weapon_generator_tab, text="Class:")
label_class.grid(row=5, column=0, sticky=tk.W)

combobox_class = ttk.Combobox(weapon_generator_tab, values=["Scout", "Soldier", "Pyro", "Demoman", "Heavy", "Engineer", "Medic","Sniper", "Spy"], state="readonly")
combobox_class.grid(row=5, column=1)
clear_class_button = tk.Button(weapon_generator_tab, text='Clear', command=lambda: clear_combobox(combobox_class))
clear_class_button.grid(row=5, column=2)

# Create widgets for form fields and bind them with clear functions
label_slot = tk.Label(weapon_generator_tab, text="Slot:")
label_slot.grid(row=6, column=0, sticky=tk.W)

combobox_slot = ttk.Combobox(weapon_generator_tab, values=["Primary", "Secondary", "Melee", "PDA"], state="readonly")
combobox_slot.grid(row=6, column=1)
clear_slot_button = tk.Button(weapon_generator_tab, text='Clear', command=lambda: clear_combobox(combobox_slot))
clear_slot_button.grid(row=6, column=2)

# Create widgets for form fields and bind them with clear functions
label_type = tk.Label(weapon_generator_tab, text="Type:")
label_type.grid(row=7, column=0, sticky=tk.W)

entry_type = tk.Entry(weapon_generator_tab)
entry_type.grid(row=7, column=1)
clear_type_button = tk.Button(weapon_generator_tab, text='Clear', command=lambda: clear_entry(entry_type))
clear_type_button.grid(row=7, column=2)

# Create 'Run' button which will run weapon generator script
run_button = tk.Button(weapon_generator_tab, text="Generate Weapon Card", command=run_weapon_generator)
run_button.grid(row=8, column=0, columnspan=3)

# Create label for displaying results or error messages
result_label = tk.Label(weapon_generator_tab, text="")
result_label.grid(row=9, column=0, columnspan=3)

# Run the Tkinter main loop
window.mainloop()
