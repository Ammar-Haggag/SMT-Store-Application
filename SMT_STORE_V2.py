import tkinter as tk
from tkinter import Scrollbar, Text, ttk, messagebox, scrolledtext ,Listbox
from PIL import Image, ImageTk
import os
import re
import pandas as pd
from tkinter import filedialog
from datetime import datetime
from tkinter import font as tkfont


def open_excel_MPM(): # function for open MPM Excel file
    # open excel function
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\MPM\maintenance MPM.xlsx'

    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")


def open_excel_SPI(): # function for open SPI Excel file
    # open excel function
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\SPI\Maintenance SPI.xlsx'

    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")


def open_excel_FUJI(): # function for open FUJI Excel file
    # open excel function
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\FUJI\preventive maintenance fuji machines.xlsx'

    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")


def open_excel_OVEN(): # function for open OVEN Excel file
    # open excel function
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\Oven\preventive maintenance reflow oven.xlsx'

    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")

 
def open_excel_AOI(): # function for open AOI Excel file
    # open excel function
    file_path = r'D:\SMT\projects\DATA BASE\MAINTENANCE\SPI\Maintenance SPI.xlsx'

    try:
        # Open the Excel file in the default application
        os.startfile(file_path)
    except Exception as e:
        print(f"Error opening the Excel file: {e}")


def check_password(evevnt=None): # Password function
    if password_entry.get() == "SMT123":  # change your password from here
        password_frame.pack_forget()
        main_frame.pack(expand=1, fill='both')
    else:
        messagebox.showerror("Error", "Incorrect Password")


def show_message(): #when click info button
    messagebox.showinfo("Info", "Developed by Eng. Ammar Haggag")


def search_files(directory, pattern): # search funtion in files
    results = []
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            try:
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    for line_number, line in enumerate(file, start=1):
                        if re.search(pattern, line):
                            results.append(
                                f'\n Found in file: {file_path} --> line {line_number} \n Part Number  : {line.strip()}\n')
            except UnicodeDecodeError:
                print(f'Error decoding file: {file_path}. Attempting fallback encoding.')

                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                        for line_number, line in enumerate(file, start=1):
                            if re.search(pattern, line):
                                results.append(
                                    f' Found in file: {file_path} --> line {line_number} \n Part Number  : {line.strip()}\n')

                except (UnicodeDecodeError, OSError):
                    print(f'Error reading file: {file_path}')

    return results


def search_button_click(event=None): #when i click search button in tab 1
    global directory_path, result_text
    global password_entry, main_frame, password_frame

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


def clear_results(): # function to clear result of search
    result_text.config(state=tk.NORMAL)
    result_text.delete('1.0', tk.END)
    result_text.config(state=tk.DISABLED)



def create_gui(): #variables
    global directory_path, vacation_directory_path, search_entry, result_text, file_name_entry, file_content_text
    global password_entry, main_frame, password_frame

    window = tk.Tk()
    window.title('Amer Group SMT Store')


    # PASSWORD FRAME
    password_frame = tk.Frame(window)
    password_frame.pack(pady=20)

    password_label = tk.Label(password_frame, text="Enter Password:")
    password_label.grid(row=0, column=0, padx=5, pady=5)

    

    password_entry = tk.Entry(password_frame, show='*')
    password_entry.grid(row=1, column=0, padx=5, pady=5)
    password_entry.bind("<Return>", check_password)  # Bind Enter key to search_files function

    password_button = tk.Button(password_frame, text="Submit", command=check_password,bg='GRAY',fg='WHITE')
    password_button.grid(row=2, column=0, padx=5, pady=5)

    main_frame = tk.Frame(window)

#------------------------------------------------------------------------------------------------

    # FOR CREATE TABS
    tab_control = ttk.Notebook(main_frame)
    tab_control.pack(expand=1, fill='both')

# --------------------------------------------------------------------------------------------------------- #

    # Tab 1: Search in Files
    tab1 = ttk.Frame(tab_control)
    tab_control.add(tab1, text='Search at Store')

    # Search Label and Entry
    search_label = tk.Label(tab1, text='Enter text to search:')
    search_label.pack(pady=10)
    search_entry = tk.Entry(tab1, width=50)
    search_entry.pack(pady=5)
    search_entry.bind("<Return>", search_button_click)  # Bind Enter key to search_files function

    # Search Button
    search_button = tk.Button(tab1, text='Search', command=search_button_click,bg='LIGHTBLUE',font=("Helvetica", 10, "bold"))
    search_button.pack(pady=10)

    # Clear Results Button
    clear_button = tk.Button(tab1, text='Clear Results', command=clear_results,font=("Helvetica", 10, "bold"))
    clear_button.pack(pady=10)

    # Results Text Box
    result_text = scrolledtext.ScrolledText(tab1, width=100, height=20, wrap=tk.WORD)
    result_text.pack(padx=10, pady=10)
    result_text.config(state=tk.DISABLED)

    # Info button
    button = tk.Button(tab1, text="Info", command=show_message, bg='#24a0ed',fg='black',font=("Helvetica", 10, "bold"))
    button.pack(pady=20)
    button.place(relx=1.0, rely=0, anchor=tk.NE, x=-10, y=5)
    # Load and display image (optional)
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

    # Tab 2: Workers
    tab2 = ttk.Frame(tab_control)
    tab_control.add(tab2, text='Workers')

    # Headers for Workers tab
    header_name = tk.Label(tab2, text="Name", font=("Helvetica", 12, "bold"))
    header_name.grid(row=0, column=2, padx=10, pady=5)

    header_status = tk.Label(tab2, text="Status", font=("Helvetica", 12, "bold"))
    header_status.grid(row=0, column=3, padx=10, pady=5)

    header_credits = tk.Label(tab2, text="Credits", font=("Helvetica", 12, "bold"))
    header_credits.grid(row=0, column=4, padx=10, pady=5)

    # Initialize and display the Vacation_Class for managing workers
    class Vacation_Class:
        def __init__(self, parent):
            self.parent = parent

            self.workers = [
                {"name": "Mohamed Ibrahim", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")},
                {"name": "Hossam Gamal", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")},
                {"name": "Mohamed Abdelmoneam", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")},
                {"name": "Mohamed Shokry", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")},
                {"name": "Ayman Shokry", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")},
                {"name": "Moamen Saber", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")},
                {"name": "Ahmed Hassan", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")},
                {"name": "Ahmed Ramdan", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")},
                {"name": "Youssef Elsayed", "annual": 5, "casual": 5, "status": tk.StringVar(value="Attend")}
            ]

            self.load_last_saved_files()
            self.create_widgets()

        def create_widgets(self):
            self.labels = []
            for i, worker in enumerate(self.workers):
                label = tk.Label(self.parent, text=worker['name'],font=("Helvetica", 12))
                label.grid(row=i + 1, column=2, padx=10, pady=5)
                self.labels.append(label)

                status_menu = tk.OptionMenu(self.parent, worker['status'], "Attend", "Absence",
                                            "Annual Vacation", "Casual Vacation", "Vacation without salary","Health","Half day")
                status_menu.grid(row=i + 1, column=3, padx=10, pady=5)
                status_menu.config(bg="SKYBLUE", fg="black")
                status_menu['menu'].config(bg="black",fg="white")

                credits_label = tk.Label(self.parent, text=f"Annual: {worker['annual']}, Casual: {worker['casual']}",font=("Helvetica", 10))
                credits_label.grid(row=i + 1, column=4, padx=10, pady=5)
                self.labels.append(credits_label)

            self.filename_entry = tk.Entry(self.parent)
            self.filename_entry.grid(row=len(self.workers) + 1, column=3, padx=30, pady=2)

            label_save = tk.Label(tab2, text="Enter Date :")
            label_save.grid(row=len(self.workers) + 1, column=2)

            save_button = tk.Button(self.parent, text="Save Data", command=self.save_data,bg='green',fg='white',font=("Helvetica", 10, "bold"))
            save_button.grid(row=len(self.workers) + 1, column=4, padx=10, pady=5)

        def load_last_saved_files(self):
            vacation_directory = r'D:\SMT\projects\DATA BASE\Vacation'
            vacation_data_path = os.path.join(vacation_directory, "vacation_credits.txt")

            if os.path.exists(vacation_data_path):
                with open(vacation_data_path, "r") as file:
                    for line in file:
                        parts = line.strip().split(',')
                        if len(parts) == 3:
                            name, annual, casual = parts
                            for worker in self.workers:
                                if worker['name'] == name:
                                    worker['annual'] = int(annual)
                                    worker['casual'] = int(casual)
                                    break

        def save_data(self):
            filename = self.filename_entry.get().strip()
            if not filename:
                messagebox.showerror("Error", "Please enter a valid filename.")
                return

            if not filename.endswith(".txt"):
                filename += ".txt"

            vacation_directory = r'D:\SMT\projects\DATA BASE\Vacation'
            status_filename = os.path.join(vacation_directory, filename)
            credits_filename = os.path.join(vacation_directory, "vacation_credits.txt")

            with open(status_filename, "w") as status_file, open(credits_filename, "w") as credits_file:
                for worker in self.workers:
                    status = worker["status"].get()
                    if status == "Annual Vacation":
                        worker['annual'] -= 1
                    elif status == "Casual Vacation":
                        worker['casual'] -= 1

                    status_file.write(f"{worker['name']},{worker['annual']},{worker['casual']},{status}\n")
                    credits_file.write(f"{worker['name']},{worker['annual']},{worker['casual']}\n")

            # Update labels with new credit values
            for i, worker in enumerate(self.workers):
                self.labels[i * 2 + 1].config(text=f"Annual: {worker['annual']}, Casual: {worker['casual']}")

            messagebox.showinfo("Success", f"Data saved successfully in {status_filename} and {credits_filename}")

    Vacation_Class(tab2)

    #--- END OF CLASS ---#
    
# --------------------------------------------------------------------------------------------------------- #
    # Function to search for string in files (case insensitive)
    def search_files(directory, search_string):
        results = []
        try:
            for root, _, files in os.walk(directory):
                for file in files:
                    if file.endswith('.txt'):  # Adjust file type if needed
                        filepath = os.path.join(root, file)
                        with open(filepath, 'r', encoding='utf-8') as f:
                            for line in f:
                                if search_string.lower() in line.lower():  # Case insensitive check
                                    results.append(f'{filepath}: {line.strip()}')
        except Exception as e:
            messagebox.showerror("Error", f"Error searching files: {e}")
        
        return results

    # Function to handle search button click
    def search_button_click_name(event=None):
        search_string = Entry_Text.get()
        if not search_string:
            messagebox.showwarning("Warning", "Please enter a search string.")
            return
        
        # Clear previous results
        text_results.delete('1.0', tk.END)
        
        # Perform case insensitive search
        results = search_files(vacation_directory_path, search_string)
        
        # Display results
        for result in results:
            text_results.insert(tk.END, result + '\n')



    label_search_name = tk.Label(tab2, text="Enter search Name:")
    label_search_name.grid(row=12, column=2)

    Entry_Text = tk.Entry(tab2, width=30)
    Entry_Text.grid(row=12, column=3)
    Entry_Text.bind("<Return>", search_button_click_name)

    button_search_name = tk.Button(tab2, text="Search", command=search_button_click_name,bg='white',fg='black',font=("Helvetica", 8, "bold"))
    button_search_name.grid(row=12, column=4)

    text_results = Text(tab2, wrap=tk.WORD)
    text_results.grid(row=13, column=3, columnspan=1, sticky='nsew')
    
    


    scrollbar_results = Scrollbar(tab2, command=text_results.yview)
    scrollbar_results.grid(row=13, column=5, sticky='ns')
    
    text_results.config(yscrollcommand=scrollbar_results.set)
    
    # Make sure the grid configuration allows resizing
    tab2.grid_rowconfigure(13, weight=1)
    tab2.grid_columnconfigure(3, weight=1)
    

# --------------------------------------------------------------------------------------------------------- #

    # Tab 3: Excel Sheet Viewer
    tab3 = ttk.Frame(tab_control)
    tab_control.add(tab3, text='Maintenance')

    # Labels
    label = tk.Label(tab3, text="Welcome to the SMT Maintenance Viewer", font=("Helvetica", 14))
    label.pack(pady=10)

    label_instruction = tk.Label(tab3, text="Click a button to open the Machine's Maintenance file:")
    label_instruction.pack(pady=10)

    # MPM Button
    button_MPM = tk.Button(tab3, text=" MPM ",  font=("Helvetica", 16, "bold") ,command=open_excel_MPM, height=3, width=20, bg="dodgerblue")
    button_MPM.pack(pady=5)

    # SPI Button
    button_SPI = tk.Button(tab3, text=" SPI ", font=("Helvetica", 16, "bold") ,command=open_excel_SPI, height=3, width=20, bg="dodgerblue")
    button_SPI.pack(pady=5)

    # FUJI Button
    button_FUJI = tk.Button(tab3, text=" FUJI ", font=("Helvetica", 16, "bold"),command=open_excel_FUJI, height=3, width=20, bg="dodgerblue")
    button_FUJI.pack(pady=5)

    # OVEN Button
    button_OVEN = tk.Button(tab3, text=" OVEN ",font=("Helvetica", 16, "bold") ,command=open_excel_OVEN, height=3, width=20, bg="dodgerblue")
    button_OVEN.pack(pady=5)

    # AOI Button
    button_AOI = tk.Button(tab3, text=" AOI ", font=("Helvetica", 16, "bold") ,command=open_excel_AOI, height=3, width=20, bg="dodgerblue")
    button_AOI.pack(pady=5)

# --------------------------------------------------------------------------------------------------------- #

    directory_path = r'D:\SMT\projects\DATA BASE\Store'
    vacation_directory_path = r'D:\SMT\projects\DATA BASE\Vacation'

    window.mainloop()


if __name__ == '__main__':
    create_gui()
