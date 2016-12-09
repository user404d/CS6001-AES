# CS6001-AES
Authors: Quincy Conduff, Scott Payne, Colin Conduff

# Software requirements 
1.  Python version 3 (~3.5 should be fine)  
2.  Tkinter version 8.5 (should be included with python)

# Usage: Steps for using the GUI for file encryption and decryption 
1.  `python3 aes_gui.py`  
2.  Select desired key length by clicking a radio button next to 128, 192, or 256.  
3.  Click `Gen. Key` button  
4.  Select AES mode  
  a.  For ECB AES mode, select `ECB` radio button  
  b.  For CBC AES mode, select `CBC` radio button and click `Gen. IV` button  
5.  In `File Path` textbox: enter in full file path to file that you would like to encrypt  
  Example: `/Users/username/Desktop/test.png`  
  Note: If `Out Directory` input is empty, the program will create an encrypted file with `.enc` appended to the end (e.g. test.png.enc). 
6.  Click `Encrypt` button  
7.  After encryption has finished, change File Path input to the file path to the encrypted file.  
  Example: `/Users/username/Desktop/test.png.enc`  
  Note: If `Out Directory` input is empty, will overwrite original input file (e.g. test.png).  
8.  Click the `Decrypt` button  

# To run unit tests for AES encryption and decryption:
`python3 aes_test.py`

# This project includes the following files:

## aes.ico

    Icon image file for thumbnail of GUI.
  
## test_img.jpg

    Temporary image file used in aes_io.py to test file I/O. 
  
## aes_impl.py

    Functions implementing core AES encryption and decryption functionality.
  
## aes_io.py

    Sample I/O handling.
    Opens files and encrypts them in byte sized chunks, appending results to output file.
  
## aes_test.py

    Unit tests for the encryption and decryption AES functions on files and string messages.

## aes_gui.py

    Encryption/Decryption GUI implementation.
    Takes file path, key, and output directory as input.
    Clicking buttons will result in actions, with information logged in text window and bottom of window about errors or successes.
  
  ## Buttons
  
    Encrypt: 
      Takes the file path and key and encrypt the file with that key, placing it within the desired output directory.
      
    Decrypt:
      Takes the file path and key and decrypts the file with that key, placing it within the desired output direcory.
      
    Gen. Key:
      Generates a key for the user, in the event they don't want to provide their own during ecryption.

    Gen. IV:
      Generates an initialization vector for use during CBC AES mode.
      
  ## Text Fields
  
    File Path:
      Text field for user to provide file path of the file they want to encrypt or decrypt.
      
    Key:
      Text field for user to provide the key needed for decryption or the key phrase they'd like to use for encryption.
      This will need to use an appropriate hasing function to convert human-friendly phrases into correct byte length keys.
      
    Out Directory:
      Text field for user to provide the desired directory for the resulting encrypted/decrypted file to be placed in.
      Will default to same directory as the file given to be encrypted/decrypted.

  ## Radio Buttons  
    Provide options for key sizes and AES modes.


