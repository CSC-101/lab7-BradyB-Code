import convert



# Task 2
def gather_numbers()->list[float]:
    y = "y"
    numbers  =[]
    while y == "y" or y =="n":
        if y == "y":
            x = input("Enter a number: ")
            numbers.append(convert.str_to_float(x))
            y = input("Continue? y/n: ")
        else:
            return numbers
    return numbers

#main module
if __name__ == '__main__':
    print(gather_numbers())



