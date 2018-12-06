### file name: test.ipynb
```
#user input username and invisible password to sign in
#if it is correct, show hello
#if user input wrong information for 3 times, system locked.
#written by frostime

import getpass
name = input ("please input your username: ")
depart = {
        'emy': 'admin',
        'bob': 'member',
        'cat': 'newer',
}
count=0
flag=0
#this is a switch-case function, saving user's information
def login(var):
    return {
    'emy': '1234',
    'bob': '2345',
    'cat': '3456'
    }.get(var,'invalid username or password')

while count<3:
    psw = getpass.getpass("please input your password: ")
    rpsw=login(name) #right passwerd = rpsw
    if psw==rpsw:
        print('hello! %s' % name) #comparing to using "+", this statement saves more space
        flag=1
        break
    else:
        print('access denied, please try again!')
        count=count+1
else:
    print('system locked')

if flag==1:
#show their department after they login successfully
    dpt=depart[name]
    print('you are: %s' % dpt)
```
### tuple
```
tup1=(1,2,3,4,5)
tup2=('a','b','c','d')
tup2=tup1[:2]+tup2+tup1[2:]

for a in tup2:
    print (a)
    
for b in range(len(tup2)):
    print (b)
```
### write and read json, dictionary
```
import json
dic = {  
    'andy':'python',  
    'william':'js',
    'hello':'world'
      }  
#write
js = json.dumps(dic)   
file = open('this.json', 'w+')  
file.write(js)
```
```
import json
#read
#read and write mush be put in 2 different modules, otherwise there will be errors when reading
with open("this.json", 'r') as f:
    temp = json.load(f)
    print(temp)
    print(temp['andy'])
```
### three level menu, file name: menu3lvl.ipynb
```
menu = {
    '1':{
        'chinese':{
            'a1':['AUD 12', 'AUD 15'],
            'a2':['AUD 13', 'AUD 16']
        },
        'western':{
            'b1':['AUD 12', 'AUD 15'],
            'b2':['AUD 13', 'AUD 16']
        }
    },
    '2':{
        'chinese2':{
            'aa1':['AUD 12', 'AUD 15'],
            'aa2':['AUD 13', 'AUD 16']
        },
        'western2':{
            'bb1':['AUD 12', 'AUD 15'],
            'bb2':['AUD 13', 'AUD 16']
        }
    },
    '3':{
        'chinese3':{
            'aaa1':['AUD 12', 'AUD 15'],
            'aaa2':['AUD 13', 'AUD 16']
        },
        'western3':{
            'bbb1':['AUD 12', 'AUD 15'],
            'bbb2':['AUD 13', 'AUD 16']
        }
    }
}

current=menu
for key in current:
    print (key)
lvl1=input ("please choose the number of people: ") #lvl1: num of people
if lvl1=='1'or lvl1=='2'or lvl1=='3':
    current=menu[lvl1]
    temp=[]
    for key in current:
        print (key)
        temp.append(key)
    lvl2=input("please choosse the style of meal: ") #chinese or western
    if temp.count(lvl2)>0:
        current=menu[lvl1][lvl2]
        temp=[]
        for key in current:
            print (key)
            temp.append(key)
        lvl3=input("please choosse the plan: ") #plan1 or plan2
        if temp.count(lvl3)>0:
            current=menu[lvl1][lvl2][lvl3]
            print (current)
        else:
            print ("error in level 3 menu")
    else:
        print("error in level 2 menu" )
else:
    print ("error in level 1 menu")
```
