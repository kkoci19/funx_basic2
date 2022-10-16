# Ushtrimi 1
# Countdown
def countdown(num):
    output = []
    for nr in range(num, -1, -1):
        output.append(nr)
    return output


print(countdown(10))
# -----------------------------------------------------

# Ushtrimi 2
# Print and Return


def print_and_return(value):
    print(value[0])
    return value[1]


print(print_and_return([1, 2]))
# -----------------------------------------------------------

# Ushtrimi 3
# First Plus Length


def firstList_plusLength(list):
    return list[0] + len(list)


print(firstList_plusLength([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# -----------------------------------------------------------

# Ushtrimi 4
# Values Greater than Second


def greaterValue(list):
    if len(list) < 2:
        return False
    output = []
    for nr in range(0, len(list)):
        if list[nr] > list[1]:
            output.append(list[nr])
    print(len(output))
    return output


print(greaterValue([1, 2, 3, 4, 5, 6]))
print(greaterValue([6]))
# ----------------------------------------------------------


# Ushtrimi 5
# This Length, That Value
def lengthValue(size, value):
    output = []
    for nr in range(0, size):
        output.append(value)
    return output


print(lengthValue(5, 7))
print(lengthValue(3, 9))
