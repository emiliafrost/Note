### find what data is updated
```
# original data
old_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#2":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
}
 
# new data
new_dict = {
    "#1":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 800 },
    "#3":{ 'hostname':'c1', 'cpu_count': 2, 'mem_capicitys': 80 },
    "#4":{ 'hostname':'c2', 'cpu_count': 2, 'mem_capicity': 80 }
}

oldset = set(old_dict.keys())
newset = set(new_dict.keys())
updatelist = list(oldset.intersection(newset)) 

addList = []
delList = []

for key in newset:
    if key not in updatelist:
        addList.append(key)

for key in oldset:
    if key not in updatelist:
        delList.append(key)   
        
print (updatelist)
        
for key in updatelist:
    tempold=old_dict[key] # { 'hostname':'c1', 'cpu_count': 2, 'mem_capicity': 80 }
    tempnew=new_dict[key] # { 'hostname':'c1', 'cpu_count': 2, 'mem_capicitys': 80 }
    templist=tempold.keys() ^ tempnew.keys()
    if len(templist) > 0: #which means that keys are updated
        print(key,templist) #show the updated key
    else: #if the key are the same, judge whether the values are updated
        for i in tempold:
            if tempold[i] != tempnew[i]:
                print(key,i,tempold[i],i,tempnew[i]) #show the same key and the updated part
```
