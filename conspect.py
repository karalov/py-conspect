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
