from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://islamqa.info/en/answers/128927/it-is-essential-to-acquire-and-take-possession-of-items-before-selling-them"

webpage = requests.get(url)
print(webpage)

soup = BeautifulSoup(webpage.content, 'html5')
print(soup)

a= soup.find(class_='single_fatwa__question text-justified').text


print(a)

b=soup.find(class_='single_fatwa__answer').text

print(b)






data=[[a,b,]]
df=pd.DataFrame(data,columns=["a","b"])
print(df)

df.to_csv("demo.csv")
print("ok")
