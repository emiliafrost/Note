### file name: test.ipynb
```
#user input username and invisible password
#if the username and password is correct
#then the system output hello!

#written by frostime

#如果首行缩进错误，就会报错

import getpass
name = input ("please input your username: ")
psw = getpass.getpass("please input your password: ")

#below is a switch-case function using a dictionary method
def login(var):
    return {
    'emy': '1234',
    'bob': '2345',
    'cat': '3456'
    }.get(var,'invalid username or password')

rpsw=login(name) #right passwerd = rpsw
if psw==rpsw:
    print('hello! %s' % name) #comparing to using "+", this statement saves more space
    flag=True
else:
    print('access denied, please try again!')
    flag=False

if flag==True:
#show their department after they login successfully
    def case(var):
        return {
            'emy': 'admin',
            'bob': 'member',
            'cat': 'newer',
        }.get(var,'error')

    dpt=case(name)
    print('you are: %s' % dpt)
```
### file name: test2.ipynb, about tuple, list and dictionary
```
tup1=(1,2,3,4,5)
tup2=('a','b','c','d')
tup2=tup1[:2]+tup2+tup1[2:]
sum=0

for a in tup2:
    print (a)
    
for b in range(len(tup2)):
    sum = sum+b
print (sum)
```
