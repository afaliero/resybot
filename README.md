# resybot
A simple Python program to automatically reserve a table via Resy at a specified time.

Instructions: 
- Find a reservation you like on Resy and get its venue id by looking at the requests in the network tab in dev tools.
- Add the restaurant name and venue id to `rids` in ResyParams.py.
- Edit the `WHEN_TO_RESERVE` variable in ResyParams.py so that it represents the date and time reservations are released for the restaurant you want.
- Adjust the `TIME` variable in ResyParams.py based on the time at which you want your reservation to be. Keep in mind that the program will find the closest time slot to `TIME`, so it could end up being earlier or later. 
- Adjust `PARTY_SIZE` in ResyParams.py. 
- Add your credentials to the corresponding params in LoginSession.getCredentials()
- Run src/Main.py a few minutes before reservations are released and follow the terminal prompts. 
