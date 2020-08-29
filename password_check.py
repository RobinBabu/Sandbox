MIN_LENGTH = 3


def main():

    password = input("Enter a password of with a minimum of {} characters: ".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Enter a password of with a minimum of {} characters: ".format(MIN_LENGTH))

        print('*' * len(password))


main()




