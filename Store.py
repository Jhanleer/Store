import json
import Bank
import InventorySystem

def buy_product():
    print("\n📦 Available Inventory:")
    inventory = InventorySystem.load_inventory()
    
    for product, details in inventory.items():
        print(f"- {product}: {details['quantity']} units - ${details['price']} each")

    product = input("\nEnter the product you want to buy: ").lower()
    
    if product not in inventory:
        print("❌ Product does not exist.")
        return

    quantity = int(input(f"Enter quantity of {product} you want to buy: "))
    
    # Verificar si hay suficiente stock
    if inventory[product]['quantity'] < quantity:
        print("❌ Not enough stock.")
        return

    price = inventory[product]["price"]
    total_cost = price * quantity

    # Obtener saldo del banco
    balance = Bank.load_balance()

    if balance >= total_cost:
        # Actualizar inventario y saldo
        InventorySystem.sell_product()
        Bank.load_balance(balance - total_cost)  # Asumiendo que tienes una función para actualizar el balance
        print(f"✅ You bought {quantity} {product}(s) for ${total_cost:.2f}.")
    else:
        print("❌ Insufficient balance.")

# Menú de la tienda
while True:
    print("\n📍 Store Menu:")
    print("1. Show balance")
    print("2. Show inventory")
    print("3. Buy product")
    print("4. Exit")

    option = int(input("Enter an option: "))

    if option == 1:
        print(f"\n💰 Your current balance: ${Bank.load_balance():.2f}")
    elif option == 2:
        print("\n📦 Available Inventory:")
        inventory = InventorySystem.load_inventory()
        for product, details in inventory.items():
            print(f"- {product}: {details['quantity']} units - ${details['price']} each")
    elif option == 3:
        buy_product()
    elif option == 4:
        print("👋 Exiting store. See you soon!")
        break
    else:
        print("❌ Invalid option. Try again.")
