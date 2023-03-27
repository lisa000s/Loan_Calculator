phone_number = input()
digits = ['zero','one','two','three','four','five','six','seven','eight','nine']
for i in phone_number:
    for j in range(0, len(digits)):
        if int(i) == j:
            print(digits[j])
            continue
