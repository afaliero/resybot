from datetime import datetime 

class ResyParams:

    rids = {"Carbone": "6194"}

    AUTH_TOKEN = None
    PAYMENT_METHOD = None
    RESERVATION_DATE = '2022-09-17' # desired reservation date 
    TIME = datetime.strptime('20:00:00', '%H:%M:%S') 
    VENUE_ID = rids["Carbone"]
    PARTY_SIZE = '2'
    WHEN_TO_RESERVE = datetime.strptime('2022-11-13 20:07:00', '%Y-%m-%d %H:%M:%S') # time reservations are released

