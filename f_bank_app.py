def get_operation_and_amount(line: str) -> (str, float):
    """
    :rtype: (str, float)
    """

    words = line.split(" ")
    operation_with_flag = words[0]  # [x] [ ]
    operation = operation_with_flag[2:]  # to remove double dash (--)
    amount = float(words[1])  # [ ] [x]
    return operation, amount


def update(operation: str, amount: float, balance: float, hidden_fee: float) -> (float, str):
    if operation == 'deposit':
        return deposit(amount, balance, hidden_fee)
    elif operation == "withdraw":
        return withdraw(amount, balance, hidden_fee)
    else:
        return "spelling mistake continue..."


def deposit(amount: float, balance: float, hidden_fee: float) -> (float, str):
    balance += amount - hidden_fee
    return balance, f"hidden fee: -{hidden_fee}"


def withdraw(amount: float, balance: float, hidden_fee: float):
    balance_after_fee = balance - hidden_fee - amount
    if balance_after_fee <= balance:
        balance = balance_after_fee
        return balance, f"hidden fee: -{hidden_fee}"
    else:
        return balance, "Insufficient balance"


def process(balance: float, hidden_charge: float) -> (float, str):
    args = input("""Chose an option:
--deposit   x amount
--withdraw  x amount
""")
    (operation, amount) = get_operation_and_amount(line=args)
    return update(operation, amount, balance, hidden_charge)


if __name__ == '__main__':
    hidden_charge = 5
    balance = 0
    while True:
        balance, msg = process(balance, hidden_charge)
        print(msg)
        print("--------------------")
        print(f'current balance {balance}', end="\n\n")
