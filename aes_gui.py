from tkinter import *
from tkinter import ttk
import helper_functions as helper
import aes_impl as aes
import os
import aes_io
import json

def log(msg):
    log_text['state'] = 'normal'
    log_text.insert('end', msg + "\n")
    log_text.see('end')
    log_text['state'] = 'disabled'

def get_key_schedule(key_as_str):
    key = helper.convert_hex_to_bytes(key_as_str)
    return aes.gen_key_schedule(key)

def get_iv(iv_as_str):
    iv = helper.convert_hex_to_bytes(iv_as_str)
    return helper.convert_to_state_matrix(iv)

"""
On click functionality of 'Encrypt' button.
"""
def encrypt_click():

    # getting file and path and checking validity
    file_path = path_entry.get();
    if not os.path.isfile(file_path):
        log("Encryption: '{}' not found.".format(file_path))
        return
        
    out_path = od_entry.get()
    out_path = None if out_path == "" else out_path

    if key_entry.get() == "":
        gen_key_click()

    if iv_entry.get() == "" and enc_mode.get() == 1:
        gen_iv_click()

    if config_enabled.get():
        if config_entry.get() == "":
            config_entry_text.set(file_path + ".conf")
            if not write_config(): return
        if not read_config(): return

    key_schedule = get_key_schedule(key_entry.get())

    if enc_mode.get() == 0:
        log("Encrypt: {}, {}, ECB, {}, {}"
            .format(file_path, out_path,
                    4*len(key_entry.get()), key_entry.get()))
        out_file = aes_io.encrypt_file(key_schedule, file_path, out_path)
    else:
        iv = get_iv(iv_entry.get())
        log("Encrypt: {}, {}, CBC, {}, {}, {}"
            .format(file_path, out_path,
                    4*len(key_entry.get()), key_entry.get(),
                    iv_entry.get()))
        out_file = aes_io.encrypt_file(key_schedule, file_path, out_path, 16, aes.Mode.cbc,
                            iv)

    log("Encrypt: Encrypted {} as {}".format(file_path, out_file))

"""
On click functionality of 'Decrypt' button.
"""
def decrypt_click():
    # getting file and path and checking validity
    file_path = path_entry.get();
    if not os.path.isfile(file_path):
        log("Decrypt: '{}' not found.".format(file_path))
        return

    out_path = od_entry.get()
    out_path = None if out_path == "" else out_path

    if config_enabled.get():
        if config_entry.get() == "":
            config_entry_text.set(file_path + ".conf")
            if not write_config(): return
        if not read_config(): return
    elif key_entry.get() == "":
        log("Decrypt: Empty key.")
        return
    elif iv_entry.get() == "" and enc_mode.get() == 1:
        log("Decrypt: Empty IV.")
        return

    key_schedule = get_key_schedule(key_entry.get())

    if enc_mode.get() == 0:
        log("Decrypt: {}, {}, ECB, {}, {}"
            .format(file_path, out_path,
                    4*len(key_entry.get()), key_entry.get()))
        out_file = aes_io.decrypt_file(key_schedule, file_path, out_path)
    else:
        iv = get_iv(iv_entry.get())
        log("Decrypt: {}, {}, CBC, {}, {}, {}"
            .format(file_path, out_path,
                    4*len(key_entry.get()), key_entry.get(),
                    iv_entry.get()))
        out_file = aes_io.decrypt_file(key_schedule, file_path, out_path, 16, aes.Mode.cbc,
                            iv)

    log("Decrypt: Decrypted {} as {}".format(file_path, out_file))

"""
Config Checkbox Select Event
"""
def enable_config():
    if config_enabled.get():
        key_entry['state'] = 'disabled'
        iv_entry['state'] = 'disabled'
        log("Config: Enabled.")
    else:
        key_entry['state'] = 'normal'
        if enc_mode.get() == 1:
            iv_entry['state'] = 'normal'
        log("Config: Disabled.")

"""
Write Config File
"""
def write_config():
    config_path = config_entry_text.get()
    if os.path.isfile(config_path):
        log("Config: Error {} already exists.".format(config_path))
        return False

    config = {'mode': "ecb", 'key-size': key_size_bytes.get()}

    if key_entry_text.get().strip() == "":
        log("Config: Error key is empty.")
        return False
    else:
        config['key'] = key_entry_text.get()

    if enc_mode.get() == 1:
        config['mode'] = "cbc"

        if iv_entry_text.get().strip() == "":
            log("Config: Error IV is empty.")
            return False
        else:
            config['iv'] = iv_entry_text.get()

    try:
        with open(config_path, 'w') as out:
            json.dump(config, out)
    except IOError as error:
        log("Config: Error writing {}.".format(config_path))
        log("Config: IO {}".format(error))
        return False
    except:
        log("Config: Unhandled error.")
        raise

    log("Config: '{}' written.".format(config_path))
    return True

"""
Read Config File
"""
def read_config():
    config_path = config_entry_text.get()
    if not os.path.isfile(config_path):
        log("Config: Error {} not found.".format(config_path))
        return False

    config = {}

    try:
        with open(config_path, 'r') as fin:
            config = json.load(fin)
    except IOError as error:
        log("Config: Error reading {}.".format(config_path))
        log("Config: IO {}".format(error))
        return False
    except:
        log("Config: Unhandled error.")
        raise

    key = config.get('key', "")
    iv = config.get('iv', "")
    mode = config.get('mode', "ecb")
    key_size = config.get('key-size', 16)

    key_entry_text.set(key)
    iv_entry_text.set(iv)

    modes[0 if mode == "ecb" else 1].invoke()

    if key_size == 16:
        keysizes[0].invoke()
    elif key_size == 24:
        keysizes[1].invoke()
    else:
        keysizes[2].invoke()

    log("Config: '{}' loaded.".format(config_path))
    return True


"""
On click functionality of 'Gen. Key' button.
"""
def gen_key_click():
    key_size = key_size_bytes.get()
    key = helper.generate_random_key(key_size)
    
    if len(key) != key_size:
        log("Gen Key: Wrong key size. ({}, {} =/= {})"
            .format(key, len(key), key_size))
        return

    key_entry_text.set(helper.convert_bytes_to_hex(key))

    log("Gen Key: Generated.")

"""
On click functionality of 'Gen. IV' button.
"""
def gen_iv_click():
    iv = helper.initialization_vector()
    
    iv_entry_text.set(helper.convert_bytes_to_hex(iv))

    log("Gen IV: Generated.")

"""
ECB Mode Select Event
"""
def ecb_mode_select():

    gen_iv_button.config(state='disabled')
    iv_entry.config(state='disabled')
    
    log("ECB: Selected.")

"""
CBC Mode Select Event
"""
def cbc_mode_select():

    gen_iv_button.config(state='normal')
    iv_entry.config(state='normal')
    
    log("CBC: Selected.")


# ------------- Graphical User Interface Code ----------- #

# Declaring root Tk object
root = Tk()
root.resizable(0,0) # Prevents resizing window
root.title("AES Encryption App")
root.iconbitmap('aes.ico')

path_entry_text = StringVar()
key_entry_text = StringVar()
iv_entry_text = StringVar()
config_entry_text = StringVar()
config_enabled = BooleanVar()
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
od_entry.grid(column=1, row=1, sticky=(W,E), pady=(10,0))

# Seperator line between fpk and od frames
ttk.Separator(mainframe, orient="horizontal").grid(column=0, row=1, sticky=(E,W))

#frame for encryption params
encframe = ttk.Frame(mainframe)
encframe.grid(column=0, row=2, sticky=W)

ttk.Label(encframe, text="Key: ").grid(column=0, row=1, sticky=E)
key_entry = ttk.Entry(encframe, width=40, textvariable=key_entry_text)
key_entry.grid(column=1, row=1, sticky=(W,E), padx=(11,0), pady=(10,0))

ttk.Label(encframe, text="Initialization\n       Vector: ").grid(column=0, row=2, sticky=E)
iv_entry = ttk.Entry(encframe, width=40, state='disabled', textvariable=iv_entry_text)
iv_entry.grid(column=1, row=2, sticky=(W,E), padx=(11,0), pady=(10,0))

# Seperator line between od and buttons frames
ttk.Separator(mainframe, orient="horizontal").grid(column=0, row=3, sticky=(E,W))

#config field and check box
configframe = ttk.Frame(mainframe)
configframe.grid(column=0, row=4, sticky=(E,W))
ttk.Label(configframe, text="Config: ").grid(column=0, row=0, sticky=E, padx=(28,0))
config_entry = ttk.Entry(configframe, width=40, state='normal', textvariable=config_entry_text)
config_entry.grid(column=1, row=0, sticky=(E,W), padx=(10,0))
ttk.Checkbutton(configframe, onvalue=True, offvalue=False, variable=config_enabled, command=enable_config).grid(column=2, row=0, sticky=(E,W))

# Frame for control buttons
buttonsframe = ttk.Frame(mainframe)
buttonsframe.grid(column=0, row=5, sticky=(E, W))
ttk.Button(buttonsframe, text="Encrypt", command=encrypt_click).grid(column=0, row=0, sticky=(E,W), padx=(20,20))
ttk.Button(buttonsframe, text="Decrypt", command=decrypt_click).grid(column=1, row=0, sticky=(E,W), padx=(0,20))
ttk.Button(buttonsframe, text="Gen. Key", command=gen_key_click).grid(column=2, row=0, sticky=(E,W), padx=(0,20))
gen_iv_button = ttk.Button(buttonsframe, text="Gen. IV", state='disabled', command=gen_iv_click)
gen_iv_button.grid(column=3, row=0, sticky=(E,W))

#Frame for holding logging and enc parameter selections
bottomframe = ttk.Frame(mainframe)
bottomframe.grid(column=0, row=6, sticky=(E,W))

# Frame for holding log text container
logframe = ttk.Frame(bottomframe)
logframe.grid(column=0, row=0)
log_text = Text(logframe, state="disabled", width=40, height=10, wrap='word')
log_text.grid(column=0, row=0)

modesframe = ttk.Frame(bottomframe)
modesframe.grid(column=1, row=0, padx=(35,0))
modes = [ ttk.Radiobutton(modesframe, text='ECB', variable=enc_mode, value=0, command=ecb_mode_select),
        ttk.Radiobutton(modesframe, text='CBC', variable=enc_mode, value=1, command=cbc_mode_select), ]
for i,rb in enumerate(modes): rb.grid(column=0, row=i)

keysizeframe = ttk.Frame(bottomframe)
keysizeframe.grid(column=2, row=0)
keysizes = [ ttk.Radiobutton(keysizeframe, text='128', variable=key_size_bytes, value=16),
             ttk.Radiobutton(keysizeframe, text='192', variable=key_size_bytes, value=24),
             ttk.Radiobutton(keysizeframe, text='256', variable=key_size_bytes, value=32), ]
for i,keysize in enumerate(keysizes): keysize.grid(column=0, row=i)

# Adds padding around each frame container within mainframe
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

keysizes[0].invoke()
modes[0].invoke()

# Main event loop needed to make everything run
root.mainloop()
