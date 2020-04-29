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

TabelWaktu = soup.find('tr', {'class':'table_highlight'})
Shubuh = TabelWaktu.find_all('td')[1].get_text()
Dzuhur = TabelWaktu.find_all('td')[2].get_text()
Ashar = TabelWaktu.find_all('td')[3].get_text()
Maghrib = TabelWaktu.find_all('td')[4].get_text()
Isya = TabelWaktu.find_all('td')[5].get_text()

response = bot.getUpdates()

   
pprint(response)
print ('Memulai..')
print(Shubuh)

while True:

    TabelWaktu = soup.find('tr', {'class':'table_highlight'})
    Shubuh = TabelWaktu.find_all('td')[1].get_text()
    Dzuhur = TabelWaktu.find_all('td')[2].get_text()
    Ashar = TabelWaktu.find_all('td')[3].get_text()
    Maghrib = TabelWaktu.find_all('td')[4].get_text()
    Isya = TabelWaktu.find_all('td')[5].get_text()
    now = datetime.datetime.now()
    jam = now.strftime("%H:%M")
    #okeh = "10:20"
    #print(jam)

    if jam == Shubuh :
        print("Shubuh")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Shubuh oi!"))
    elif jam == Dzuhur :
        print("Dzuhur")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Dzuhur oi!"))
    elif jam == Ashar :
        print("Ashar")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Ashar oi!"))
    elif jam == Maghrib :
        print("Maghrib")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Maghrib oi!"))
        bot.sendMessage ('@JadwalSholatJakarta', str(" Selamat Berbuka Puasa!"))
    elif jam == Isya :
        print("Isya")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Isya oi!"))

    time.sleep(60)


