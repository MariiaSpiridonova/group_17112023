given_string = (
    "6..58київ\nоДеса     Львів\tжитоМИР      уЖгОрОд ХарКІВ       слАвУтИч74$:?$"
)

cities = given_string.strip("45678.\n\t$:?").lower().title().split()

for city in cities:
    print(f"Я\U00002764{city}")
