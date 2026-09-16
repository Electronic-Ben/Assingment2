def get_int(msg, fail = "Invalid."):
    try:
        ans = int(input(msg))
    except Exception as e:
        print(fail)
        return get_int(msg, fail)
    return ans

def check_parity():
    x = get_int("Enter a number: ")
    print()
    print(str(x) + " is " + ("Even" if x % 2 == 0 else "Odd"))

def check_multiple():
    x = get_int("\nEnter a number: ")
    y = get_int("Enter another number: ")

    indicator = " is " if x % y == 0 else " is not "

    print()
    print(str(x) + indicator + "a multiple of " + str(y))

check_parity()
check_multiple()

