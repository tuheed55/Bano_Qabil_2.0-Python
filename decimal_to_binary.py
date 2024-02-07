

# Name          : Muhammad Tuheed Ahmed.
# Roll Number   : 36820
# Email Address : tuheedahmed55@gmail.com

# decimal to binary converter.

def decimal_to_binary(decimal_num):

# formula
    binary_result = ""
    while decimal_num > 0:
        binary_result = str(decimal_num % 2) + binary_result
        decimal_num //= 2

# apply condition.
    if not binary_result:
        binary_result = "0"
    return binary_result

# input a decimal number from the user
decimal_input = int(input("Enter a decimal number: "))

# call the function and display the result
binary_result = decimal_to_binary(decimal_input)
print(f"The binary representation of {decimal_input} is: {binary_result}")


