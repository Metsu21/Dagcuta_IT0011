def sum_digits(digits):
    sum = 0
    for digit in digits:
        if '0' <= digit <= '9':  
            sum += int(digit)
    return sum

input_string = input("Enter a string of digits: ")
print("The sum of the digits is:", sum_digits(input_string))