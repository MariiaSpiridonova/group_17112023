# from pprint import pprint
import requests

url = "https://script.google.com/macros/s/AKfycbzNj_WQBs8X-kViKIenVNsnqIzvReBG9xKUUUtgx7WfIdcn8AIYsXLZxn41za1EOCPGOw/exec"

response = requests.get(url=url)
data_from_sheets = response.json()
# pprint(persons)

sum_income_large_over35 = 0
large_families_count = 0
families_loans_over_income = 0
woman_owns_flat = 0

for person in data_from_sheets["people"]:
    if person["age"] > 35 and person["many_kids"] is True:
        sum_income_large_over35 += person["income"]
    if person["many_kids"] is True:
        large_families_count += 1
    if person["income"] < person["loan_payment"]:
        families_loans_over_income += 1
    if person["gender"] == "female" and person["owns_house"] is True:
        woman_owns_flat += 1

print(f"Місячний дохід людей, сім'я яких є багатодітною і вік яких більше 35 років: {sum_income_large_over35}")
print(f"Кількість багатодітних сімей:  {large_families_count}")
print(f"Кількість сімей, в яких витрати за кредитами більші за доходи: {families_loans_over_income}")
print(f"Кількість жінок які забезпечені власним житлом: {woman_owns_flat}")
