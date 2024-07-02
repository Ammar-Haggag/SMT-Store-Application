import os
import re
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk
from datetime import datetime  # Import datetime module
from tkinter import filedialog
import pandas as pd
from tkinter import font as tkfont


def open_excel_MPM(): # open excel function 
    # Specify the file path
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\MPM\maintenance MPM.xlsx'
    
    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")

def open_excel_SPI(): # open excel function
    # Specify the file path
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\SPI\Maintenance SPI.xlsx'
    
    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")

def open_excel_FUJI(): # open excel function
    # Specify the file path
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\FUJI\preventive maintenance fuji machines.xlsx'
    
    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")        

def open_excel_OVEN(): # open excel function
    # Specify the file path
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\Oven\preventive maintenance reflow oven.xlsx'
    
    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")

def open_excel_AOI(): # open excel function
    # Specify the file path
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\SPI\Maintenance SPI.xlsx'
    
    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")

def show_message(): #for message of info button
    messagebox.showinfo("Info", "Developed by Eng. Ammar Haggag")

def search_files(directory, pattern): #function search of text in files
    results = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    for line_number, line in enumerate(file, start=1):
                        if re.search(pattern, line):
                            results.append(f'\n Found in file: {file_path} --> line {line_number} \n Part Number  : {line.strip()}\n')
            except UnicodeDecodeError:
                print(f'Error decoding file: {file_path}. Attempting fallback encoding.')

                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        for line_number, line in enumerate(file, start=1):
                            if re.search(pattern, line):
                                results.append(f' Found in file: {file_path} --> line {line_number} \n Part Number  : {line.strip()}\n')
                                
                except (UnicodeDecodeError, OSError):
                    print(f'Error reading file: {file_path}')

    return results

def search_button_click(): 
    global directory_path, result_text

    search_text = search_entry.get().strip()
    if search_text:
        pattern = re.compile(re.escape(search_text), re.IGNORECASE)
        results = search_files(directory_path, pattern)
        if results:
            result_text.config(state=tk.NORMAL)
            result_text.delete('1.0', tk.END)
            for result in results:
                result_text.insert(tk.END, result + '\n')
            result_text.config(state=tk.DISABLED)
        else:
            messagebox.showinfo('Search Results', 'No matching results found.')
    else:
        messagebox.showwarning('Search Text Required', 'Please enter text to search.')

def clear_results():
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.config(state=tk.DISABLED)

def search_file_by_name(): #function search for  vacation date
    file_name = file_name_entry.get().strip()
    if file_name:
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        file_path = os.path.join(vacation_directory_path, file_name)
        print(f"Searching for file: {file_path}")
        if os.path.exists(file_path):
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    file_content = file.read()
                file_content_text.config(state=tk.NORMAL)
                file_content_text.delete('1.0', tk.END)
                file_content_text.insert(tk.END, file_content)
                file_content_text.config(state=tk.DISABLED)
            except Exception as e:
                messagebox.showerror("Error", f"Error reading file: {e}")
        else:
            messagebox.showinfo('File Not Found', f'The specified file does not exist: {file_path}')
    else:
        messagebox.showwarning('File Name Required', 'Please enter the name of the file.')

def create_gui():
    global directory_path, vacation_directory_path, search_entry, result_text, file_name_entry, file_content_text

    window = tk.Tk()
    window.title('Amer Group SMT Store')

    # --------------------------------------------------------------------------------------------------------- # 

    # Create a Tab Control
    tab_control = ttk.Notebook(window)
    tab_control.pack(expand=1, fill='both')

    # --------------------------------------------------------------------------------------------------------- #

    # Tab 1: Search in Files
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Search in Files')

    # Search Label and Entry
    search_label = tk.Label(tab1, text='Enter text to search:')
    search_label.pack(pady=10)
    search_entry = tk.Entry(tab1, width=50)
    search_entry.pack(pady=5)

    # Search Button
    search_button = tk.Button(tab1, text='Search', command=search_button_click)
    search_button.pack(pady=10)

    # Clear Results Button
    clear_button = tk.Button(tab1, text='Clear Results', command=clear_results)
    clear_button.pack(pady=10)

    # Results Text Box
    result_text = scrolledtext.ScrolledText(tab1, width=100, height=20, wrap=tk.WORD)
    result_text.pack(padx=10, pady=10)
    result_text.config(state=tk.DISABLED)

    # info button
    button = tk.Button(tab1, text="Info", command=show_message,bg="gainsboro")
    button.pack(pady=20)
    button.place(x=790, y=10)

    # Load and display image
    try:
        img = Image.open(r'D:\SMT\projects\DATA BASE\logo\logo.png')  # Replace with your image file location
        img = img.resize((80, 80))  # Resize the image as needed
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(tab1, image=img)
        img_label.image = img  # Keep a reference to the image object
        img_label.pack(pady=10)
    except IOError as e:
        print(f'Error loading image: {e}')

    # --------------------------------------------------------------------------------------------------------- #

    # Tab 2: Select Names using Checkboxes
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Workers')

    names = ['Mohamed Ibrahim', 'Hossam Gamal ', 'Mohamed Shokry', 'Moamen Saber', 'Ahmed Hassan', 'Ahmed Ramdan', 'Ayman Shokry', 'Mohamed Abdelmoam', 'Youssef Elsayed']
    statuses = ['Attend','Absence','Vacation', 'Casual vacation' ,'Vacation without salary']
    selected_statuses = {name: tk.StringVar() for name in names}

    def Workers_Vacation():
        current_date = datetime.now().strftime('%d-%m-%Y')
        file_name = f'{current_date}.txt'
        
        # Specify the directory where you want to save the file
        save_path = r'D:\SMT\projects\DATA BASE\Vacation'  # Replace with your desired path
        
        # Combine the directory path and file name
        full_path = os.path.join(save_path, file_name)
        
        with open(full_path, 'w') as file:
            for name in names:
                status = selected_statuses[name].get()
                file.write(f"{name}: {status}\n")
        print(f"Names status saved to {full_path}")

    # Header labels
    tk.Label(tab2, text="Name", font=('Arial', 10, 'bold')).grid(row=0, column=0, padx=10, pady=5)
    for col, status in enumerate(statuses, 1):
        tk.Label(tab2, text=status, font=('Arial', 10, 'bold')).grid(row=0, column=col, padx=10, pady=5)

    for row, name in enumerate(names, 1):
        tk.Label(tab2, text=name, font=('Arial', 10)).grid(row=row, column=0, padx=10, pady=5)
        for col, status in enumerate(statuses, 1):
            tk.Radiobutton(tab2, variable=selected_statuses[name], value=status).grid(row=row, column=col, padx=5, pady=5)
        selected_statuses[name].set(statuses[0])  # Set default status to 'attend'

    # Save Button
    save_button = tk.Button(tab2, text='Save Vacation', command=Workers_Vacation,bg="limegreen")
    save_button.grid(row=len(names) + 1, column=0, columnspan=len(statuses) + 1, pady=10)

    # File name entry
    file_name_label = tk.Label(tab2, text="File Name:")
    file_name_label.grid(row=len(names) + 2, column=0, padx=10, pady=5, sticky='e')
    file_name_entry = tk.Entry(tab2, width=45)
    file_name_entry.grid(row=len(names) + 2, column=1, padx=10, pady=5, columnspan=3)

    # Search file button
    search_file_button = tk.Button(tab2, text="Search", command=search_file_by_name)
    search_file_button.grid(row=len(names) + 2, column=4, padx=10, pady=5)

    # File content text box
    file_content_text = scrolledtext.ScrolledText(tab2, width=100, height=10, wrap=tk.WORD)
    file_content_text.grid(row=len(names) + 3, column=0, columnspan=6, padx=10, pady=10)
    file_content_text.config(state=tk.DISABLED)

    button_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

# --------------------------------------------------------------------------------------------------------- #

    # Tab 3: maintaince files
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text='Maintaince')


    #  Button for MPM
    MPM_button = tk.Button(tab3, text='MPM',command=open_excel_MPM,font=button_font,bg="darkturquoise")
    MPM_button.pack(pady=20)
    MPM_button.config(width=20, height=3)

    #  Button for SPI
    SPI_button = tk.Button(tab3, text='SPI', command=open_excel_SPI,font=button_font,bg="darkturquoise")
    SPI_button.pack(pady=20)
    SPI_button.config(width=20, height=3)

    #  Button for FUJI
    FUJI_button = tk.Button(tab3, text='FUJI',command=open_excel_FUJI,font=button_font,bg="darkturquoise")
    FUJI_button.pack(pady=20)
    FUJI_button.config(width=20, height=3)

    #  Button for OVEN
    OVEN_button = tk.Button(tab3, text='OVEN',command=open_excel_OVEN,font=button_font,bg="darkturquoise")
    OVEN_button.pack(pady=20)
    OVEN_button.config(width=20, height=3)

    #  Button for AOI
    AOI_button = tk.Button(tab3, text='AOI',command=open_excel_AOI,font=button_font,bg="darkturquoise")
    AOI_button.pack(pady=20)
    AOI_button.config(width=20, height=3)
    

    # Define the directory path
    directory_path = r'D:\SMT\projects\DATA BASE\Store'  # Replace with your data base location
    vacation_directory_path = r'D:\SMT\projects\DATA BASE\Vacation'  # Replace with your vacation data base location

    window.mainloop()

if __name__ == '__main__':
    create_gui()