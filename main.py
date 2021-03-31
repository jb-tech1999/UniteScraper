from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
from time import sleep
import requests
import datetime
import os
from colorama import Fore, Back, Style
from datetime import datetime

myUrl = 'https://unite180.com/church_bookings/booking.php'

#open up connection and grabbing HTML
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

def check_services():

    #HTML parser
    page_soup = soup(page_html, 'html.parser')

    HQ1_Full = 'Morning Service  (08:55) (140/140)'
    HQ2_Full = 'Evening Service (16:55) (140/140)'

    Brook1_Full = 'Morning Service (09:00) (180/180)'
    Brook2_Full = 'Evening Service (17:00) (180/180)'

    Potch1_Full = 'First Service (16:00) (70/70)'
    Potch2_Full = 'Evening Service (18:00) (70/70)'

    HQ1 = page_soup.find('option', {'value': 'hq_1'}).get_text()
    if HQ1 == HQ1_Full:
        print(Fore.RED + "Sorry the service is still full: HQ Service 1")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN +HQ1)
        print(Style.RESET_ALL)
        telegram_bot_sendtext(HQ1)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))


    HQ2 = page_soup.find('option', {'value': 'hq_2'}).get_text()
    if HQ2 == HQ2_Full:

        print(Fore.RED + "Sorry the service is still full: HQ Service 2")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN +HQ2)
        print(Style.RESET_ALL)
        telegram_bot_sendtext(HQ2)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))


    Brook1 = page_soup.find('option', {'value': 'bn_1'}).get_text()
    if Brook1 == Brook1_Full:

        print(Fore.RED + "Sorry the service is still full: Brooklyn Morning service")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN +Brook1)
        print(Style.RESET_ALL)
        telegram_bot_sendtext(Brook1)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))

    Brook2 = page_soup.find('option', {'value': 'bn_2'}).get_text()
    if Brook2 == Brook2_Full:

        print(Fore.RED + "Sorry the service is still full: Brooklyn Evening service")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN +Brook2)
        print(Style.RESET_ALL)
        telegram_bot_sendtext(Brook2)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))


    Potch1 = page_soup.find('option', {'value': 'ph_1'}).get_text()
    if Potch1 == Potch1_Full:

        print(Fore.RED + "Sorry the service is still full: Potch first service service")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN +Potch1)
        print(Style.RESET_ALL)
        telegram_bot_sendtext(Potch1)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))


    Potch2 = page_soup.find('option', {'value': 'ph_2'}).get_text()
    if Potch2 == Potch2_Full:

        print(Fore.RED + "Sorry the service is still full: Potch Second service service")
        print(Style.RESET_ALL)
    else:
        print(Fore.GREEN +Potch2)
        print(Style.RESET_ALL)
        telegram_bot_sendtext(Potch2)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))


def telegram_bot_sendtext(bot_message) -> object:
    bot_token = '1470823420:AAHTdHwIgxtozQcDOYQFV0eRb31JZ5ThA-o'
    contact_ID = ['1132226909']
   # bot_chat = ['1132226909', '1331881872']
    #bot_chatID = []
    #bot_chatID = ('1132226909','1331881872')
   # print(len(contact_ID))
    for i in range(len(contact_ID)):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + contact_ID[i] + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
      #  print(response.json())

       # return response.json()



#ijbnrcrfvbieuaew
i = 0
while True:
    os.system("cls")
    i = i+1
    time = datetime.now()
    time = time.time()
    now = (str(time.hour) + ':' + str(time.minute) + ':' + str(time.second))
    print(Fore.GREEN + now)
    print("===============================================================")
    print(Style.RESET_ALL)
    check_services()
    print(Fore.GREEN +"===============================================================")
    print(Style.RESET_ALL)
    print(Fore.BLUE + str(i))
    print(Style.RESET_ALL)
    sleep(10)
    print("\n")