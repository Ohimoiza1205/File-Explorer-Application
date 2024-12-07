# Basic File Explorer App

A simple desktop application built using Python and Tkinter that allows users to navigate local directories, view files, open text files, and delete them. The app features a user-friendly interface with a file list, scrollable view, and basic file management operations like opening and deleting files.

## Features

- **File Navigation**: Browse through files and directories in the current working directory.
- **Open Files**: Open and read `.txt` files in a new window.
- **Delete Files**: Delete selected files from the local directory.
- **User-friendly Interface**: View files in a scrollable list with buttons for interaction.

## Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- Operating System: Windows, macOS, or Linux (any OS with Python and Tkinter support)

## Installation

### Clone the Repository
To get started with the project, first clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/basic-file-explorer.git
cd basic-file-explorer
```

### Install Python and Tkinter
Ensure Python 3.x is installed on your machine. Tkinter should be installed with Python by default, but if it’s not available, you can install it using:

- **Windows**: Tkinter is bundled with Python. If not, install python-tk.
- **macOS/Linux**: Tkinter is usually included by default with Python. If it’s missing, you can install it using the package manager.
```bash
sudo apt-get install python3-tk  # For Linux
brew install python-tk           # For macOS
```

### Run the Application
To run the application, execute the following command from the project directory:
```bash
python file_explorer_app.py
```
This will launch the Basic File Explorer GUI application.

### Usage
- **Navigating Files**: The app will display a list of files and directories from the current working directory.
- **Opening a File**: To open a file, click on the file in the list (must be a .txt file). It will open in a new window displaying the content of the file.
- **Deleting a File**: Select the file from the list and click the "Delete" button to remove the file from your system.
- **Refreshing the File List**: The file list automatically updates when a file is opened or deleted.

### App Overview
**File List**: A scrollable list displays all files and directories in the current directory.
**Buttons**:
- Open: Opens the selected .txt file in a new window.
- Delete: Deletes the selected file from the current directory.
- Error Handling: Includes error handling for invalid file types, empty inputs, and file permissions.

**Code Structure**
- ``file_explorer_app.py``: The main application script, containing the Tkinter interface and file management logic.
- UI Components: Utilizes Tkinter widgets such as Listbox, Button, Scrollbar, and Text to build the GUI.

**File Operations**:
- Opening Files: Uses Python's built-in open() function to read .txt files.
- Deleting Files: Uses os.remove() to delete files from the file system.

### Improvements to Consider
While the application is simple, I still aim to enhance it with additional features such as:

- **Search Functionality**: Add the ability to search for files by name.
- **File Renaming**: Add an option to rename files directly from the GUI.
- **Drag-and-Drop Support**: Allow users to drag and drop files into the file explorer for easier access.
- **File Preview**: Implement a preview window for text files before opening them.
- **File Sorting**: Allow sorting by file name, size, or modification date.
- **Support for Other File Types**: Extend the app to handle other file types (e.g., images, PDFs).

### License
This project is licensed under the MIT License - see the LICENSE file for details.

### Contributions
Contributions are welcome! If you'd like to contribute to the project, please fork the repository, create a feature branch, and submit a pull request.

**Steps to Contribute**:
- Fork the repository
- Create a new branch (``git checkout -b feature-branch``)
- Commit your changes (``git commit -m 'Add new feature'``)
- Push to the branch (``git push origin feature-branch``)
- Create a pull request

### Contact
If you have any questions or suggestions, feel free to reach out:

- Email: omoiza@ttu.edu
- GitHub: @Ohimoiza1205
