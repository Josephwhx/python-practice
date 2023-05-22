# While loop
number = 7
user_input = input("Would you like to play? (Y/n): ").lower()

while user_input != 'n':
    user_number = int((input("Guess our number: ")))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("you were off by one.")
    else:
        print("Sorry, it's wrong")

# For loop
friends = ["Rolf", "Jen", "Bob", "Annie"]

for friend in friends:
    print(f"{friend} is my friend.")


grades = [35, 67, 98, 100, 100]
total = 0
total_sum = sum(grades)
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)