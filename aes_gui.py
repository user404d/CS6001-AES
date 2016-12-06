from tkinter import *
from tkinter import ttk
import helper_functions as helper
import aes_impl as aes
import os
import aes_io

"""
On click functionality of 'Encrypt' button.
"""
def encrypt_click():

    # getting file and path and checking validity
    file_path = path_entry.get();
    if  not os.path.isfile(file_path):
        log_text['state'] = 'normal'
        log_text.insert('end', "Encrypt: File Not Found.")
        log_text['state'] = 'disabled'

    # getting key value from key entry field
    temp = key_entry.get();
    # splitting temp into list, delimitting every 2 characters
    key = [int(temp[i:i+2]) for i in range(0, len(temp), 2)]
    # generating key schedule from converted key
    key_schedule, _ = aes.gen_key_schedule(key)

    aes_io.encrypt_file(key_schedule, file_path)
    log_text['state'] = 'normal'

    log_text['state'] = 'disabled'

"""
On click functionality of 'Dencrypt' button.
"""
def decrypt_click():

    # getting file and path and checking validity
    file_path = path_entry.get();
    if  not os.path.isfile(file_path):
        log_text['state'] = 'normal'
        log_text.insert('end', "Encrypt: File Not Found.")
        log_text['state'] = 'disabled'

    # getting key value from key entry field
    temp = key_entry.get();
    # splitting temp into list, delimitting every 2 characters
    key = [int(temp[i:i+2]) for i in range(0, len(temp), 2)]
    # generating key schedule from converted key
    key_schedule, _ = aes.gen_key_schedule(key)

    aes_io.decrypt_file(key_schedule, file_path, od_entry.get())

    log_text['state'] = 'normal'
    log_text.insert('end', "Decrypt")
    log_text.insert('end', "\n")
    log_text['state'] = 'disabled'

"""
On click functionality of 'Gen. Key' button.
"""
def genkey_click():
    key = helper.generate_random_key(16)

    temp = ""
    for i in key:
        temp += str(i)
    key_entry_text.set(temp)

    log_text['state'] = 'normal'
    log_text.insert('end', "Generate Key")
    log_text.insert('end', "\n")
    log_text['state'] = 'disabled'


# ------------- Graphical User Interface Code ----------- #

# Declaring root Tk object
root = Tk()
root.resizable(0,0) # Prevents resizing window
root.title("AES Encryption App")
root.iconbitmap('aes.ico')

path_entry_text = StringVar()
key_entry_text = StringVar()
out_dir = StringVar()

# Adding frame to root Tk window
mainframe = ttk.Frame(root, padding="5")
# Configuring main frame of the window
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# Causes main frame to resize with window resize
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Frame for file path and key input widgets
fpkframe = ttk.Frame(mainframe)
fpkframe.grid(column=0, row=0, sticky=W)

# Label and text field entry for file path
ttk.Label(fpkframe, text="File Path: ").grid(column=0, row=0, sticky=W)
path_entry = ttk.Entry(fpkframe, width=40, textvariable=path_entry_text)
path_entry.grid(column=1, row=0, sticky=(W,E)) # Stretches entry text field

# Label and text field entry for key
ttk.Label(fpkframe, text="Key: ").grid(column=0, row=1, sticky=E)
key_entry = ttk.Entry(fpkframe, width=40, textvariable=key_entry_text)
key_entry.grid(column=1, row=1, sticky=(E), pady=(10,0))

# Seperator line between fpk and od frames
ttk.Separator(mainframe, orient="horizontal").grid(column=0, row=1, sticky=(E,W))

# Frame for output directory textfield entry
odframe = ttk.Frame(mainframe)
odframe.grid(column=0, row=2, sticky=(E,W))
ttk.Label(odframe, text="Out Directoy: ").grid(column=0, row=0, sticky=W)
od_entry = ttk.Entry(odframe, width=40, textvariable=out_dir)
od_entry.grid(column=0, row=1, sticky=(E,W), padx=(65,0), pady=(5,0))

# Seperator line between od and buttons frames
ttk.Separator(mainframe, orient="horizontal").grid(column=0, row=3, sticky=(E,W))

# Frame for control buttons
buttonsframe = ttk.Frame(mainframe)
buttonsframe.grid(column=0, row=4, sticky=(E, W))
ttk.Button(buttonsframe, text="Encrypt", command=encrypt_click).grid(column=0, row=0, sticky=(E,W), padx=(20,20))
ttk.Button(buttonsframe, text="Decrypt", command=decrypt_click).grid(column=1, row=0, sticky=(E,W), padx=(0,20))
ttk.Button(buttonsframe, text="Gen. Key", command=genkey_click).grid(column=2, row=0, sticky=(E,W))

# Frame for holding log text container
logframe = ttk.Frame(mainframe)
logframe.grid(column=0, row=5, sticky=(E,W))
log_text = Text(logframe, state="disabled", width=40, height=10, wrap='word')
log_text.grid(column=0, row=0, stick=(E,W))

# Adds padding around each frame container within mainframe
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# Main event loop needed to make everything run
root.mainloop()
