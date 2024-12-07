import os
import tkinter as tk
from tkinter import filedialog, messagebox

class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic File Explorer")
        self.root.geometry("600x400")

        # Frame for file list
        self.frame = tk.Frame(self.root)
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Listbox to display files and directories
        self.listbox = tk.Listbox(self.frame, height=15, width=50)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        # Bottom frame with buttons
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(fill=tk.X, side=tk.BOTTOM)

        # Open and Delete buttons
        self.open_button = tk.Button(self.bottom_frame, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.bottom_frame, text="Delete", command=self.delete_file)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        # Initialize file explorer
        self.load_directory()

    def load_directory(self):
        # Get the list of files and directories
        current_dir = os.getcwd()
        files_and_dirs = os.listdir(current_dir)
        
        # Clear the listbox and insert new entries
        self.listbox.delete(0, tk.END)
        for entry in files_and_dirs:
            self.listbox.insert(tk.END, entry)

    def open_file(self):
        try:
            selected_item = self.listbox.get(self.listbox.curselection())
            path = os.path.join(os.getcwd(), selected_item)

            # Only open text files
            if os.path.isfile(path) and path.endswith(".txt"):
                with open(path, "r") as file:
                    content = file.read()

                # Display content in a new window
                new_window = tk.Toplevel(self.root)
                new_window.title(f"Opening {selected_item}")
                text_widget = tk.Text(new_window)
                text_widget.pack(fill=tk.BOTH, expand=True)
                text_widget.insert(tk.END, content)

            else:
                messagebox.showwarning("Invalid file", "Please select a valid text file.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def delete_file(self):
        try:
            selected_item = self.listbox.get(self.listbox.curselection())
            path = os.path.join(os.getcwd(), selected_item)

            if os.path.isfile(path):
                os.remove(path)
                self.load_directory()  # Reload directory
            else:
                messagebox.showwarning("Invalid Selection", "Please select a file to delete.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()
