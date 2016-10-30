# CS6001-AES

# aes.ico

    Icon image file for thumbnail of GUI.
  
# test_img.jpg

    Temporary image file used in aes_io.py to test file I/O. 
    Will be removed when program starts becoming more complete.
  
# aes_impl.py

    Functions implementing core AES encryption and decryption functionality.
  
# aes_io.py

    Sample I/O handling.
    Opens files and encrypts them in byte sized chunks, appending results to output file.
    Still needs actual aes implementation functions called within them, recieving strange integer error currently.
  
# ------- NEW -------- #

# aes_gui.py

    Prototype GUI implementation.
    Takes file path, key, and output directory as input.
    Clicking buttons will result in actions, with information logged in text window and bottom of window about errors or successes.
    Currently just prints button name in text window when buttons are pressed.
  
  # Buttons
  
    Encrypt: 
      Takes the file path and key and encrypt the file with that key, placing it within the desired output directory.
      
    Decrypt:
      Takes the file path and key and decrypts the file with that key, placing it within the desired output direcory.
      
    Gen. Key:
      Generates a key for the user, in the event they don't want to provide their own during ecryption.
      Need to cause error notification if trying to do this when decrypting, or just mreove this button.
      
  # Text Fields
  
    File Path:
      Text field for user to provide file path of the file they want to encrypt or decrypt.
      
    Key:
      Text field for user to provide the key needed for decryption or the key phrase they'd like to use for encryption.
      This will need to use an appropriate hasing function to convert human-friendly phrases into correct byte length keys.
      
    Out Directory:
      Text field for user to provide the desired directory for the resulting encrypted/decrypted file to be placed in.
      Will default to same directory as the file given to be encrypted/decrypted.
    
