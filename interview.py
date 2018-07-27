#!/usr/bin/python3

dataset1 = [['raptozaur',2.3],
['tyranozaur',4.5],
['obazaur',3.1],
['mamozaur',1.3],
['kokozaur',2.5],
['lanozaur',3.4],
['papozaur',2.2]]

dataset2 = [['lanozaur',2,3.1],
['papozaur',4,2],
['raptozaur',2,5.3],
['kokozaur',2,3.2],
['tyranozaur',4,3],
['mamozaur',2,2.4]]

out={}
for lst in dataset2:
  if lst[1] == 2:
    name=lst[0]
    out[name]=lst[2]*dict(dataset1)[name]

newlist=sorted(out.items(),key=lambda x: x[1])
newlist.reverse()
print(newlist)



             
