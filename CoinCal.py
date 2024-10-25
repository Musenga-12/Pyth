def get_change():
    accepted_coins = [25, 10, 5]
    total_amount = 0
    
    while total_amount < 50:
        coin = int(input("Insert a coin (25, 10, 5): "))
        if coin in accepted_coins:
            total_amount += coin
            print(f"Total amount: {total_amount} cents")
        else:
            print("Coin not accepted.")
    
    change = total_amount - 50
    print(f"You owe {change} cents in change.")

get_change()