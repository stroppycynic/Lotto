import random

print("Choose 6 different numbers from 1 to 49")


def get_user_number():
    """Get number from user.

    Try until user give proper number.

    :rtype: int
    :return: given number as int
    """
    while True:
        try:
            user_number = int(input("Choose the number: "))
            break
        except ValueError:
            print("It's not a number")
    return user_number


def get_numbers():
    """Get 6 different numbers between 1 and 49.
    :rtype: list
    :return: list with 6 numbers provided by user.
    """
    user_numbers_list = []
    while len(user_numbers_list) < 6:
        number = (get_user_number())
        if number not in user_numbers_list and 0 < number <= 49:
            user_numbers_list.append(number)
        elif number not in user_numbers_list and number > 49:
            print("Number is too big")
        elif number not in user_numbers_list and number >= 0:
            print("Number is too small")
        else:
            print("Number already provided")
    return user_numbers_list


def print_numbers(numbers):
    """Print given numbers with ascending order.

    :param list numbers: list of numbers
    """
    print(", ".join(str(number) for number in sorted(numbers)))


def computer_numbers():
    """Chose 6 random numbers.

    :rtype: list
    :return: list with 6 random numbers
    """
    numbers = list(range(1, 49))
    random.shuffle(numbers)
    return numbers[:6]


def lotto():
    """Main function with our program."""
    user_numbers = get_numbers()
    print("Your numbers:")
    print_numbers(user_numbers)
    random_numbers = computer_numbers()
    print("Lotto numbers:")
    print_numbers(random_numbers)

    hits = 0
    for number in user_numbers:
        if number in random_numbers:
            hits += 1

    print(f"You hit {hits} {'number' if hits == 1 else 'numbers'}!")


if __name__ == '__main__':
    lotto()
