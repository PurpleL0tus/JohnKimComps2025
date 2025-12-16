import random
from tools import tokens
from math_stuff import normal_distribution
import time

regex_tokens = [
    ".",     # Matches any single character except a newline
    "^",     # Asserts position at the start of a string
    "$",     # Asserts position at the end of a string
    "*",     # Matches 0 or more repetitions of the preceding element
    "+",     # Matches 1 or more repetitions of the preceding element
    "?",     # Matches 0 or 1 repetition of the preceding element
    "{n}",   # Matches exactly n repetitions of the preceding element
    "{n,}",  # Matches n or more repetitions of the preceding element
    "{n,m}", # Matches between n and m repetitions of the preceding element
    "[]",    # Matches any single character in the brackets
    "|",     # Acts as a logical OR between patterns
    "\\",    # Escapes special characters
    "\\d",   # Matches any digit (equivalent to [0-9])
    "\\D",   # Matches any non-digit character
    "\\w",   # Matches any word character (alphanumeric + underscore)
    "\\W",   # Matches any non-word character
    "\\s",   # Matches any whitespace character
    "\\S",    # Matches any non-whitespace character
    "\\b"
]

test = ['\\d','?','$']
# Start time
start_time = time.time()

token_count = normal_distribution(3, 3, 0, 10)

output = ''
valid_regex_count = 0
invalid_regex_count = 0

keyword_list_test = ['hello(a)','hello(a|b|c|d)', 'than']
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
words = "[Gg]upp(ies|y)"

random_words = random.sample(words, k=1)
#print(random_words)
token_instance = tokens()
random_value = token_instance.get_random_value()
#print(random_value)

a = 0
b=0
time_list = []
guess = []
while 0 == 0:
    output = ''

    a = a+1
    token_count = normal_distribution(3, 3, 1, 10)
    token_count = random.randint(1, 10)

    random_integer = random.randint(0, token_count - 1)  # Generates a random number between 1 and 10 (inclusive)

    for i in range(token_count):
        random_value = random.choice(regex_tokens)
        '''if '%' in random_value:
            for b in range(random_value.count('%')):
                random_value = random_value.replace('%', f'{random.randint(0, 9)}',1)'''

        '''if '~' in random_value:
            for q in range(random_value.count('~')):
                random_value = random_value.replace('~', f'{random.sample(words, k=1)}',1)'''

        #print(random_value)
        output = ''.join([output, random_value])


        if i == random_integer:
            output = ''.join([output, words])


    #print(f'output is : {output}\n')






    #if output == r"\d[Gg]upp(ies|y)?$" or output == r"^\d[Gg]upp(ies|y)?$" or output == r"\b\d[Gg]upp(ies|y)?\b" or output == r"^[Gg]upp(ies|y)$":'''
    if output == r"\b[Gg]upp(ies|y)(?:\s+\w+)*\s*":
        end_time = time.time()
        duration = end_time - start_time

        print("YESSSSSS")
        print(output)
        print(f"Execution time: {duration:.4f} seconds")
        print(f"that took {a} guesses")


        time_list.append(duration)
        start_time = time.time()
        guess.append(a)
        a = 0

        b = b + 1
        if b == 10:
            print("YESSSSSS")
            print(output)
            print(time_list)
            print(guess)

            print(f"average Execution time: {sum(time_list) / len(time_list)} seconds")
            print(f"average that took {sum(guess) / len(guess)} guesses")


            break

    '''output = ''
    if is_valid_regex(output) == True:
        #print('valid regex')
        valid_regex_count += 1
    if is_valid_regex(output) == False:
        #print('invalid regex')
        invalid_regex_count += 1

print('')
print(f'valid_regex_count: {valid_regex_count}')
print(f'invalid_regex_count: {invalid_regex_count}')'''
