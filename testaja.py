from bs4 import BeautifulSoup
import requests # tadinya pake urllib, tetapi raspberry pi tidak bisa install library urllib
import telepot
import time, datetime
from telepot.loop import MessageLoop
from pprint import pprint

URL = 'https://jadwalsholat.pkpu.or.id/'
page = requests.get(URL)
soup = BeautifulSoup(page.text,'html.parser')
#print(soup.prettify()) # <-- dipake buat cek aja
bot = telepot.Bot('1267590625:AAHJV6vU6Q5KxMBs6CAYcehsshNp1s56h9I')
now = datetime.datetime.now()
jam = now.strftime("%H:%M")

TabelWaktu = soup.find('tr', {'class':'table_highlight'})
#Waktu = TabelWaktu.find_all('td')
Shubuh = TabelWaktu.find_all('td')[1].get_text()
Dzuhur = TabelWaktu.find_all('td')[2].get_text()
Ashar = TabelWaktu.find_all('td')[3].get_text()
Maghrib = TabelWaktu.find_all('td')[4].get_text()
Isya = TabelWaktu.find_all('td')[5].get_text()
okeh = "13:20"

response = bot.getUpdates()


def action(msg):

    now = datetime.datetime.now()
    jam = now.strftime("%H:%M")
    okeh = "14:39"
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)
    if jam == okeh:
        bot.sendMessage (26222891, str(" berhasil"))

   
while 2:
    MessageLoop(bot, action).run_as_thread()
    pprint(response)
    print ('Up and Running....')
    time.sleep(10)


