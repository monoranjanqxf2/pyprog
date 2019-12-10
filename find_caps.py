text = input("Enter your text here :")
count = 0
for letter in text:
    if letter.isupper():
        count += 1
        print(letter)
print(f'Number of capital letter is : {count}')
