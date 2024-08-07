import tkinter as tk
from tkinter import messagebox
import json
import os
import webbrowser

# File to save URLs
filename = 'urls.json'

# Load URLs from file if it exists
if os.path.exists(filename):
    with open(filename, 'r') as file:
        urls = json.load(file)
else:
    # Initial URLs dictionary
    urls = {
        "Work": ["https://www.canva.com/", "https://openai.com/blog/chatgpt/", "https://gemini.google.com/"],
        "Personal": ["https://www.netflix.com/", "https://open.spotify.com/", "https://www.youtube.com/", "https://www.hotstar.com/in/"],
        "Education": ["https://www.coursera.org/", "https://www.udemy.com/"],
        "Social Media": ["https://www.instagram.com/", "https://www.facebook.com/", "https://in.linkedin.com/"],
        "Mails": ["https://mail.google.com/mail/", "https://www.microsoft.com/en-in/microsoft-365/outlook/email-and-calendar-software-microsoft-outlook"]
    }

# Adds Python object in JSON format in the JSON file
def save_urls():
    with open(filename, 'w') as file:
        json.dump(urls, file)

def add_website():
    category = category_var.get()
    new_url = url_entry.get()
    if category in urls:
        urls[category].append(new_url)
        save_urls()
        messagebox.showinfo("Success", f"URL added to {category} category.")
    else:
        messagebox.showerror("Error", f"Category '{category}' not found in urls dictionary.")
    url_entry.delete(0, tk.END)

def open_webpages():
    category = open_category_var.get()
    if category in urls:
        for url in urls[category]:
            webbrowser.open_new_tab(url)
        messagebox.showinfo("Success", f"Opened all URLs in {category} category.")
    else:
        messagebox.showerror("Error", f"Category '{category}' not found in urls dictionary.")

def add_category():
    new_category = category_entry.get()
    if new_category and new_category not in urls:
        urls[new_category] = []
        save_urls()
        category_menu['menu'].add_command(label=new_category, command=tk._setit(category_var, new_category))
        open_category_menu['menu'].add_command(label=new_category, command=tk._setit(open_category_var, new_category))
        messagebox.showinfo("Success", f"Category '{new_category}' added.")
    else:
        messagebox.showerror("Error", "Category is empty or already exists.")
    category_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Manage Website URLs")

# Create and place the category label and dropdown for adding URLs
category_label = tk.Label(root, text="Add URL to Category:")
category_label.grid(row=0, column=0, padx=10, pady=10)
category_var = tk.StringVar(root)
category_var.set("Work") # default value
category_menu = tk.OptionMenu(root, category_var, *urls.keys())
category_menu.grid(row=0, column=1, padx=10, pady=10)

# Create and place the URL entry for adding URLs
url_label = tk.Label(root, text="New URL:")
url_label.grid(row=1, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=1, column=1, padx=10, pady=10)

# Create and place the add button
add_button = tk.Button(root, text="Add URL", command=add_website)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

# Create and place the category label and dropdown for opening URLs
open_category_label = tk.Label(root, text="Open URLs in Category:")
open_category_label.grid(row=3, column=0, padx=10, pady=10)
open_category_var = tk.StringVar(root)
open_category_var.set("Work") # default value
open_category_menu = tk.OptionMenu(root, open_category_var, *urls.keys())
open_category_menu.grid(row=3, column=1, padx=10, pady=10)

# Create and place the open button
open_button = tk.Button(root, text="Open URLs", command=open_webpages)
open_button.grid(row=4, column=0, columnspan=2, pady=10)

# Create and place the category entry and add category button
new_category_label = tk.Label(root, text="New Category:")
new_category_label.grid(row=5, column=0, padx=10, pady=10)
category_entry = tk.Entry(root, width=50)
category_entry.grid(row=5, column=1, padx=10, pady=10)

add_category_button = tk.Button(root, text="Add Category", command=add_category)
add_category_button.grid(row=6, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()

print(urls) # for Terminal view what all URLs are added


