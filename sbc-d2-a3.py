from random import randint
#swertres
taya1 = int(input("Enter first number (0-9):"))
taya2 = int(input("Enter second number (0-9):"))
taya3 = int(input("Enter third number (0-9):"))

result1 = randint(0,9)
result2 = randint(0,9)
result3 = randint(0,9)

print("Taya nimo:", taya1, taya2, taya3)
print("Result:", result1, result2, result3)

if (taya1 == result1 and taya2 == result2 and taya3 == result3):
    print("You Win!")
else:
    bet = [taya1, taya2, taya3]
    result = [result1, result2, result3]

    if sorted(bet) == sorted(result):
        print("You Partially Win!")
    else:
        print("You Lose!")