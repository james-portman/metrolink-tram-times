import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

def tram_time(minutes):
    if minutes.lower() in ["arrived", "departing"]:
        return minutes
    minutes = minutes.replace('mins','')
    minutes = minutes.replace('min','')
    return format(datetime.now() + timedelta(minutes=int(minutes)), '%H:%M')

def check(from_stop):
    result = requests.get("https://beta.tfgm.com/public-transport/tram/stops/"+from_stop+"-tram")

    soup = BeautifulSoup(result.text, 'html.parser')
    departures = soup.find(id='departure-items')

    trams = departures.find_all('tr', "tram")
    for tram in trams:
        destination = tram.find('td', 'departure-destination').get_text().strip()
        wait = tram.find('td', 'departure-wait').get_text().strip()
        print "From %s -> %s - %s" % (from_stop, destination, tram_time(wait))

check('deansgate-castlefield')
check('exchange-quay')
check('exchange-square')
check('mediacityuk')
