from playsound import playsound
from gtts import gTTS
import urllib.request
import requests
import PyPDF2
import json
import time
import os

url = 'http://www.greatwar.nl/books/meinkampf/meinkampf.pdf'
r = requests.get(url, allow_redirects=True)
open('meinkampf.pdf', 'wb').write(r.content)

pdfFileObj = open('meinkampf.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
numofpage = pdfReader.numPages
firstpart = []
secondpart = []
thirdpart = []
id = "" #Yout channel id
key = ""#You need free youtube api key
data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key).read()
url = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
num = int(url)
line = 0

text = []
for i in range(numofpage):
    page = pdfReader.getPage(i)
    some = page.extractText().split(".")
    text = text + some


def read(some):
    filename = "mp3.mp3"
    tts = gTTS(text=some, lang='en')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
    pass

while True:
    data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+id+"&key="+key).read()
    url = json.loads(data)["items"][0]["statistics"]["subscriberCount"]
    subs = int(url)
    time.sleep(1)
    if subs == num:
        print(text[line])
        read(text[line])
        num = num + 1
        line = line + 1
