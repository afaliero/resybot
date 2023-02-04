from datetime import datetime 

class ResyParams:
    def __init__(self, restaurant_name, res_date):
        self.restaurant_name = restaurant_name
        self.venue_id = self.rids[self.restaurant_name]
        # desired reservation date 
        self.reservation_date = res_date if res_date else '2023-01-28' 

    # Resy venue ids with release times 
    rids = {
        "4 Charles": "834", # 9am 30 days before 
        "Carbone": "6194", # 10am 30 days before
        "Coletta": "58982", # tester
        "Cote": "35676", # 10am 30 days before 
        "Don Angie": "1505", # 9am 7 days in advance
        "I Sodi": "443", # 12am 14 days in advance
        "L'Artusi": "25973", # 9am 2 weeks before
        "Lilia": "418", # via phone at 10am 30 days before; leftovers on Resy at 12am
        "Rezdora": "5771", # 12am 21 days in advance
        "Sadelle's": "29967",
        "The Nines": "7490", # 12am 2 weeks before 
        "Via Carota": "2567" # 10am 30 days before 
         }

    AUTH_TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJleHAiOjE2Nzc2NDE0NTYsInVpZCI6OTA5MTc4LCJndCI6ImNvbnN1bWVyIiwiZ3MiOltdLCJsYW5nIjoiZW4tdXMiLCJleHRyYSI6eyJndWVzdF9pZCI6NzA5NjE1Nn19.AcL1ePbuF5cZJWIc1bck7dKoh3kUxCu2T2H0cP922T-x8j_PGKHSeJwga98uw4F3MhKHM02GiDRKPpQTA0bHrkz6AJuGi9gXTQ-9nZfPeSqOktUtHEz5CcMeE6O5zg3WOUaoZUrxE60uXtT9E47K1IvvCDUP5tk6bm1oeYaqZh0UqU-i'
    PAYMENT_METHOD = None
    TIME = datetime.strptime('18:30:00', '%H:%M:%S') 
    PARTY_SIZE = '2'
    WHEN_TO_RESERVE = datetime.strptime('2023-02-04 10:00:00', '%Y-%m-%d %H:%M:%S') # time reservations are released

