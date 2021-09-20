# -*- coding: utf-8 -*-
"""
Created on Thu Apr 6 16:37:42 2021

@author: Akhil Robertson Cutinha
"""

from pprint import PrettyPrinter
from nand2tetris_hdl_parser import parse_hdl

choice = "y"
while(choice == "y" or choice == "Y"):
    filename = input("Enter the name of the HDL file (along with .hdl): ")
    pp = PrettyPrinter()
    hdl = open(filename,"r").read()
    parsed_hdl = parse_hdl(hdl)
    #pp.pprint(parsed_hdl) 
    internatl_bus = {}  #dictionary to store the internal pins and their bus sizes

    #function to check if a pin can be subbussed. Internal pins are not allowed to be subbussed
    def is_sliceable(pin, size = 0):
        for part in parsed_hdl['inputs']:
            if(part['name'] == pin):
                return True
        for part in parsed_hdl['outputs']:
            if(part['name'] == pin):
                print(size)
                return True
        for key, val in internatl_bus.items():
            if(key == pin):
                if(val == size):
                    return True
        return False

    def is_busable(pin, size = 0):
        for part in parsed_hdl['inputs']:
            if(part['name'] == pin):
                return True
        for part in parsed_hdl['outputs']:
            if(part['name'] == pin):
                print(size)
                return True
        return False
    #print(is_sliceable('sel'))
    
    #Driver Function: checks if a sub bus error occurs. Needs the above is_sliceable function, filename and parsedHDL
    def internal_sub_bus():
        count = 0
        for part in parsed_hdl['parts']:
            for seg in part['external']:
                bus_size = seg['end'] - seg['start'] + 1
                if seg['name'] in internatl_bus:
                    if(is_sliceable(seg['name'],bus_size)):
                        continue
                    else:
                        count += 1
                        print('Internal bus of "'+seg['name']+'" cannot be sub bussed')
                        print('Bus length :', internatl_bus[seg['name']])
                        print('Bus Length used:', bus_size)
                        if(internatl_bus[seg['name']] - bus_size >= 0):
                            print('Hint: split the internal bus into 2 busses of lengths', bus_size,'and',(internatl_bus[seg['name']]-bus_size),'by subbusing the output pin where "'+seg['name']+'" is defined.' )
                        else:
                            print('You are using larger bus than available')
                else:
                    internatl_bus[seg['name']] = bus_size
        if(count == 0):
            print(" No Sub bussing Errors were found in this program, Great Job!")

    internal_sub_bus()
    choice = input("Do you want to test another program? [y/n]: ")
