#!/usr/bin/python

import os, sys, getopt

def exit_if_not_valid_file(filename):
   if not os.path.isfile('./'+filename):
      print("{} was not found in the current directory.".format(filename))
      sys.exit()

def main(argv):
   inputfile = ''
   outputfile = ''
   key_size = 0

   help_text = 'aes_cli.py -k <key size> -i <inputfile> -o <outputfile>'

   if len(argv) == 0:
      print(help_text)
      sys.exit(2)

   try:
      opts, args = getopt.getopt(argv,"hk:i:o:",["ifile=","ofile="])
   except getopt.GetoptError:
      print(help_text)
      sys.exit(2)
   
   # Process input from arguments 
   for opt, arg in opts:
      if opt == '-h':
         print(help_text)
         sys.exit()
      elif opt == ("-k"):
         key_size = int(arg)
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg

   # Check for valid input
   if key_size not in [128,192,256]:
      print("The key size must be either 128, 192, or 256 bits long.")
      sys.exit()

   if len(inputfile) == 0 or len(outputfile) == 0:
      print("Please provide a filename.")
      sys.exit()

   exit_if_not_valid_file(inputfile)
   exit_if_not_valid_file(outputfile)



if __name__ == "__main__":
   main(sys.argv[1:])