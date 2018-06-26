import json
data=json.load(open("data.json"))
data=json.loads(open("data.json").read())

from difflib import SequenceMatcher
ratio=SequenceMatcher(None,word,another_word).ratio()  #ration of word similarity

from difflib import get_close_matches
similars_list=get_close_matches(word,words_list)

# pip install glob2
# python -m pip install glob2
import glob2
glob2.glob("*.txt")

from datetime import datetime
now=datetime.now()
now.year
now.hour
delta=now - datetime(1972,7,11)
delta.days
datetime.strptime("1972-6-11","%Y-%m-%d")
>>datetime.datetime(1972, 6, 11, 0, 0)
 now.strftime("%m/%d/%Y")
>>'06/16/2018'

# pip install jupyter
# jupyter notebook
# pip install pandas
# pip install ipython
# ipython
import pandas
df=pandas.DataFrame([[1,2,3],[4,5,6]])
df.shape
df1=pandas.read_csv('supermarkets.csv',sep=';')
df0=pandas.read_csv('http://pythonhow.com/supermarkets.csv',sep=',')
pandas.read_csv? #help on methid
df1.set_index("ID")
df1.loc[1:3,"Address":"State"]  #slicing
df1.loc[3] #All for row with ID=3
df1.iloc[0:3,2:4] #indexes instead of column names
df1.Address  # all adresses
df1.columns
df1.index
df1.T # revert, columns becoimes rows and vice versa
df1['Continent'] = ['North America'] * df1.shape[0]  #create new column
df2=pandas.read_json('super.json')
df3=pandas.read_excel('data.xlsx',sheetname=0)
data=df3.to_json
open("data.json","w").write(data)

import numpy  #multidimentional array object
n=numpy.arange(27)
n.reshape(3,9)  # 2 dimentional
n.reshape(3,3,3)  # 3 dimentional
m=numpy.asarray(list)

#pip install opencv-python  - image processing (cv2)
import cv2
im_g=cv2.imread('smallgray.png',0)  #1 dimention - greyscale numpy array
im_g=cv2.imread('smallgray.png',1)  #3 dimentional (RGB) numpy array
cv2.imwrite('newing.png',im_g)
im_g[1:3,2:4]  #slicing  rows,columns
im_g.T #invert
for i in im_g.flat   # iterate thru all elements
ims=numpy.hstack((im_g,im_g))  # tsack horisontally  vstack - vertically hsplit,vsplit  - split

# pip install folium
import folium
map = folium.Map(location=[80,100])
map.save("Map1.html")

import time
time.sleep(1)

from collections import OrderedDict
dict=OrderedDict() # to make sure order will stay constant

from itertools import groupby
l="1222311"
for k,c in groupby(l):
  print(k,list(c))
#1 ['1']
#2 ['2', '2', '2']
#3 ['3']
#1 ['1', '1']

l=[('a', 2), ('e', 3), ('c', 3), ('d', 1), ('b', 1)]
sorted(l,key=lambda x: (-x[1],x[0]))
#[('c', 3), ('e', 3), ('a', 2), ('b', 1), ('d', 1)] - first by number desc, then by letter asc (deflt)  

my_mapping = {'a': 23, 'b': 42, 'c': 0xc0ffee}
my_mapping
{'b': 42, 'c': 12648430. 'a': 23}  # 😞

# The "json" module can do a much better job:
import json
print(json.dumps(my_mapping, indent=4, sort_keys=True))
{
    "a": 23,
    "b": 42,
    "c": 12648430
}

# Note this only works with dicts containing
# primitive types (check out the "pprint" module):
>>> json.dumps({all: 'yup'})

import re
S="1qaz2wsx3edc4rfv5tgb6yhn7ujm8ik9ol0pQWERTYUIOPASDFGHJKLZXCVBNM"
re.search("[a-z]+",S).group(0)  # display first occurence all lower letters from string
qaz
re.findall("[a-z]+",S)
['qaz', 'wsx', 'edc', 'rfv', 'tgb', 'yhn', 'ujm', 'ik', 'ol', 'p']

#Valid email addresses must follow these rules:
#It must have the username@websitename.extension format type.
#The username can only contain letters, digits, dashes and underscores.
#The website name can only have letters and digits.
#The maximum length of the extension is 3
re.match("^[a-zA\-Z0-9_-]+@[a-zA-Z0-9]+\.[a-z]{1,3}$",s)
#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
#1 4 9 16 25 36 49 64 81
#r before string means to recognize "\" character as a regular character. r"\n" means two chars \ and n
print re.sub("(<!--.*?-->)", "", html) #remove comment from html 
#To replace string by another one use replace method of the string
>>> "mama kaka lala".replace("a","###")
'm###m### k###k### l###l###'

#sorting by index
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='') # sort: first lower, then upper, then odd numbers, then even

#Let's say you have to make a list of the squares of integers from  to  (both included).

>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
#Now, you only require those elements that are greater than  but less than .

>> l = list(filter(lambda x: x > 10 and x < 80, l))

#The reduce() function applies a function of two arguments cumulatively on a list of objects in succession from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
from functools import reduce
>>> reduce(lambda x, y : x + y,[1,2,3])
6
#You can also define an initial value. If it is specified, the function will assume initial value as the value given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:

>>> reduce(lambda x, y : x + y, [1,2,3], -3)
3

from fractions import Fractions
result=Fraction(numerator,denominator)  # simplify fraction
print(result.numerator, result.denominator)
t = Fraction(*reduce(lambda x,y: (x[0]*y[0], x[1]*y[1]),fracs))
#fracs: [[1,2],[3,4],[10,6]] calc product of fractions  1/2 * 3/4 * 10/6

# Why Python Is Great:
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

>>> myfunc(*tuple_vec)
1, 0, 1

>>> myfunc(**dict_vec)
1, 0, 1
>>> myfunc(*dict_vec)
x y z

import uuid # generate unique ID. Different types (uuid1,uuid2,uuid3,uuid4)
>>> str(uuid.uuid4())
'e8f3076a-77e8-47d1-9c3f-ed6bc012bc93'

# The "timeit" module lets you measure the execution
# time of small bits of Python code
>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))',number=10000)
0.3412662749997253