class Bank:
    def __init__(self, holder_name, initial_deposit):
        self.holder_name = holder_name
        self.balance = initial_deposit


user1 = Bank('chooto bro', 10000)


print(user1.holder_name)