import os
import re
import tkinter as tk
from tkinter import messagebox, scrolledtext
from PIL import Image, ImageTk  # Import PIL for image handling

def show_message():
    messagebox.showinfo("Info", "Developed by Eng. Ammar Haggag")

def search_files(directory, pattern):
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
        pattern = re.compile(re.escape(search_text),re.IGNORECASE)
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

def create_gui():
    global directory_path, search_entry, result_text

    window = tk.Tk()
    window.geometry('800x600')
    window.title('Amer Group SMT Store')

    # Define the directory path
    directory_path = r'D:\SMT\projects\DATA BASE' # replace (path) with your data base location

    # Search Label and Entry
    search_label = tk.Label(window, text='Enter text to search:')
    search_label.pack(pady=10)
    search_entry = tk.Entry(window, width=50)
    search_entry.pack(pady=5)

    # Search Button
    search_button = tk.Button(window, text='Search', command=search_button_click)
    search_button.pack(pady=10)

    # Clear Results Button
    clear_button = tk.Button(window, text='Clear Results', command=clear_results)
    clear_button.pack(pady=10)

    # Results Text Box
    result_text = scrolledtext.ScrolledText(window, width=100, height=20, wrap=tk.WORD)
    result_text.pack(padx=10, pady=10)
    result_text.config(state=tk.DISABLED)

     # Name Label
    #name_label = tk.Label(window, text='By : Eng. Ammar Haggag', font=('Helvetica', 10, 'bold'))
    #name_label.pack(pady=10)
    #name_label.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # info button
    button = tk.Button(window, text="Info", command=show_message)
    button.pack(pady=20) 
    button.place(x=10, y=10) 
    
    


    # Load and display image
    try:
        img = Image.open(r'D:\SMT\projects\DATA BASE\logo\logo.png') # Replace (Path) with your image file location
        img = img.resize((80, 80))  # Resize the image as needed
        img = ImageTk.PhotoImage(img)
        img_label = tk.Label(window, image=img)
        img_label.image = img  # Keep a reference to the image object
        img_label.pack(pady=10)
    except IOError as e:
        print(f'Error loading image: {e}')

    window.mainloop()

if __name__ == '__main__':
    create_gui()