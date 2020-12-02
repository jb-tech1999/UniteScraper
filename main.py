from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
import requests
import datetime

myUrl = 'https://unite180.com/church_bookings/booking.php'

#open up connection and grabbing HTML
uClient = uReq(myUrl)
page_html = uClient.read()
uClient.close()

def check_services():

    #HTML parser
    page_soup = soup(page_html, 'html.parser')

    HQ1_Full = 'Morning First Service  (07:55) (155/155)'
    HQ2_Full = 'Evening Service (16:55) (155/155)'
    HQ3_Full = 'Morning Second Service (09:55) (155/155)'

    Brook1_Full = 'Morning Service (09:00) (205/205)'
    Brook2_Full = 'Evening Service (17:00) (205/205)'

    HQ1 = page_soup.find('option', {'value': 'hq_1'}).get_text()
    if HQ1 == HQ1_Full:
        print("Sorry the service is still full: HQ Service 1")
    else:
        print(HQ1)
        telegram_bot_sendtext(HQ1)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))
       # send_mail('HQ First service')

    HQ2 = page_soup.find('option', {'value': 'hq_2'}).get_text()
    if HQ2 == HQ2_Full:
        print("Sorry the service is still full: HQ Service 2")
    else:
        print(HQ2)
        telegram_bot_sendtext(HQ2)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))

    HQ3 = page_soup.find('option', {'value': 'hq_3'}).get_text()
    if HQ3 == HQ3_Full:
        print("Sorry the service is still full: HQ Service 3")
    else:
        print(HQ3)
        telegram_bot_sendtext(HQ3)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))

    Brook1 = page_soup.find('option', {'value': 'bn_1'}).get_text()
    if Brook1 == Brook1_Full:
        print("Sorry the service is still full: Brooklyn Morning service")
    else:
        print(Brook1)
        telegram_bot_sendtext(Brook1)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))

    Brook2 = page_soup.find('option', {'value': 'bn_2'}).get_text()
    if Brook2 == Brook2_Full:
        print("Sorry the service is still full: Brooklyn Evening service")
    else:
        print(Brook2)
        telegram_bot_sendtext(Brook2)
        print(telegram_bot_sendtext('https://www.unite180.com/church\\_bookings/booking.php'))


def telegram_bot_sendtext(bot_message) -> object:
    bot_token = '1470823420:AAHTdHwIgxtozQcDOYQFV0eRb31JZ5ThA-o'
    contact_ID = ['1132226909']
   # bot_chat = ['1132226909', '1331881872']
    #bot_chatID = []
    #bot_chatID = ('1132226909','1331881872')
    print(len(contact_ID))
    for i in range(len(contact_ID)):
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + contact_ID[i] + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        print(response.json())

       # return response.json()



#ijbnrcrfvbieuaew
i = 0
while True:
    i = i+1
    print(datetime.datetime.now())
    check_services()
    print(i)
    time.sleep(10)
    print("\n")