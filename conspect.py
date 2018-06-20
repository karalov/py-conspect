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

#sorting by index
order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='') # sort: first lower, then upper, then odd numbers, then even

#Let's say you have to make a list of the squares of integers from  to  (both included).

>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
#Now, you only require those elements that are greater than  but less than .

>> l = list(filter(lambda x: x > 10 and x < 80, l))