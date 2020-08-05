from bs4 import BeautifulSoup
import requests # tadinya pake urllib, tetapi raspberry pi tidak bisa install library urllib
import telepot
import time, datetime
from telepot.loop import MessageLoop
from pprint import pprint

URL = 'https://jadwalsholat.pkpu.or.id/' # ini alamat URL yang menyediakan jadwal sholat realtime, kita akan scraping page ini
bot = telepot.Bot('******') # <-- Ganti String value dengan token dari telegram bot / BotFather
response = bot.getUpdates()

pprint(response)
print ('Memulai..')


while True:
    
    page = requests.get(URL)
    soup = BeautifulSoup(page.text,'html.parser')
    #print(soup.prettify()) # <-- dipake buat cek aja
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
    
    NShubuh = "Waktu Shubuh hari ini :" + Shubuh
    NDzuhur = "Waktu Dzuhur hari ini :" + Dzuhur
    NAshar = "Waktu Ashar hari ini :" + Ashar
    NMaghrib = "Waktu Maghrib hari ini :" + Maghrib
    NIsya = "Waktu Isya hari ini :" + Isya
    
    Print(NShubuh)
    
    if jam == Shubuh :
        print("Shubuh")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Shubuh!"))
        bot.sendMessage ('@JadwalSholatJakarta', str(NShubuh))
    elif jam == Dzuhur :
        print("Dzuhur")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Dzuhur!"))
        bot.sendMessage ('@JadwalSholatJakarta', str(NDzuhur))
    elif jam == Ashar :
        print("Ashar")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Ashar!"))
        bot.sendMessage ('@JadwalSholatJakarta', str(NAshar))
    elif jam == Maghrib :
        print("Maghrib")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Maghrib, Selamat Berbuka Puasa!"))
        bot.sendMessage ('@JadwalSholatJakarta', str(NMaghrib))
    elif jam == Isya :
        print("Isya")
        bot.sendMessage ('@JadwalSholatJakarta', str(" Waktunya Sholat Isya!"))
        bot.sendMessage ('@JadwalSholatJakarta', str(NIsya))

    time.sleep(10)
