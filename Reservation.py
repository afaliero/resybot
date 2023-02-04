from datetime import datetime
import requests
import ResyParams 
import sys 
import time

class Reservation:

	def __init__(self, resyParams: ResyParams):
		self.resyParams = resyParams


	def get_best_table(self, time, headers):
		params = (
			('x-resy-auth-token', self.resyParams.AUTH_TOKEN),
			('day', self.resyParams.reservation_date),
			('lat', '0'),
			('long', '0'),
			('party_size', self.resyParams.PARTY_SIZE),
			('venue_id', self.resyParams.venue_id)
		)
		response = requests.get('https://api.resy.com/4/find', headers=headers, params=params)
		venues = response.json()['results']['venues']
		if not venues:
			print("Sorry, no reservations have been released for " + self.resyParams.reservation_date)
			return

		available_tables = venues[0]['slots']

		if len(available_tables) == 0:
			print("Sorry, no available tables on " + self.resyParams.reservation_date)
			return 

		# get table closest to TIME 
		best_table = available_tables[0]
		for table in available_tables:
			best_table = self.compare_tables(best_table, table)
		return best_table 
			
	# compares two tables and returns table with better reservation time (better = closer to TIME) 
	def compare_tables(self, table1, table2): 
		table1_time = datetime.strptime(table1['date']['start'].split(" ")[1], '%H:%M:%S')
		table2_time = datetime.strptime(table2['date']['start'].split(" ")[1], '%H:%M:%S')

		table1_time_diff = abs(table1_time - self.resyParams.TIME)
		table2_time_diff = abs(table2_time - self.resyParams.TIME)

		if table1_time.hour <= 17 and table2_time.hour > 17:
			return table2 
		elif table2_time.hour <= 17 and table1_time.hour > 17:
			return table1 

		return table1 if table1_time_diff < table2_time_diff else table2


	def make_reservation(self, best_table, headers):
		if best_table:
			params = (
				('x-resy-auth-token', self.resyParams.AUTH_TOKEN),
				('config_id', str(best_table['config']['token'])),
				('day', self.resyParams.reservation_date
				),
				('party_size', self.resyParams.PARTY_SIZE)
			)
			request = requests.get('https://api.resy.com/3/details', headers=headers, params=params)
			details = request.json() 
			book_token = details['book_token']['value']
			headers['x-resy-auth-token'] = self.resyParams.AUTH_TOKEN
			data = {
				'book_token': book_token,
				'struct_payment_method': self.resyParams.PAYMENT_METHOD,
				'source_id': 'resy.com-venue-details'
			}
			response = requests.post('https://api.resy.com/3/book', headers=headers, data=data)
			return response 
