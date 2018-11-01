#! /usr/bin/python

# Repair log for VMS
# By Paul Hartman
# Copyright 2018

# use python 3

#### DO ONE THING BUT DO IT WELL! ####


# Import space
import os

# Def Space
def clear():
    if (os.name == 'nt'):
        c = os.system('cls')
    else:
        c = os.system('clear')
    del c

# Variable space
path_v = "~/VMS/vehicles/"
file_full ='path_v' + 'VIN'

# What vehicle are we playing with today?
clear
while false
    VIN = raw_input("What is the VIN Number. (Type "x" to exit")
    VIN2 = raw_input("Please confirm the VIN Number (Type "x" to exit")

    if VIN2 == VIN
        break
    else;
        print ("The Vin Numbers do not match! please try again. Type "x" both times to exit program.")

# Escape sequence
if VIN == "x"
    exit(

    )
# Open that vehicle's file or create it if it doesn't exist
try:
    with open(file_full) as file:
        pass
except IOError as e:
    print "Unable to open the file on that vehicle. Have you created it yet?"
# NOTE: Build a program to create files on new Vehicles.
print "please discrible the problem"
problem = raw_input()


# Did we use any parts?

        # Any other parts?
