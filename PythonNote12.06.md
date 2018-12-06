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
