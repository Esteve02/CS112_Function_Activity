print("BUTAD, JOHN ESTEVE")
print("CS112, COMPUTER PROGRAMMING 1")
def diff_num(num1, num2, num3):
    result = num1 + num2 + num3
    return result


def same_num(num1, num2, num3):
    result = num1 * num2 * num3
    return result


def same_second_num(num1, num2, num3):
    result = num1 * num2 + num3
    return result


def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input in ['yes', 'no']:
            return user_input

        else:
            print("Invalid input. Please enter 'yes' or 'no'")






while True:
    print("\nEnter a \"NUMBER\"")
    num1 = eval(input("Enter first number: "))
    num2 = eval(input("Enter second number: "))
    num3 = eval(input("Enter third number: "))
    num = num1, num2, num3
    if num1 != num2 and num3:
        print("Result is", diff_num(num1, num2, num3))

    elif num1 == num2 and num3:
        print("Result is", same_num(num1, num2, num3))

    elif num1 == num2 != num3:
        print("Result is", same_second_num(num1, num2, num3))

    elif num1 == num3 != num2:
        print("Result is", same_second_num(num1, num2, num3))

    elif num2 == num1 != num3:
        print("Result is", same_second_num(num1, num2, num3))

    elif num2 == num3 != num1:
        print("Result is", same_second_num(num1, num2, num3))

    elif num3 == num1 != num2:
        print("Result is", same_second_num(num1, num2, num3))

    elif num3 == num2 != num1:
        print("Result is", same_second_num(num1, num2, num3))

    another = get_user_input("\nTry Again? (yes, no): ")
    if another != 'yes':
        break

