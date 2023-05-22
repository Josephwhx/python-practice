numbers = [1, 3, 5]
doubled = []

for num in numbers:
    doubled.append(num * 2)

# Alternative
doubled = [x * 2 for x in numbers]

friends = ["Rolf", "Sam", "Samantha", "Saurabh", "Jen"]
starts_s = [friend for friend in friends if friend.startswith("s")]

print(starts_s)
