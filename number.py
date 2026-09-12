def check_even_odd(number):
    if number % 2 == 0:
        print("The number is Even")
    else:
        print("The number is Odd")


def check_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

check_even_odd(number)

if check_prime(number):
    print("The number is Prime")
else:
    print("The number is Not Prime")
