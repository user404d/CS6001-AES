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
        log_text.insert('end', "Encrypt: Input File Not Found.\n")
        log_text['state'] = 'disabled'
        
    out_path = od_entry.get()
    out_path = None if out_path == "" else out_path

    # getting key value from key entry field
    temp = key_entry.get();
    # splitting temp into list, delimitting every 2 characters
    key = helper.convert_hex_to_bytes(temp)
    # generating key schedule from converted key
    key_schedule, _ = aes.gen_key_schedule(key)

    if enc_mode.get() == 0:
        aes_io.encrypt_file(key_schedule, file_path, out_path)
    else:
        temp = iv_entry_text.get()
        iv = helper.convert_hex_to_bytes(temp)
        iv = helper.convert_to_state_matrix(iv)
        aes_io.encrypt_file(key_schedule, file_path, out_path, 16, aes.Mode.cbc,
                            iv)

    log_text['state'] = 'normal'
    log_text.insert('end', "Encrypt\n")
    log_text['state'] = 'disabled'

"""
On click functionality of 'Dencrypt' button.
"""
def decrypt_click():

    # getting file and path and checking validity
    file_path = path_entry.get();
    if not os.path.isfile(file_path):
        log_text['state'] = 'normal'
        log_text.insert('end', "Decrypt: Encrypted File Not Found.\n")
        log_text['state'] = 'disabled'
        return

    out_path = od_entry.get()
    out_path = None if out_path == "" else out_path

    # getting key value from key entry field
    temp = key_entry.get();
    # splitting temp into list, delimitting every 2 characters
    key = helper.convert_hex_to_bytes(temp)
    # generating key schedule from converted key
    key_schedule, _ = aes.gen_key_schedule(key)

    if enc_mode.get() == 0:
        aes_io.decrypt_file(key_schedule, file_path, out_path)
    else:
        temp = iv_entry_text.get()
        iv = helper.convert_hex_to_bytes(temp)
        iv = helper.convert_to_state_matrix(iv)
        aes_io.decrypt_file(key_schedule, file_path, out_path, 16, aes.Mode.cbc,
                            iv)

    log_text['state'] = 'normal'
    log_text.insert('end', "Decrypt\n")
    log_text['state'] = 'disabled'

"""
On click functionality of 'Gen. Key' button.
"""
def gen_key_click():
    key_size = key_size_bytes.get()
    key = helper.generate_random_key(key_size)
    
    if len(key) != key_size:
        print(key, key_size)
        log_text['state'] = 'normal'
        log_text.insert('end', "Error in Key Generation\n")
        log_text['state'] = 'disabled'
        return

    key_entry_text.set(helper.convert_bytes_to_hex(key))

    print(key_entry_text.get())

    log_text['state'] = 'normal'
    log_text.insert('end', "Generate Key\n")
    log_text['state'] = 'disabled'

def gen_iv_click():
    iv = helper.initialization_vector()
    
    iv_entry_text.set(helper.convert_bytes_to_hex(iv))

    log_text['state'] = 'normal'
    log_text.insert('end', "Generate Initialization Vector.\n")
    log_text['state'] = 'disabled'

def ecb_mode_select():

    gen_iv_button.config(state='disabled')
    iv_entry.config(state='disabled')
    
    log_text['state'] = 'normal'
    log_text.insert('end', "ECB mode selected\n")
    log_text['state'] = 'disabled'

def cbc_mode_select():

    gen_iv_button.config(state='normal')
    iv_entry.config(state='normal')
    
    log_text['state'] = 'normal'
    log_text.insert('end', "CBC mode selected\n")
    log_text['state'] = 'disabled'


# ------------- Graphical User Interface Code ----------- #

# Declaring root Tk object
root = Tk()
root.resizable(0,0) # Prevents resizing window
root.title("AES Encryption App")
root.iconbitmap('aes.ico')

path_entry_text = StringVar()
key_entry_text = StringVar()
iv_entry_text = StringVar()
out_dir = StringVar()
key_size_bytes = IntVar()
enc_mode = IntVar()

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
ttk.Label(fpkframe, text="File Path: ").grid(column=0, row=0, sticky=E)
path_entry = ttk.Entry(fpkframe, width=40, textvariable=path_entry_text)
path_entry.grid(column=1, row=0, sticky=(W,E)) # Stretches entry text field

# Label for output directory and textfield entry
ttk.Label(fpkframe, text="Out Directoy: ").grid(column=0, row=1, sticky=W)
od_entry = ttk.Entry(fpkframe, width=40, textvariable=out_dir)
od_entry.grid(column=1, row=1, sticky=(E,W), pady=(10,0))

# Seperator line between fpk and od frames
ttk.Separator(mainframe, orient="horizontal").grid(column=0, row=1, sticky=(E,W))

#frame for encryption params
encframe = ttk.Frame(mainframe)
encframe.grid(column=0, row=2, sticky=(E,W))

ttk.Label(encframe, text="Key: ").grid(column=0, row=1, sticky=E)
key_entry = ttk.Entry(encframe, width=40, textvariable=key_entry_text)
key_entry.grid(column=1, row=1, sticky=(E), padx=(11,0), pady=(10,0))

ttk.Label(encframe, text="Initialization\n       Vector: ").grid(column=0, row=2, sticky=E)
iv_entry = ttk.Entry(encframe, width=40, state='disabled', textvariable=iv_entry_text)
iv_entry.grid(column=1, row=2, sticky=(E), padx=(11,0), pady=(10,0))

# Seperator line between od and buttons frames
ttk.Separator(mainframe, orient="horizontal").grid(column=0, row=3, sticky=(E,W))

# Frame for control buttons
buttonsframe = ttk.Frame(mainframe)
buttonsframe.grid(column=0, row=4, sticky=(E, W))
ttk.Button(buttonsframe, text="Encrypt", command=encrypt_click).grid(column=0, row=0, sticky=(E,W), padx=(20,20))
ttk.Button(buttonsframe, text="Decrypt", command=decrypt_click).grid(column=1, row=0, sticky=(E,W), padx=(0,20))
ttk.Button(buttonsframe, text="Gen. Key", command=gen_key_click).grid(column=2, row=0, sticky=(E,W), padx=(0,20))
gen_iv_button = ttk.Button(buttonsframe, text="Gen. IV", state='disabled', command=gen_iv_click)
gen_iv_button.grid(column=3, row=0, sticky=(E,W))

#Frame for holding logging and enc parameter selections
bottomframe = ttk.Frame(mainframe)
bottomframe.grid(column=0, row=5, sticky=(E,W))

# Frame for holding log text container
logframe = ttk.Frame(bottomframe)
logframe.grid(column=0, row=0)
log_text = Text(logframe, state="disabled", width=40, height=10, wrap='word')
log_text.grid(column=0, row=0)

modesframe = ttk.Frame(bottomframe)
modesframe.grid(column=1, row=0, padx=(35,0))
rbs = [ ttk.Radiobutton(modesframe, text='ECB', variable=enc_mode, value=0, command=ecb_mode_select),
        ttk.Radiobutton(modesframe, text='CBC', variable=enc_mode, value=1, command=cbc_mode_select), ]
for i,rb in enumerate(rbs): rb.grid(column=0, row=i)

keysizeframe = ttk.Frame(bottomframe)
keysizeframe.grid(column=2, row=0)
keysizes = [ ttk.Radiobutton(keysizeframe, text='128', variable=key_size_bytes, value=16),
             ttk.Radiobutton(keysizeframe, text='192', variable=key_size_bytes, value=24),
             ttk.Radiobutton(keysizeframe, text='256', variable=key_size_bytes, value=32), ]
for i,keysize in enumerate(keysizes): keysize.grid(column=0, row=i)

# Adds padding around each frame container within mainframe
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

keysizes[0].invoke()
rbs[0].invoke()

# Main event loop needed to make everything run
root.mainloop()
