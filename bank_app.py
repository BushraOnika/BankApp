input_what_type=input("Press 1 for deposite or press 2 for withdraw\n")
total = 0
hidden_charge=5
print("Current Balance: ",total+int(input("Enter the amount you want to deposite\n"))-hidden_charge) if input_what_type == "1" else print("Current Balance: ",total-int(input("Enter the amount ypu want to withdraw\n"))-hidden_charge)

