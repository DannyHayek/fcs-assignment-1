age = int(input("Please enter your age: "))

if age < 10:
    price = 0
elif age < 19:
    price = 4
elif age < 25:          #The idea here is that if the user is strictly less than 10 or more than 50 years old then they are not allowed to watch the movie
    price = 7
elif age < 36:
    price = 10
elif age < 51:
    price = 20
else:
    price = 0


if price == 0:
    print("You are not allowed to view this movie!")
else:
    print("The ticket price is " + str(price) + "$.")