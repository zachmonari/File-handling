with open('file.txt', 'w') as file:
    file.write('Hello World!')
with open('file.txt', 'a') as file:
    file.write('\nMy name is Walker!')
with open('file.txt', 'r') as file:
    contents = file.read()
print(contents)