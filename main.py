from src.converter import convert

def convert_currency():
    print("--- CURRENCY CONVERTER ---")
    print("1. USD to INR")
    print("2. EUR to INR")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ")
    
    if choice == '1':
        amount = float(input("Enter amount in USD: "))
        rate = 83.0
        result = convert(amount, rate)
        print(f"Result: {amount} USD = {result} INR")
    elif choice == '2':
        amount = float(input("Enter amount in EUR: "))
        rate = 90.0
        result = convert(amount, rate)
        print(f"Result: {amount} EUR = {result} INR")
    else:
        print("Exiting...")

if __name__ == "__main__":
    convert_currency()