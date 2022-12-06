def factorial(num, *args):
    if len(args) == 0:
        if num == 1:
            return 1
        else:
            return num * factorial(num - 1)
    else:
        return "ACCEPTING ONLY 1 ARGUMENT"


print(factorial(6))
