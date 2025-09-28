# with automatically opens and closes the file for us.
# It prevents errors and makes our code cleaner.
with open('file.txt', 'w') as file:
    file.write('Hello World!')
with open('file.txt', 'a') as file:
    file.write('\nMy name is Walker!')
with open('file.txt', 'r') as file:
    contents = file.read()
print(contents)
# File 2
entry=input("Enter your diary entry: ")
with open('diary.txt', 'a') as file:
    file.write(entry+"\n")
# File 3
entry=input("Enter your name and score: ")
with open("scores.txt","a") as file:
    file.write(entry+"\n")
with open("scores.txt", "r") as file:
    contents=file.read()
print(contents)
