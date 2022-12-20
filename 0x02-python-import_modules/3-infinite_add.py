#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    length = len(sys.argv)
    count = 1
    total = 0

    while count < length:
        sum = int(sys.argv[count])
        total = sum + total
        count += 1

    print(total)
