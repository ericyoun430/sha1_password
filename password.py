import time






def main():
    start = time.time()
    for i in range(1000000):
        x = 3
    end = time.time()
    print("Runtime is:" + str(end-start))




if __name__ == "__main__":
    main()


