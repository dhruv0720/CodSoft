import customtkinter as ctk
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


def refresh_list():
    contact_list.delete("0.0", "end")

    for contact in contacts:
        contact_list.insert(
            "end",
            f"{contact['name']} | {contact['phone']}\n"
        )


def add_contact():
    contact = {
        "name": name_entry.get(),
        "phone": phone_entry.get(),
        "email": email_entry.get(),
        "address": address_entry.get()
    }

    contacts.append(contact)
    save_contacts()
    refresh_list()
    clear_fields()


def search_contact():
    keyword = search_entry.get().lower()

    contact_list.delete("0.0", "end")

    for contact in contacts:
        if keyword in contact["name"].lower() or keyword in contact["phone"]:
            contact_list.insert(
                "end",
                f"Name: {contact['name']}\n"
                f"Phone: {contact['phone']}\n"
                f"Email: {contact['email']}\n"
                f"Address: {contact['address']}\n\n"
            )


def delete_contact():
    selected_name = name_entry.get()

    global contacts

    contacts = [
        contact for contact in contacts
        if contact["name"] != selected_name
    ]

    save_contacts()
    refresh_list()
    clear_fields()


def update_contact():
    selected_name = name_entry.get()

    for contact in contacts:
        if contact["name"] == selected_name:
            contact["phone"] = phone_entry.get()
            contact["email"] = email_entry.get()
            contact["address"] = address_entry.get()

    save_contacts()
    refresh_list()


def clear_fields():
    name_entry.delete(0, "end")
    phone_entry.delete(0, "end")
    email_entry.delete(0, "end")
    address_entry.delete(0, "end")


# Main Window
root = ctk.CTk()
root.title("Contact Management System")
root.geometry("900x600")

contacts = load_contacts()

title = ctk.CTkLabel(
    root,
    text="📞 Contact Management System",
    font=("Arial", 24, "bold")
)
title.pack(pady=10)

# Search
search_frame = ctk.CTkFrame(root)
search_frame.pack(fill="x", padx=20, pady=10)

search_entry = ctk.CTkEntry(
    search_frame,
    placeholder_text="Search by Name or Phone"
)
search_entry.pack(side="left", padx=10, pady=10, expand=True, fill="x")

ctk.CTkButton(
    search_frame,
    text="Search",
    command=search_contact
).pack(side="left", padx=10)

# Form
form_frame = ctk.CTkFrame(root)
form_frame.pack(fill="x", padx=20)

name_entry = ctk.CTkEntry(form_frame, placeholder_text="Name")
name_entry.pack(padx=10, pady=5, fill="x")

phone_entry = ctk.CTkEntry(form_frame, placeholder_text="Phone Number")
phone_entry.pack(padx=10, pady=5, fill="x")

email_entry = ctk.CTkEntry(form_frame, placeholder_text="Email")
email_entry.pack(padx=10, pady=5, fill="x")

address_entry = ctk.CTkEntry(form_frame, placeholder_text="Address")
address_entry.pack(padx=10, pady=5, fill="x")

# Buttons
button_frame = ctk.CTkFrame(root)
button_frame.pack(pady=10)

ctk.CTkButton(
    button_frame,
    text="Add Contact",
    command=add_contact
).grid(row=0, column=0, padx=10)

ctk.CTkButton(
    button_frame,
    text="Update Contact",
    command=update_contact
).grid(row=0, column=1, padx=10)

ctk.CTkButton(
    button_frame,
    text="Delete Contact",
    command=delete_contact
).grid(row=0, column=2, padx=10)

# Contact List
contact_list = ctk.CTkTextbox(root, height=250)
contact_list.pack(fill="both", expand=True, padx=20, pady=10)

refresh_list()

root.mainloop()