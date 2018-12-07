# improved 3 level menu .py
```
import json
import sys
#read
with open("menu.json", 'r') as f:
    menu = json.load(f)
    current0 = menu
    for key in current0:
        print (key)

def level1 (opt1): #level1's input is changeable
    while opt1!='q' and opt1!='b':
        if opt1 in menu:
            global opt11
            opt11=opt1
            current=menu[opt1]
            for key in current:
                print (key)
            level2(input ("please choose the style of meal: "))    #link to the 2nd level of menu
            break
        elif opt1!='b':
            level1(input ("error, please try again:"))
            break
        
def level2(opt2):
    while opt2!='q':
        print ("this is level2")
        current=menu[opt11]      
        if opt2 in current:
            global opt22
            opt22=opt2
            current=menu[opt11][opt2]
            for key in current:
                print(key)
            level3(input("please choose the plan: ")) #link to the 3nd level of menu
            break
        elif opt2=='b':
            level1(input ("please choose the number of people:"))
            break
        else:
            level2(input ("error, please try again:"))
            break      

def level3(opt3):
    while opt3!='q':
        current=menu[opt11][opt22]
        if opt3 in current:
            current = menu[opt11][opt22][opt3]
            print ("your final choice is: %s" %current)
            break
        elif opt2=='b':
            level2(input ("please choose the style of meal: "))
        else:
            level3(input ("error, please try again:"))   
        
level1(input ("please choose the number of people:"))
```
