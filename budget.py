class Category:
    def __init__(self, category):
        self.category = category
        self.amount = 0
        self.ledger = []

    def deposit(self, amount, description=''):
        self.ledger.append({
            "amount": amount,
            "description": description,
        })
        self.amount += amount

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({
                "amount": -amount,
                "description": description
            })
            self.amount -= amount
            return True
        return False

    def get_balance(self):
        return self.amount

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category}")
            self.amount -= amount

            category.deposit(amount, f"Transfer from {self.category}")
            category.amount += amount
            return True
        return False

    def check_funds(self, amount):
        if amount > self.amount:
            return False
        return True

    def __str__(self):
        max_length = 30
        description_length = 23
        result = ""
        result += self.category.center(max_length, '*') + '\n'
        for row in self.ledger:
            result += row["description"][:description_length] + \
                "{:,.2f}".format(row["amount"]).rjust(
                    max_length - len(row["description"])) + "\n"
        result += f"Total: {self.amount}"
        return result


def create_spend_chart(categories):
    indicator = "o"
    result = ""
    result += "Percentage spent by category \n"
    for row in range(100, -10, -10):
        result += str(row).rjust(3) + "|"
    return result
