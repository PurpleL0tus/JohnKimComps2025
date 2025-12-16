import random
from tools import tokens
from tools import is_valid_regex
from math_stuff import normal_distribution
from keywords import process_keywords
output = ''
valid_regex_count = 0
invalid_regex_count = 0

keyword_list_test = ['hello(a)','hello(a|b|c|d)', 'than']
words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon"]
words = ["insert-keyword-here"]

random_words = random.sample(words, k=1)
#print(random_words)
token_instance = tokens()
random_value = token_instance.get_random_value()
#print(random_value)


'''
for a in range(1000000):
    for i in range(random.randint(2, 10)):
        random_value = token_instance.get_random_value()
        if '%' in random_value:
            for b in range(random_value.count('%')):
                random_value = random_value.replace('%', f'{random.randint(0, 9)}',1)
        if '~' in random_value:
            for q in range(random_value.count('~')):
                random_value = random_value.replace('~', f'{random.sample(words, k=1)}',1)

        #print(random_value)

        output = ''.join([output, random_value])
    print(output)
    output = ''
    if is_valid_regex(output) == True:
        #print('valid regex')
        valid_regex_count += 1
    if is_valid_regex(output) == False:
        #print('invalid regex')
        invalid_regex_count += 1

print('')
print(f'valid_regex_count: {valid_regex_count}')
print(f'invalid_regex_count: {invalid_regex_count}')
'''
def test_random_regex(a):
    if a == a:
        return False
def generate_regex(i, keywords):
    #print(keywords)
    p = len(keywords)-1
    #print(f'hi{keywords}')
    #print(f'p : {p}')



    output = ''
    for j in range(i):
        random_value = token_instance.get_random_value() #get random token
        if '%' in random_value:
            for b in range(random_value.count('%')):
                random_value = random_value.replace('%', f'{random.randint(0, 9)}', 1)
        if '~' in random_value:
            for q in range(random_value.count('~')):
                #print(f'wtf is happening{keywords}')
                hi = random.randint(0, p)
                random_value = random_value.replace('~', f'{keywords[hi]}', 1)

        # print(random_value)

        output = ''.join([output, random_value])
        #print(output)
    return output

class main:
    keyword_list_test = ['guppies', 'guppy', 'guppitonia']
    keywords = process_keywords(keyword_list_test)
    print(f'{keywords} da keywords')

    i = 0
    while 0 == 0:
        
        i = i + 1

        if i < 20000:
            if i < 10000:
                j = 1
            elif i > 10000:
                j = 2
            token_count = normal_distribution(3, j,0,10)
        else:
            token_count = random.randint(0, 10)# not worth the computational trouble, pretty much a flat line
        #print(f'please don {keywords}')
        a = generate_regex(token_count, keywords)
        print(a)

        if i == 50000:
            print('failed')
            break

        if test_random_regex(a):
            print(a)
            break




