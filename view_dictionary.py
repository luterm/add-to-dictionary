import tkinter as tk
   from tkinter import ttk
   import os

   # Define the dictionary file path
   dictionary_path = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/personal_dictionary.txt")

   # Create the main window
   root = tk.Tk()
   root.title("Dictionary Viewer")

   # Create a treeview for the table
   tree = ttk.Treeview(root, columns=("English", "Polish"), show="headings")
   tree.heading("English", text="English")
   tree.heading("Polish", text="Polish")
   tree.pack(padx=10, pady=10)

   # Read and display dictionary entries
   try:
       if os.path.exists(dictionary_path):
           with open(dictionary_path, 'r', encoding='utf-8') as f:
               for line in f:
                   if line.strip():
                       english, polish = line.strip().split(": ", 1)
                       tree.insert("", "end", values=(english, polish))
       else:
           tk.Label(root, text="Dictionary file not found").pack()
   except Exception as e:
       tk.Label(root, text=f"Error reading dictionary: {e}").pack()

   # Start the main loop
   root.mainloop()