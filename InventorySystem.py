""" Crea un programa que simule un pequeño sistema de inventario para una tienda.
Requisitos:
1.Usa un diccionario para almacenar los productos y su cantidad en inventario.
2.Muestra un menú en el que el usuario pueda:

    Agregar un producto al inventario.

    Vender un producto (disminuir su cantidad en inventario).

    Mostrar el inventario.

    Salir del programa.
3.Usa while para que el menú se repita hasta que el usuario decida salir.
4.Usa if...else para manejar las opciones del menú y validar si un producto está en el inventario.
"""
import json
from Bank import load_balance, save_balance
# Nombre del archivo donde guardaremos el inventario
INVENTORY_FILE = "inventory.json"

# Cargar el inventario desde el archivo JSON
def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            data = json.load(file)
            # Convertir productos antiguos (números) al nuevo formato
            for product, details in data.items():
                if isinstance(details, int):  # Si el producto solo tiene cantidad y no precio
                    data[product] = {"quantity": details, "price": 0.0}  # Precio por defecto 0.0
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

# Guardar el inventario en el archivo JSON
def save_inventory():
    with open(INVENTORY_FILE, "w") as file:
        json.dump(inventory, file, indent=4)

inventory = load_inventory()  #CAMBIO: Cargar el inventario al inicio del programa

def add_product(): #In this function, we add a product to the inventory.
    product= input("Enter the name of the product: ").lower() #we ask the user to enter the name of the product.
    quantity= int(input("Enter the quantity of the product that enter in the inventory: ")) #we ask the user to enter the quantity of the product.
    
    if product in inventory:
        inventory[product]["quantity"] += quantity  # Si el producto ya existe, sumamos la cantidad
    else:
        price= float(input("Enter the price of the product: ")) #we ask the user to enter the price of the product.
        inventory[product] = {"quantity": quantity, "price": price}  # Si es un nuevo producto, lo agregamos
    save_inventory()
    print(f"{quantity} units of {product} added to inventory.")
    


def sell_product():
    product = input("Enter the name of the product: ").lower()

    if product in inventory:
        quantity = int(input("Enter the quantity of the product that you want to sell: "))

        if inventory[product]["quantity"] >= quantity:
            total_price = inventory[product]["price"] * quantity  # Calcular el costo total

            balance = load_balance()  # Obtener saldo actual del banco
            if balance >= total_price:  # Verificar si el usuario tiene suficiente dinero
                inventory[product]["quantity"] -= quantity  # Restar productos vendidos
                
                if inventory[product]["quantity"] == 0:
                    del inventory[product]  # Eliminar producto si no queda stock
                
                balance -= total_price  # Descontar del saldo
                save_balance(balance)  # Guardar el nuevo saldo

                save_inventory()   
                print(f"Product sold. ${total_price} deducted from your balance.")
            else:
                print("Insufficient balance to purchase the product.")
        else:
            print("Not enough quantity in the inventory.")
    else:
        print("Product not found in inventory.")

def show_inventory():
    print("***Inventory***")
    if not inventory:
        print("The inventory is empty.")
    else:
        for product, details in inventory.items():
             print(f"{product}: {details['quantity']} units - ${details['price']} each")

if __name__ == "__main__":
    while True:
        print("\nMenu:")
        print("1. Add product to inventory")
        print("2. Sell product")
        print("3. Show inventory")
        print("4. Exit")
        option= int(input("Enter an option: ")) #we ask the user to enter an option.

        if option== 1: #This is a conditional statement that check if the option is 1.
            add_product() #If the option is 1, we call the add_product function.
        elif option==2:
            sell_product()
        elif option==3:
            show_inventory()
        elif option==4:
            break
        else:
            print("Invalid option. Try again.")
