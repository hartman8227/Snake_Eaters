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

def getdatetime(timedateformat='complete'):
        from datetime import datetime
        timedateformat = timedateformat.lower()
        if timedateformat == 'day':
            return ((str(datetime.now())).split(' ')[0]).split('-')[2]
        elif timedateformat == 'month':
            return ((str(datetime.now())).split(' ')[0]).split('-')[1]
        elif timedateformat == 'year':
            return ((str(datetime.now())).split(' ')[0]).split('-')[0]
        elif timedateformat == 'hour':
            return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
        elif timedateformat == 'minute':
            return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1]
        elif timedateformat == 'second':
            return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2]
        elif timedateformat == 'millisecond':
            return (str(datetime.now())).split('.')[1]
        elif timedateformat == 'yearmonthday':
            return (str(datetime.now())).split(' ')[0]
        elif timedateformat == 'daymonthyear':
            return ((str(datetime.now())).split(' ')[0]).split('-')[2] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[1] + '-' + ((str(datetime.now())).split(' ')[0]).split('-')[0]
        elif timedateformat == 'hourminutesecond':
            return ((str(datetime.now())).split(' ')[1]).split('.')[0]
        elif timedateformat == 'secondminutehour':
            return (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[2] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[1] + ':' + (((str(datetime.now())).split(' ')[1]).split('.')[0]).split(':')[0]
        elif timedateformat == 'complete':
            return str(datetime.now())
        elif timedateformat == 'datetime':
            return (str(datetime.now())).split('.')[0]
        elif timedateformat == 'timedate':
            return ((str(datetime.now())).split('.')[0]).split(' ')[1] + ' ' + ((str(datetime.now())).split('.')[0]).split(' ')[0]


# Variable space
path_v = "~/VMS/vehicles/"
file_full = 'path_v' + 'VIN'
date = getdatetime('daymonthyear')
# What vehicle are we playing with today?
clear
while false
 VIN = input("What is the VIN Number. (Type "x" to exit")
  VIN2 = input("Please confirm the VIN Number (Type "x" to exit")

   if VIN2 == VIN
     break
    else
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
mileage = input("What is the mileage?")
print "Please describle the problem?"
problem = input()


# Did we use any parts?
print "Were any parts or supplies used? (Y/N)"
yn = input ()
    a = s.lower(yn)
    del yn
    __ = a[0]
    if __ = "y"
        while __= "y"
            make = input("What is the make of the part")
            part = input("What is the part number?")
            parts = [make + ',' + part]
                for item in parts
                partslist.append(item)
                yn = input("Any more")
                yn = input ()
                    a = s.lower(yn)
                    del yn
                    __ = a[0]

# Ok now it is time to write all this in a file
# want to write in csv format: date,mileage,problem,parts,parts,parts,etc
f.write(date + mileage + problem + partslist)
