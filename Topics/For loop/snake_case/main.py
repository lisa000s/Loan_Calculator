word = input()
str = ""
for letter in word:
    if letter.isupper():
        str = str + "_" + letter.lower()
    else:
        str = str + letter
print(str)