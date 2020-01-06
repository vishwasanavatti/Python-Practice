from __future__ import print_function


def sum(a):
    add = 0;
    while a<50:
        add+=a;
        a+=1;
    return add;


print(sum(5))

x=125


def c():
    y=100
    print(x)
    print (y)

def d():
    print (x)

c()
d()

def sent(name='Vishwas',action="ate",item='egg'):
    print (name,action,item)

sent()
sent("Nikesh",'is',"Mad")
sent(item="Salad")
sent(item="awesome",name='Manoj',action='is')

ah=[1,2,3,4,5]
k,*l=ah
print(k)
print(l)

def sum(*args):
    t=0;
    for c in args:
        t+=c;
    print(t)

sum(1)
sum(1,2,3,4)

def calc(a,b,c):
    d=a+(b*2)-(c*3)
    print(d)

am=[10,5,2]
bm=[15,3,2]
calc(bm[0],bm[1],bm[2])#time consuming
calc(*am)
