### improved 3-level menu .py file
```
import json
import sys
#read
with open("menu.json", 'r') as f:
    menu = json.load(f) #menu is a global variable
#functions
def output (dict0):  #dict0 should be a dict, this function is used to print current menu
    for key in dict0:  #traverse all keys in current dict
        print (key)

def level1 (opt1): #use user's input as opt1
    while opt1!='q' and opt1!='b': #q: quit, b: back
        if opt1 in menu: 
            current2 = menu[opt1] #current2: 2nd level of menu
            level2(current2) #call def level2
            break
        else:
            level1(input ("error, please try again:"))
            break
    else:
        print("quit successfully")
        
def level2(current2):
    output(current2) #output the possible choices of 2nd level of menu
    opt2=input("please choose the style of meal: ")
    while opt2!='q': 
        if opt2 in current2:
            current3=current2[opt2] #current3: 3rd level of menu
            level3(current2, current3) #call def level3
            break
        elif opt2=='b':
            output(menu)
            level1(input ("please choose the number of people:"))
            break
        else:
            print("error, please try again")
            level2(current1)
            break
    else:
        print("quit successfully")

def level3(current1, current2):
    output(current2)
    opt3=input("please choose the style of meal: ")
    while opt3!='q':
        if opt3 in current2:
            current3 = current2[opt3]
            print ("your final choice is: %s" %current3)
            break
        elif opt3=='b':
            level2(current1)
            break
        else:
            print("error, please try again")
            level3(current2)
            break
    else:
        print("quit successfully")
#main
print("press q to quit, press b to return to the upper layer of menu...")
output(menu)
level1(input ("please choose the number of people:"))
```
