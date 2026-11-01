LOGO = r"""
  _  __ ___  ____  ___
 | |/ /|_ _|/ ___||_ _|
 | ' /  | | \___ \ | |
 | . \  | |  ___) || |
 |_|\_\|___||____/|___|
   data . automation . ai
   > Tagerechner  v0.1
"""
print(LOGO)

def find_total_days(years, months, days):
    my_days = (years * 365) + (months * 30) + days
    return my_days

print("Willkommen beim Tagerechner!\n")

years = int(input("Wie viele Jahre? "))
months = int(input("Wie viele Monate? "))
days = int(input("Wie viele Tage? "))

total = find_total_days(years, months, days)

tage_formatiert = f"{total:,}".replace(",", ".")

print("\n\033[92m========================================")
print(f"       ERGEBNIS: ca. {tage_formatiert} TAGE")
print("========================================\033[0m")

print()
input("Enter drücken zum Beenden ...")