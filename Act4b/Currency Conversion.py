import csv

def load_currency_rates(filename):
    rates = {}
    with open(filename, 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            code, name, rate_str = row
            rates[code.strip().upper()] = (name.strip(), float(rate_str))
    return rates

def main():
    data = load_currency_rates('currency.csv')
    dollars = float(input("How much dollar do you have? "))
    target = input("What currency you want to have? ").strip().upper()
    if target in data:
        name, rate = data[target]
        converted = dollars * rate
        print(f"\nDollar: {dollars} USD")
        print(f"{name}: {converted}")
    else:
        print("Currency not found.")

if __name__ == '__main__':
    main()
