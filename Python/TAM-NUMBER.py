def is_palindrome(num):
    return str(num) == str(num)[::-1]

def process_file(filename):
    try:
        with open(filename, "r") as file:
            for i, line in enumerate(file, start=1):
                numbers = list(map(int, line.strip().split(",")))
                total = sum(numbers)
                result = "Palindrome" if is_palindrome(total) else "Not a palindrome"
                print(f"Line {i}: {', '.join(map(str, numbers))} (sum {total}) - {result}")
    except FileNotFoundError:
        print("Error: File not found.")
    except ValueError:
        print("Error: Invalid data in file.")

process_file("numbers.txt")
