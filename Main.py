from bs4 import BeautifulSoup
#import urllib.request as request
import telepot
import time, datetime
from telepot.loop import MessageLoop
import urllib3.request as request

URL = 'https://jadwalsholat.pkpu.or.id/'
page = request.urlopen(URL)
soup = BeautifulSoup(page, 'html.parser')

'''print(soup.prettify())'''

TabelWaktu = soup.find('tr', {'class':'table_highlight'})

Waktu = TabelWaktu.find_all('td')

Shubuh = TabelWaktu.find_all('td')[1].get_text()
Dzuhur = TabelWaktu.find_all('td')[2].get_text()
Ashar = TabelWaktu.find_all('td')[3].get_text()
Maghrib = TabelWaktu.find_all('td')[4].get_text()
Isya = TabelWaktu.find_all('td')[5].get_text()

bot = telepot.Bot('1267590625:AAHJV6vU6Q5KxMBs6CAYcehsshNp1s56h9I')

now = datetime.datetime.now()
def action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print ('Received: %s' % command)
    if command == '/shubuh':
        bot.sendMessage (chat_id, str("Waktu Shubuh pukul " + Shubuh))
    elif command == '/dzuhur':
        bot.sendMessage (chat_id, str("Waktu Dzuhur pukul " + Dzuhur))
    elif command == '/ashar':
        bot.sendMessage (chat_id, str("Waktu Ashar pukul " + Ashar))
    elif command == '/maghrib':
        bot.sendMessage (chat_id, str("Waktu Maghrib pukul " + Maghrib))
    elif command == '/isya':
        bot.sendMessage (chat_id, str("Waktu Isya pukul " + Isya))

print (bot.getMe())
MessageLoop(bot, action).run_as_thread()
print ('Up and Running....')
while 1:
    time.sleep(10)

