words = ["abc", "car", "ada", "racecar", "cool"]

for word in words:
    if word == word[::-1]:
        print(word)
