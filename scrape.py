import requests
import numpy as np
from bs4 import BeautifulSoup
  
URL = "https://web-geeks.herokuapp.com/web6.html"


urls = ["https://web-geeks.herokuapp.com/","https://web-geeks.herokuapp.com/sonnet1.html","https://web-geeks.herokuapp.com/sonnet2.html","https://web-geeks.herokuapp.com/sonnet3.html","https://web-geeks.herokuapp.com/web4.html","https://web-geeks.herokuapp.com/web5.html"]
classes = []


for url in urls:
    r = requests.get(url)
    
    soup = BeautifulSoup(r.content,"html.parser") # If this line causes an error, run 'pip install html5lib' or install html5lib

    for element in soup.find_all(class_=True):
        classes.extend(element["class"])

print(classes)