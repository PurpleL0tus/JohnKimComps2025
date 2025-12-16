import random
from tools import tokens
from tools import is_valid_regex


def regex_generator(input_string):
    regex_output = ''
    list_output = []
    valid_regex_count = 0
    invalid_regex_count = 0

    keywords = input_string
    #print(keywords)

    #print(random_keywords)
    token_instance = tokens()
    #print(random_value)


    for a in range(10000):
        for i in range(random.randint(2, 4)):
            random_value = token_instance.get_random_value()
            if '%' in random_value:
                for b in range(random_value.count('%')):
                    random_value = random_value.replace('%', f'{random.randint(0, 9)}',1)
            if '~' in random_value:
                for q in range(random_value.count('~')):
                    random_value = random_value.replace('~', f'{random.sample(keywords, k=1)}',1)

            #print(random_value)

            regex_output = ''.join([regex_output, random_value])
        #print(regex_output)
        if is_valid_regex(regex_output) == True:
            #print('valid regex')
            return regex_output

            list_output.append(regex_output)
            valid_regex_count += 1
        if is_valid_regex(regex_output) == False:
            #print('invalid regex')
            invalid_regex_count += 1
        regex_output = ''


    return list_output

    #print('')
    #print(f'valid_regex_count: {valid_regex_count}')
    #print(f'invalid_regex_count: {invalid_regex_count}')



