import time
import random


def main():
    start = time.time()
    chars = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()-_=+[]{};:?/.>,<`~'\""
    dictionary = list(chars)
    password = input("Enter password: ")

    check = ""
    while (password != check):
        check = random.choices(chars,k=len(password))
        print(str(check))

        if (check == list(password)):
            end = time.time()
            print("Your password is: " + "".join(check) + " and it took " + str(end-start) + "seconds to crack")
            return
    end = time.time()
    print("Couldn't find your password in" + str(end-start) + "seconds")





if __name__ == "__main__":
    main()