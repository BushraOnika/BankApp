def get_operation_and_amount(line: str) -> (str, float):
    """
    :returns:
    tuple: (operation string, amount float)

    >>> get_operation_and_amount("--deposit 100")
    ('deposit', 100.0)
    >>> get_operation_and_amount("--withdraw 50.5")
    ('withdraw', 50.5)
    >>> get_operation_and_amount("--deposit 75")
    ('deposit', 75.0)
    """

    words = line.split(" ")
    operation_with_flag = words[0]  # [x] [ ]
    operation = operation_with_flag[2:]  # to remove double dash (--)
    amount = float(words[1])  # [ ] [x]
    return operation, amount


def update(operation: str, balance: float, amount: float, charge: float) -> (float, str):
    """
    :param operation:
    :param balance:
    :param amount:
    :param charge:
    :return:
    tuple: (amount float, message string)

    >>> update("deposit", 0, 100, 5)
    (95, 'hidden fee: -5')
    >>> update("withdraw", 200, 100, 5)
    (95, 'hidden fee: -5')
    >>> update("invalid", 100, 50, 5)
    'not supported'
    """
    match operation:
        case "deposit":
            return deposit(balance, amount, charge)
        case "withdraw":
            return withdraw(balance, amount, charge)
        case _:
            return "not supported"


def deposit(balance: float, amount: float, charge: float) -> (float, str):
    """
    :param amount:
    :param balance:
    :param charge:
    :returns:
    new_balance (float)
    message (str)

    >>> deposit(0, 100, 5)
    (95, 'hidden fee: -5')
    >>> deposit(100, 0, 5)
    (100, 'non-positive not supported')
    >>> deposit(0, 5, 5)
    (0, 'insufficient fund for charge')

    """
    if amount <= 0:
        return balance, f"non-positive not supported"

    new_balance = balance + amount - charge

    if new_balance <= charge:
        return balance, f"insufficient fund for charge"

    return new_balance, f"hidden fee: -{charge}"


def withdraw(balance: float, amount: float, charge: float):
    """
        :param amount:
        :param balance:
        :param charge:
        :returns:
        new_balance (float)
        message (str)

        >>> withdraw(200, 100, 5)
        (95, 'hidden fee: -5')
        >>> withdraw(0, 100, 5)
        (0, 'Insufficient balance')
        >>> withdraw(0, 0, 5)
        (0, 'non-positive not supported')
    """

    if amount <= 0:
        return balance, f"non-positive not supported"

    new_balance = balance - charge - amount
    if new_balance < 0:
        return balance, "Insufficient balance"
    else:
        return new_balance, f"hidden fee: -{charge}"


def process(balance: float, charge: float) -> (float, str):
    args = input("""Chose an option:
--deposit   x amount
--withdraw  x amount
""")
    (operation, amount) = get_operation_and_amount(line=args)
    return update(operation, balance, amount, charge)


if __name__ == '__main__':
    hidden_charge = 5
    balance = 0
    while True:
        print("--------------------")
        balance, msg = process(balance, hidden_charge)
        print(msg)
        print("--------------------")
        print(f'current balance {balance}', end="\n")
        print("--------------------", end="\n\n")
