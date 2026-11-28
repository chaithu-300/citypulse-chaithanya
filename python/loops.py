for number in range(1,6):
    print(number)

for language in ["Python","C++", "Java Script"]:
    print(language)

for letter in "Python":
    print(letter)


count = 1

while  count < 10:
    print(count)
    count += 1


for number in range(1, 10):
    if number == 5:
        break
    print(number)

for number in range(1, 20):
    if number == 10:
        break
    if number == 5:
        continue

password = "QWERTYqwerty12#"

Password = input("enter your password: ")

while password == Password:
    print("password is correct")
    break
else:
    print("password is wrong try again")