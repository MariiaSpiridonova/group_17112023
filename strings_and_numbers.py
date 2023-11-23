import decimal

print("\U00000F04" * 40)

name = input("Enter your name >>> ").strip().title()
age = input("Enter you age >>> ")
avg_salary = input("Enter your average salary per month in UAH >>> ")

years_to_pension = 65 - int(age)
income_uah = int(years_to_pension) * 12 * float(avg_salary)
income_usd = decimal.Decimal(income_uah / 37.3)
income_usd_round = income_usd.quantize(decimal.Decimal("0."))

cars_quantity = decimal.Decimal(income_usd / 31500)
cars_quantity_round = cars_quantity.quantize(decimal.Decimal("0."))

print(
    f"I, {name}, can earn only {income_usd_round} USD, that would be enough"
    f" only for {cars_quantity_round} cars.\nIt is not OK for me, "
    f"so I will be changing my life and obstinately learn programming!"
)
