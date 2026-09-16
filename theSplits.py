def get_int(msg, fail = "Invalid."):
    try:
        ans = int(input(msg))
    except Exception as e:
        print(fail)
        return get_int(msg, fail)
    return ans

def is_5_digits(x):
    return len(str(x)) == 5

def get_5_digit_num():
    x = get_int("Enter a 5 digit number: ")
    if not is_5_digits(x):
        print("Number must be 5 digits!")
        return get_5_digit_num()
    return x


num = str(get_5_digit_num())
print("   ".join(list(num)))