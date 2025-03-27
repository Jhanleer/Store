"""
Crear un sistema de cajero/banco en Python que permita a los usuarios gestionar su dinero y 
conectarlo a un sistema de inventario.

✅ Ver saldo: Consultar cuánto dinero hay en la cuenta.

✅ Depositar dinero: Aumentar el saldo ingresando una cantidad.

✅ Retirar dinero: Disminuir el saldo, asegurando que no se retire más de lo disponible.

✅ Guardar el saldo en un archivo JSON para persistencia.
"""
import json

BANK_FILE = "bank.json"

def load_balance():#This function load the balance from the bank file.
    try:
        with open(BANK_FILE, "r") as file:
            data = json.load(file)
            return data.get("balance", 0) # Obtener el saldo o 0 si no existe
    except (FileNotFoundError, json.JSONDecodeError):
        return 0
    

def save_balance(balance):
    with open(BANK_FILE, "w") as file:
        json.dump({"balance": balance}, file, indent=4)



def show_balance(balance):
    print(f"Your balance is: ${balance}")

def deposit(balance):
    
    amount= float(input("Enter the amount you want to deposit: "))
    balance += amount
    save_balance(balance)
    print(f"${amount} deposited successfully.")
    return balance

def withdraw(balance): 
    amount= float(input("Enter the amount you want to withdraw: "))#we ask the user to enter the amount that he want to withdraw.
    if amount <= balance: #This is a conditional statement that check if the amount that the user want to withdraw is less than or equal to the balance.
        balance -= amount
        save_balance(balance)
        print(f"${amount} withdrawn successfully.")
    else:
        print("Insufficient funds.")
    return balance

if __name__ == "__main__":
    balance= load_balance()
    
    while True:
            print("1. Show balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            option= int(input("Enter an option: ")) #we ask the user to enter an option.
            if option ==1:
                show_balance(balance)
            elif option ==2:
                deposit(balance)
            elif option ==3:
                withdraw(balance)
            elif option ==4:
                break
            else:
                print("Invalid option.")

 # Llamamos la función principal para iniciar el programa.
