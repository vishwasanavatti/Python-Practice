import requests
from bs4 import BeautifulSoup
import operator

def start(url):
    wordList=[]
    source_code=requests.get(url).text
    soup=BeautifulSoup(source_code,'html.parser')
    for post in soup.findAll('div',{'class':'_3wU53n'}):
        content = post.string
        words=content.lower().split()
        for sep in words:
            #print(sep)
            wordList.append(sep)
    clean_list(wordList)

def clean_list(wordlist):
    clean_list_word=[]
    for word in wordlist:
        symbols="~!@#$%^&*()_+<>:\"?{}|`;'/.,[\]-="
        for i in range(0,len(symbols)):
            word =word.replace(symbols[i],"")
        if len(word)>0:
            clean_list_word.append(word)
    create_dic(clean_list_word)

def create_dic(clean_list_word):
    word_count={}
    for word in clean_list_word:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1

    for key,value in sorted(word_count.items(),key=operator.itemgetter(1)):
        print(key,value)



start('https://www.flipkart.com/search?q=tablet&otracker=start&as-show=on&as=off')

