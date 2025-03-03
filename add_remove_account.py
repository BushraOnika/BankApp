def add_acount(acount:list[str]):
    return acount
def remove_account(name:str):
    for i in range(len(add_acount())):
        if(add_acount().index(i)==name):
            add_acount().remove(i)


c_or_d=input("Press 1 for create and Press 2 for delete: ")

if c_or_d=='1':
    add_acount(input())
else:
    remove_account(input())