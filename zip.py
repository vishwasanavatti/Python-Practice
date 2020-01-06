first=['Vishwas','Nikesh','Manoj']
last=['Anavatti','Raj','Kumar']

names=zip(first,last)

#[(vishwas,Anavatti),(Nikesh,raj),(Manoj,Kumar)]

for a,b in names:
    print(a , b)


x=lambda a:a*5

print(x(2))

market={
    'Apple':4536,
    'FB': 3342,
    'Google':2131,
    'Amazon':7634,
    'Tesla':2345
}

mar=zip(market.values(),market.keys())
print(min(zip(market.values(),market.keys())))
print(max(mar))
print(sorted(zip(market.keys(),market.values())))
print(sorted(zip(market.values(),market.keys())))