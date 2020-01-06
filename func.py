def hello():
    print("Hi How are you?")

fw=open('sample.txt','w')
fw.write("Hello World!")
fw.write("\n Whats up?")
fw.close()

fr=open("sample.txt",'r')
text=fr.read()
print(text)
fr.close()