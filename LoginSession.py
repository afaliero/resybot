import requests 

class LoginSession:

    def getCredentials(self):
        print("Log into Resy\n")
        # email = input("Email: ")
        # password = input("Password: ")
        return {
            'email': "may1themovie@aol.com",
            'password': "Jmr27z92-r"
        }

    def login(self, headers):
        data = self.getCredentials()
        response = requests.post('https://api.resy.com/3/auth/password', headers=headers, data=data).json()
        AUTH_TOKEN = response['token']
        PAYMENT_METHOD = '{"id":' + str(response['payment_method_id']) + '}'
        return AUTH_TOKEN, PAYMENT_METHOD