from collections import deque
import re

def check_string4palindrome(input_string: str):
    if len(input_string) < 2:
        print("Ooops, next time enter more than 1 characters.")
    else:
        formated_string = re.sub(r"\s", "", input_string.strip()).lower()

        deque4sting = deque(formated_string)
        # print(deque4sting)

        while len(deque4sting) > 1:
            is_palindrome = False if deque4sting.popleft() != deque4sting.pop() else True

        if is_palindrome:
            print(f"{input_string} - is palindrome")
        else:
            print(f"{input_string} - not a palindrome")
    
check_string4palindrome(input("Give me something to check --> "))