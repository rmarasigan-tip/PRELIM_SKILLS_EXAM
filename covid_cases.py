import json
import csv

with open('covid_cases.json','r') as file:
    json = json.load(file)

filename = "data.csv"

with open('data.csv','w') as data_file:
    covid_data = csv.writer(data_file)
    covid_data.writerow(["Data Reported","Countries and Territories","Number of Cases","Deaths"])
    for item in json["records"]:
        covid_data.writerow([item['dateRep'],item['countriesAndTerritories'],item['cases'],item['deaths']])


