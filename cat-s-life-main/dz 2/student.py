import secrets

class Student:
    def __init__(self, name, money=0):
        self.name = name
        self.money = money

    def __str__(self):
        return (f'Name - {self.name}\n'
                f'Money - {self.money}\n')

    def earn_money(self, amount):
        self.money += amount
        print(f"{self.name} earned {amount} money. Total money: {self.money}")

    def spend_money(self, amount):
        if self.money >= amount:
            self.money -= amount
            print(f"{self.name} spent {amount} money. Total money: {self.money}")
        else:
            print(f"{self.name} doesn't have enough money to spend {amount}.")

    def study(self):
        print(f"{self.name} is studying.")

    def work(self):
        earnings = secrets.randbelow(21) + 10  # Від 10 до 30
        self.earn_money(earnings)
        print(f"{self.name} was working and earned {earnings} money.")

    def live_one_year(self):
        for _ in range(365):
            action = secrets.choice(["study", "work"])
            if action == "study":
                self.study()
            elif action == "work":
                self.work()

