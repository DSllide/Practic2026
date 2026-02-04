class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print(f"Внесено: {amount} грн")
        else:
            print("Сума внеску повинна бути додатньою!")

    def withdraw(self, amount):

        if amount > self.__balance:
            print("Недостатньо коштів!")
        elif amount <= 0:
            print("Сума зняття повинна бути додатньою!")
        else:
            self.__balance -= amount
            print(f"Знято: {amount} грн")

    def get_balance(self):

        return self.__balance



account = BankAccount(1000)
print("Початковий баланс:", account.get_balance())


account.deposit(500)
print("Баланс після поповнення:", account.get_balance())


account.withdraw(300)
print("Баланс після зняття:", account.get_balance())


print("\nСпроба прямого доступу до __balance:")
try:
    account.__balance = 100000
except AttributeError as e:
    print(e)

print("Баланс після спроби прямого доступу:", account.get_balance())
