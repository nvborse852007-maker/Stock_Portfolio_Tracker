# Stock Portfolio Tracker

# Dictionary containing stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "MSFT": 420
}

portfolio = {}
total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

# Get the number of stocks
num_stocks = int(input("How many different stocks do you own? "))

# Get stock details
for i in range(num_stocks):
    stock_name = input("Enter stock symbol: ").upper()

    if stock_name not in stock_prices:
        print("Stock not found! Please try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    price = stock_prices[stock_name]
    investment_value = price * quantity

    # Store stock quantity
    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    # Calculate total investment
    total_investment += investment_value
print(f"{stock_name}: {quantity} x ${price} = ${investment_value}")

# Display portfolio summary
print("\n===== Portfolio Summary =====")

for stock_name, quantity in portfolio.items():
    value = stock_prices[stock_name] * quantity
    print(f"{stock_name}: {quantity} shares = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

# Save results to a text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")

    for stock_name, quantity in portfolio.items():
        value = stock_prices[stock_name] * quantity
        file.write(f"{stock_name}: {quantity} shares = ${value}\n")

    file.write(f"Total Investment Value: ${total_investment}\n")

print("Portfolio saved successfully to portfolio.txt")