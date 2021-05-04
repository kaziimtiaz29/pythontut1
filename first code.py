'''number1 = input("Enter whole number: ")
number2 = input("Enter decimal number: ")

integer_number = int(number1)
float_number = float(number2)
round_number = int(round(float_number))

print(number1)
print(number2)
print(round_number)
'''
def add_calc(number1, number2):
    answer = number1 + number2
    return answer
number1= int(input("input1:"))
number2= int(input("input2:"))
added_number = add_calc(number1,number2)

print(added_number + 20)