class BankAccount:
    def __init__(self, balance=0):
        self.__balance = 0
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        if value < 0:
            print("Баланс не може бути від’ємним! Значення не змінено.")
        else:
            self.__balance = value

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Внесено: {amount}")
        else:
            print("Сума внеску повинна бути додатньою!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Сума зняття повинна бути додатньою!")
        elif amount > self.__balance:
            print("Недостатньо коштів!")
        else:
            self.__balance -= amount
            print(f"Знято: {amount}")



account = BankAccount(100)
print("Початковий баланс:", account.balance)

account.deposit(50)
print("Баланс після поповнення:", account.balance)

account.withdraw(30)
print("Баланс після зняття:", account.balance)

account.balance = -500
print("Баланс після спроби прямої зміни:", account.balance)
