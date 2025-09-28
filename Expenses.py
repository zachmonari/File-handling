while True:
    item=input("Enter the item bought ('quit' to stop): ")
    if item.lower() == "quit":
        break
    amount=input("Enter the amount spent on the item: ")
    with open("Expenses.txt", "a") as file:
        file.write(item+": Ksh" +amount+"\n")

with open("Expenses.txt", "r") as file:
    print("Here are all your expenses saved!")
    print(file.read())