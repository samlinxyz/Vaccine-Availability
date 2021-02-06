import requests
from playsound import playsound
from time import sleep

vaccine_sites_and_unavailability_messages = {
    "https://www.memorialhermann.org/services/conditions/coronavirus/covid-19-vaccine-frequently-asked-questions": "At this time, due to limited vaccine supply, all COVID-19 vaccination appointments are full.",
    "https://uthtmc.az1.qualtrics.com/jfe/form/SV_aafBE5i1QEk0RLg": "This link has been deactivated.",
    "https://www.clockwisemd.com/hospitals/4513/appointments/new": "There are no visit times available for online scheduling right now.  Please try back later to schedule your appointment.",
}

def check_vaccine_websites(sites_and_unavailability_messages):
    for website_url, error_message in sites_and_unavailability_messages.items():
        try: 
            if error_message not in requests.get(website_url).text:
                return website_url
        except ConnectionError:
            print("ConnectionError from", website_url)
    return None

def main():

    while (available_website := check_vaccine_websites(vaccine_sites_and_unavailability_messages)) is None:
        print("Nothing yet...")
        sleep(150)

    print(available_website)
    playsound('C:/Users/Milkman/Documents/GitHub/Vaccine-Availability/melt.mp3')

if __name__ == "__main__":
    main()