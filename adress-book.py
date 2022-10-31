# Import library
import tkinter as tk

# Create window
window = tk.Tk()
window.geometry('384x256')
window.resizable(False, False)
window.title('Adress Book')
window.config(bg = 'dark grey')

# Set the contact list
contact_list = []

# Define variables
name = tk.StringVar(value = '')
phone = tk.IntVar(value = '')

# Labels
title = tk.Label(text = 'Adress Book', font = 'verdana 15 bold', fg = 'white', bg = 'brown').pack()
name_label = tk.Label(text = 'Name:', font = 'verdana 10', bg = 'dark grey').place(x = 25, y = 50)
phone_label = tk.Label(text = 'Phone:', font = 'verdana 10', bg = 'dark grey').place(x = 25, y = 75)

# Entries
name_entry = tk.Entry(textvariable = name).place(x = 75, y = 50)
phone_entry = tk.Entry(textvariable = phone).place(x = 75, y = 75)

# Listbox
listbox = tk.Listbox()
listbox.place(x = 225, y = 50)

# Functions
def add():
    contact = (name.get(), phone.get())
    contact_list.append(contact)
    contact_list.sort()
    # Insert name alfabethically
    listbox.insert(contact_list.index(contact), name.get())
    name.set('')
    phone.set('')

def view():
    global contact
    contact = contact_list[listbox.curselection()[0]]
    name.set(contact[0])
    phone.set(contact[1])

def edit():
    global contact
    global contact_list
    listbox.delete(contact_list.index(contact))
    edited_contact = (name.get(), phone.get())
    contact_list = [edited_contact if item == contact else item for item in contact_list]
    contact_list.sort()
    # Replace name in listbox
    listbox.insert(contact_list.index(edited_contact), name.get())

def delete():
    contact = contact_list[listbox.curselection()[0]]
    listbox.delete(contact_list.index(contact))
    contact_list.remove(contact)

# Buttons
add_button = tk.Button(text = 'Add', fg = 'white', bg = 'brown', command = add).place(x = 30, y = 125)
view_button = tk.Button(text = 'View', fg = 'white', bg = 'brown', command = view).place(x = 70, y = 125)
edit_button = tk.Button(text = 'Edit', fg = 'white', bg = 'brown', command = edit).place(x = 110, y = 125)
delete_button = tk.Button(text = 'Delete', fg = 'white', bg = 'brown', command = delete).place(x = 150, y = 125)


window.mainloop()