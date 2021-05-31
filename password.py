import time
import hashlib


def converter(text):
    digest = hashlib.sha1(text.encode()).hexdigest()
    return digest

def main():
    start = time.time()

    user_input = input("Enter sha1: ")
    clean_input = user_input.strip().lower()
    
    with open('./dictionary.txt') as f:
        for line in f:
            test_pass = line.strip()
            converted_val = converter(test_pass)
            if (converted_val == clean_input):
                end = time.time()
                print("Password has been found in " + str(end-start) + " seconds: " + line)
                return
        print("Password not found")

    end = time.time()
    print("Runtime is:" + str(end-start))

if __name__ == "__main__":
    main()


