import csv

file_path = "C:\\Users\\Мария\\Downloads\\airport-codes_csv.csv"

with open(file_path, mode="r", encoding="utf-8") as file:
    readable_file = csv.DictReader(file, delimiter=";")

    for airport in readable_file:
        if "iso_country" in airport and airport["iso_country"] == "UA":
            print(airport["name"])
