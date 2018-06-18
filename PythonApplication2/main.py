import collat
while True:
    try:
        userInput = int(input("Enter a number: "))
    except ValueError:
        print("Enter a whole number, try again.")
        continue
    else:
        break

while (userInput != 1):
    userInput = collat.collatz(userInput)