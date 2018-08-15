import string
name=input("Account name: ").lower()[::-1]
pwd=""
def iswovel(letter):
    wovels="aeiou"
    if letter in wovels:
        return True
    else:
        return False

for i in [1,3,5,7]:
     if len(name) >= i:
         if name[i].upper() == "Z":
             pwd+="a"
         else:
             pwd+=string.ascii_letters[string.ascii_letters.index(name[i]) + 1]
     else:
         pwd+="_"
all=len(name)
wovels=0
nonwovels=0
for i in name:
    if iswovel(i):
        wovels+=1
    else:
        nonwovels+=1
sum=all + wovels + nonwovels + 3
lastdigit=str(int(str(sum)[0]) + int(str(sum)[1]))
pwd=pwd + str(all +1) + str(wovels + 1) + str(nonwovels +1) + str(lastdigit)
print(pwd.capitalize()+"!")
input("Press ENTER to close...")