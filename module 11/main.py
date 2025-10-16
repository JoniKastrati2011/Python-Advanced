file_path = "example.txt"
# file = open(file_path, "r")
#
#
# content = file.read()
# print(content)

# with open(file_path, "r")as file:
#     content = file.read()
#     print(content)

# "r"Read only mode
# "w"Write
# "a"Append
# "b" Binary mode
# "x"Exclusive creation

# with open("example.txt", "r")as file:
#     line1 = file.readlines()
#     print(line1)


# with open(file_path, "w")as file:
#     file.write("Hello World!")
#
# lines = ['Hello World', 'Welcome to Python']
# with open(file_path, "w")as file:
#     file.writelines(lines)

# with open(file_path,"a")as file:
#     file.write("New data append")

data = b"This is some binary data"
# with open('example.bin', 'wb')as file:
#     file.write(data)

# with open(file_path, "rb") as file:
#     data = file.read()

with open(file_path) as file:
    for line in file:
        clean_line = line.strip()
        print(clean_line)

with open("example.txt") as file:
    for line in file:
        words = line.strip().split()
        print(words)

name = "Rubik"
age = 2

with open("example.txt", "a") as file:
    file.write("Name"+ name+ "\nAge" + str(age))

with open("example.txt", "a") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")