# Password Manager

## Overview

This is a simple password manager application built using Tkinter in Python. It allows users to generate random passwords, save them along with website details, and retrieve passwords when needed.

## Features

1. **Password Generation**: Clicking on the "Generate Password" button will create a strong, random password.

2. **Save Passwords**: Users can input website details, including the website name, email/username, and password. Clicking on the "Add" button will save this information.

3. **Search for Passwords**: Users can search for saved passwords by entering the website name and clicking on the "Search" button.

## How to Use

### 1. Generate Password

- Click on the "Generate Password" button to create a random password.
- The generated password will be automatically copied to the clipboard.

### 2. Save Passwords

- Enter the website name, email/username, and password.
- Click on the "Add" button to save the information.

### 3. Search for Passwords

- Enter the website name in the "Website" field.
- Click on the "Search" button to retrieve the saved email and password for that website.

## Dependencies

- Python 3.x
- Tkinter (for GUI)
- pyperclip (for clipboard functionality)

## How to Run

1. Clone the repository to your local machine.

```bash
git clone https://github.com/your-username/password-manager.git
cd password-manager
```
2. Run the application.

```bash
python password_manager.py
```
## File Structure
- password_manager.py: The main Python script containing the password manager application.
- logo.png: Logo image used in the GUI.
- Data.json: JSON file to store saved password data.
