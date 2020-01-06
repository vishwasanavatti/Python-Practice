import math
area=4*math.pi*2.3**2
volume=(4/3)*math.pi*2.3**3
print("Surface Area is {:.2f}".format(area))
print("Volume is {:.2f}" .format(volume))

import math
print("Surface area is {:.2f}".format(4*math.pi*2.3**2))
print("Volume is {:.2f}".format((4/3)*math.pi*2.3**3))
"""
s='tata consultancy services limited'
count=0
xa=len(s)
sas=0
vowels=set("aeiou")
while sas<xa:
    if s[sas] == 'a' or s[sas] == 'e' or s[sas] == 'i' or s[sas] == 'o' or s[sas] == 'u':
        count+=1
        sas+=1
print(count)"""

s = 'tata consultancy services limited'
count = 0
a = 0
vowels = set("aeiou")
l = len(s)
for letter in s:
    if letter in vowels:
            count += 1

print(count)

name=input("Enter name: ")
#first,last=name.split()
#print(first[::-1],last[::-1])

words=name.split(" ")
print(words)

for word in words:
    li=len(word)-1
    for index in range(li,-1,-1):
        print(word[index],end='')
    print(end=' ')
print(end='\n')

for x in (1,10,100):
    print(x)