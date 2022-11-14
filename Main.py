from datetime import datetime 
import LoginSession
import Reservation
import ResyParams

class Main:

    def main(self):
        headers = {	 
	'authorization': 'ResyAPI api_key="VbWk7s3L4KiK5fzlO7JD3Q5EYolJI7n5"',
	'accept-encoding': 'gzip, deflate, br',
	'access-control-request-headers': 'authorization,cache-control,x-origin,x-resy-auth-token,x-resy-universal-auth',
    }
        session = LoginSession.LoginSession()
        resyParams = ResyParams.ResyParams()
        reservation = Reservation.Reservation(resyParams)

        # retrieve and set auth token and payment method by logging in
        resyParams.AUTH_TOKEN, resyParams.PAYMENT_METHOD = session.login(headers) 

        while True:
            if datetime.now() >= resyParams.WHEN_TO_RESERVE:
                print("reserving...")
                table = reservation.get_best_table(reservation.resyParams.TIME, headers)
                reservation.make_reservation(table, headers) 
                return


Main().main()