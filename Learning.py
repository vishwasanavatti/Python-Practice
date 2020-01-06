vish=['vishwas',"Manoj","Nikesh"]

for v in vish:
    print (v),
    print (len(v)),
    print (v.upper())

a=2;
while a<5:
    print("Hello")
    a+=1;

for x in range(1,101):
    if (x%4)==0:
        print (x)

n=25;
for m in range(50):
    if m is n:
        print (m,"Found");
        break;
    else:
        print (m);

f=[10,77,25,55]
for j in f:
    if j==25:
        continue;
    else:
        print (j);

asn=r"\n\t\\"
print(asn)

s1="Py"+"thon"
print(s1)
s2="python is amazing"
print(s2)
s3="python\nis\namazing"
print(s3)
s4="Python\tis\tamazing"
print(s4)

s1='Python\nis\namazing'
rs1="%r"%s1
print(rs1)
s2='Python\tis\tamazing'
rs2="%r"%s2
print(rs2)

s='INfinity'
print(s.isalpha())
print(s.isdigit())
print(len(s))
print(s.upper())
print(s.lower())
print(s.count('i'))
print(s.index('t'))

emplist1=list()
print(emplist1)
emplist1.append(9)
emplist1.append(10)
print(emplist1)
emplist2=[]
print(emplist2)
emplist2.extend(('a','b','c'))
print(emplist2)
e=emplist2.pop()
print(emplist2)
print(e)


f=slice(4)
print(f)

k=['a','b','c','d','e','f','g']

print(k[slice(0,7,2)])
print(k[slice(0,4,2)])
print(k[slice(0,7,2)])

aks=range(1,10,100)
print(list(aks))

k1=range(5)
print(list(k1))
k2=range(10,15)
print(list(k2))
k3=range(10,21,2)
print(list(k3))
k4=range(100,1,-25)
print(list(k4))


a={10,20,30,40}
b={30,60}
u=a.union(b)
print(list(u))
i=a.intersection(b)
print(list(i))
d=a-b
print(list(d))
sd=a.union(b)-a.intersection(b)
print(list(sd))


d1=dict()
print(d1)
d2={'p':'t'}
print(d2)
d2['v'] = ''
d2['d'] = ''
print(d2)
del(d2['v'])
print(d2)



