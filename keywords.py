'''print("keyword1:")
keyword1 = input()
print("keyword2:")
keyword2 = input()'''
import re

#keyword_list_test = ['gupp(ies|happy)', 'guppitonia', 'gupppiop']
keyword_list_test = ['gupp(ies|happy)', 'gupp(itonia)', 'gupp(piop)']



#print(f'key1: {keyword1}\nkey2: {keyword2}\nkey3: {keyword3}')

def sort_by_length(strings):
    return sorted(strings, key=len)

def remove_redundancies_and_none(input_list):
    # Create a set to store unique elements
    unique_elements = set()
    # Iterate through the list and add non-None elements to the set
    for item in input_list:
        if item is not None:
            unique_elements.add(item)
    # Convert the set back to a list
    return list(unique_elements)

def alphabetize_list(input_list):
    # Use sorted() to sort the list
    return sorted(input_list, key=str)

def pair_matcher_util(input, input2):
    for i in range(len(max(input,input2))):
        try:
            if input[i] != input2[i]:

                return f'{input[:i]}({input[i:]}|{input2[i:]})'

        except IndexError:
            a = f'{input[i:]}{input2[i:]}'
            if len(a) == 1:
                return f'{input[:i]}{a}?'
            return f'{input[:i]}({a})?'

    return None

def find_prefix(input, input2):
    i_remember = 0
    for i in range(len(max(input, input2))):
        prefix = input[:i]

        if re.search(r'\(.*\)', input):
            if i == re.search(r'\(.*\)', input).span()[0]:
                break
        if re.search(r'\(.*\)', input2):
            if i == re.search(r'\(.*\)', input2).span()[0]:
                break
        try:
            if input[i] != input2[i]:
                break
                # return f'{input[:i]}({input[i:]}|{input2[i:]})'

        except IndexError:
            break
            '''a = f'{input[i:]}{input2[i:]}'
            if len(a) == 1:
                return f'{input[:i]}{a}?'
            return f'{input[:i]}({a})?'''''
        i_remember = i
    return i_remember

def find_parts(input, input2):
    # input not input2 must be the one pre-processed
    input_match = re.search(r'.*\(.*\)\?$', input)  # if the regex ends with '(smth)?'
    input_match1 = re.search(r'.*\(.*|.*\)$', input)  # if the regex ends with '(smth|smth)'
    input_match2 = re.search(r'.*[^/\\/]\?$', input)  # if the regex ends with '?' but not '\?'

    input2_match = re.search(r'.*\(.*\)\?$', input2)  # if the regex ends with '(smth)?'
    input2_match1 = re.search(r'.*\(.*|.*\)$', input2)  # if the regex ends with '(smth|smth)'
    input2_match2 = re.search(r'.*[^/\\/]\?$', input2)  # if the regex ends with '?' but not '\?'

    if not input_match and not input_match1 and not input_match2 and not input2_match and not input2_match1 and not input2_match2:  # if no regex shit detected
        return (pair_matcher_util(input, input2))

    if not input_match and not input_match1 and not input_match2:  # if no regex shit in input
        if input2_match or input2_match1 or not input2_match2:  # if regex shit in input2
            a = input
            b = input2
            input = b
            input2 = a

            input_match = re.search(r'.*\(.*\)\?$', input)  # if the regex ends with '(smth)?'
            input_match1 = re.search(r'.*\(.*|.*\)$', input)  # if the regex ends with '(smth|smth)'
            input_match2 = re.search(r'.*[^/\\/]\?$', input)  # if the regex ends with '?' but not '\?'

            input2_match = re.search(r'.*\(.*\)\?$', input2)  # if the regex ends with '(smth)?'
            input2_match1 = re.search(r'.*\(.*|.*\)$', input2)  # if the regex ends with '(smth|smth)'
            input2_match2 = re.search(r'.*[^/\\/]\?$', input2)  # if the regex ends with '?' but not '\?'

    result = None

    parts_list = []

    if input_match or input_match1:
        if input_match:
            match = re.search(r'\(.*\)\?$', input)
        elif input_match1:
            match = re.search(r'\(.*\)$', input)
        s = match.group()  # Extract the matched part

        flag = 0

        for i in range(len(s)):
            if s[i] == r'(' or s[i] == r')' or s[i] == r'|':
                if i != 0:
                    if s[i - 1] != '\\':
                        print(f'append me please !!! {s[flag + 1:i]}')
                        parts_list.append(s[flag + 1:i])
                        flag = i  # ahhhh i've been captured
    elif input_match2:
        parts_list.append(input[-2])

    if input2_match or input2_match1:
        if input2_match:
            match = re.search(r'\(.*\)\?$', input2)
        elif input2_match1:
            match = re.search(r'\(.*\)$', input2)
        s = match.group()  # Extract the matched part

        flag = 0

        for i in range(len(s)):
            if s[i] == r'(' or s[i] == r')' or s[i] == r'|':
                if i != 0:
                    if s[i - 1] != '\\':
                        # print(f'{s[i - 1]}')
                        parts_list.append(s[flag + 1:i])
                        flag = i  # ahhhh i've been captured
    elif input2_match2:
        parts_list.append(input2[-2])
    # print(f'hi input is {input}, {input2}')


    print(f'parts list is {parts_list}')

    parts_list = remove_redundancies_and_none(parts_list)
    parts_list = alphabetize_list(parts_list)

    print(f'parts list is 2{parts_list}')
    return(parts_list)

def pair_matcher(input, input2):
    if input == None or input2 == None:
        return None

    #print(input, input2)
    if input[0].lower() != input2[0].lower() or input[1] != input2[1] or input[2] != input2[2]:
        return None
    
    # input not input2 must be the one pre-processed
    input_match = re.search(r'.*\(.*\)\?$', input)  # if the regex ends with '(smth)?'
    input_match1 = re.search(r'.*\(.*|.*\)$', input)  # if the regex ends with '(smth|smth)'
    input_match2 = re.search(r'.*[^/\\/]\?$', input)  # if the regex ends with '?' but not '\?'

    input2_match = re.search(r'.*\(.*\)\?$', input2)  # if the regex ends with '(smth)?'
    input2_match1 = re.search(r'.*\(.*|.*\)$', input2)  # if the regex ends with '(smth|smth)'
    input2_match2 = re.search(r'.*[^/\\/]\?$', input2)  # if the regex ends with '?' but not '\?'

    if not input_match and not input_match1 and not input_match2 and not input2_match and not input2_match1 and not input2_match2: #if no regex shit detected
        return(pair_matcher_util(input, input2))

    if not input_match and not input_match1 and not input_match2: #if no regex shit in input
        if input2_match or input2_match1 or not input2_match2: # if regex shit in input2
            a = input
            b = input2
            input = b
            input2 = a

            input_match = re.search(r'.*\(.*\)\?$', input)  # if the regex ends with '(smth)?'
            input_match1 = re.search(r'.*\(.*|.*\)$', input)  # if the regex ends with '(smth|smth)'
            input_match2 = re.search(r'.*[^/\\/]\?$', input)  # if the regex ends with '?' but not '\?'

            input2_match = re.search(r'.*\(.*\)\?$', input2)  # if the regex ends with '(smth)?'
            input2_match1 = re.search(r'.*\(.*|.*\)$', input2)  # if the regex ends with '(smth|smth)'
            input2_match2 = re.search(r'.*[^/\\/]\?$', input2)  # if the regex ends with '?' but not '\?'

    result = None

    print(f'hi im input 1 and 2 : {input, input2}')

    # find prefix
    i_remember = 0
    for i in range(len(max(input,input2))):
        prefix = input[:i]

        if re.search(r'\(.*\)', input):
            if i == re.search(r'\(.*\)', input).span()[0]:
                break
        if re.search(r'\(.*\)', input2):
            if i == re.search(r'\(.*\)', input2).span()[0]:
                break
        try:
            if input[i] != input2[i]:
                break
                #return f'{input[:i]}({input[i:]}|{input2[i:]})'

        except IndexError:
            break
            '''a = f'{input[i:]}{input2[i:]}'
            if len(a) == 1:
                return f'{input[:i]}{a}?'
            return f'{input[:i]}({a})?'''''
        i_remember = i

    #print(f'prefix: {prefix}')


    print('hiii')

    if input_match or input_match1 or input_match2:
        if input2_match or input2_match1 or not input2_match2: #if regex shit in both inputs

            #collect parts list
            parts_list = []

            if input_match or input_match1:
                if input_match:
                    match = re.search(r'\(.*\)\?$', input)
                elif input_match1:
                    match = re.search(r'\(.*\)$', input)
                s = match.group()  # Extract the matched part

                flag = 0

                for i in range(len(s)):
                    if s[i] == r'(' or s[i] == r')' or s[i] == r'|':
                        if i != 0:
                            if s[i - 1] != '\\':
                                print(f'append me please !!! {s[flag + 1:i]}')
                                parts_list.append(s[flag + 1:i])
                                flag = i #ahhhh i've been captured
            elif input_match2:
                parts_list.append(input[-2])

            if input2_match or input2_match1:
                if input2_match:
                    match = re.search(r'\(.*\)\?$', input2)
                elif input2_match1:
                    match = re.search(r'\(.*\)$', input2)
                s = match.group()  # Extract the matched part

                flag = 0

                for i in range(len(s)):
                    if s[i] == r'(' or s[i] == r')' or s[i] == r'|':
                        if i != 0:
                            if s[i - 1] != '\\':
                                # print(f'{s[i - 1]}')
                                parts_list.append(s[flag + 1:i])
                                flag = i  # ahhhh i've been captured
            elif input2_match2:
                parts_list.append(input2[-2])
            #print(f'hi input is {input}, {input2}')

        print(f'parts list is {parts_list}')

        parts_list = remove_redundancies_and_none(parts_list)
        parts_list = alphabetize_list(parts_list)

        print(f'parts list is 2{parts_list}')


        #organize parts list to output
        if re.search(r'\(.*\)$', input):
            j = re.search(r'\(.*\)$', input).span()[0] -1

        elif re.search(r'\(.*\)?$', input):
            j = re.search(r'\(.*\)?$', input).span()[0] -1


        if j != i_remember:
            parts_list.append(input[i_remember:j])


        if re.search(r'\(.*\)$', input2):
            j = re.search(r'\(.*\)$', input2).span()[0] -1

        elif re.search(r'\(.*\)?$', input2):
            j = re.search(r'\(.*\)?$', input2).span()[0] -1

        if j != i_remember:
            parts_list.append(input2[i_remember:j])


        r = f'{prefix}('
        for i in range(len(parts_list)):
            r = r + parts_list[i]
            if i != len(parts_list) - 1:
                r = r + r'|'
        r = r + r')'
        if input[-1] == r'?' or input2[-1] == r'?':
            r = r + r'?'

        print(f'returning parts list is 2{parts_list}')
        return r





    if input_match:
        x = input[:-2]
        result = x + f'|{input2[i_remember:]})?'
    elif input_match1:
        x = input[:-1]
        result = x + f'|{input2[i_remember:]})'
    elif input_match2:
        x = input[:-1]
        y = x[-1]
        x = x[:-1]
        result = x + f'({y}|{input2[i_remember:]})?'

    print(f'returning {result}')

    return result


def first_4_match(input, input2):
    b = False
    if len(input) > 4 and len(input2) > 4:
        if input[0] == input2[0]:
            b = True
            for i in range(4):
                if input[i] != input2[i]:
                    b = False

    return b

def pair_capitalizator(input, input2):
    if input == None or input2 == None:
        return None
    if input[0].lower() == input2[0] or input[0] == input2[0].lower() and input[1:] == input2[1:]:
        return f'[{input[0].upper()}{input[0].lower()}]{input[1:]}'
    return None



def process_keywords(input):
    #input = sort_by_length(input)
    keyword_list = input.copy()
    intermediate_keyword_list = input.copy()
    #print(f'hi{keyword_list}')
    #print(intermediate_keyword_list)

    for i in range(len(keyword_list)):
        #print(f'KW list is : {keyword_list}')
        for j in range(len(keyword_list)):
            #print(f'KW list is 22: {keyword_list}')

            if i != j:
                if keyword_list[i][0].lower() == keyword_list[j][0].lower() and keyword_list[i][1] == keyword_list[j][1] and keyword_list[i][2] == keyword_list[j][2]:
                    paired = pair_matcher(keyword_list[i], keyword_list[j])
                    print(f"key1 {keyword_list[i]}, key 2 {keyword_list[j]}")
                    print(f'paire : {paired}')
                    #print(f'KW list is 23: {keyword_list}')
                    if paired != None:
                        try:
                            intermediate_keyword_list[i] = None
                            intermediate_keyword_list[j] = None

                        except IndexError:
                            pass
                        #print(f'KW list is 24: {keyword_list}')

                        keyword_list.append(paired)

    print(f'da list is :{keyword_list}')


    print(f'ik list is :{intermediate_keyword_list}')
    intermediate_keyword_list = remove_redundancies_and_none(intermediate_keyword_list)





    final_keyword_list=[]
    final_keyword_list = intermediate_keyword_list.copy()
    for i in range(len(intermediate_keyword_list)):
        for j in range(len(intermediate_keyword_list)):
            if i != j:
                capped = pair_capitalizator(intermediate_keyword_list[i], intermediate_keyword_list[j])
                if capped != None:
                    final_keyword_list[i] = None
                    final_keyword_list[j] = None
                    final_keyword_list.append(paired)

    final_keyword_list = remove_redundancies_and_none(final_keyword_list)

    print(f'processed keywords :{final_keyword_list}')
    return final_keyword_list

                

    '''if first_4_match(keyword1, keyword2):
        print('hi')
        a = pair_matcher_util(keyword1, keyword2)
        print(a)

    b = pair_matcher(a,keyword3)
    #print(pair_matcher(b,keyword4))

    print(pair_capitalizator(keyword2, keyword4))'''


    '''input = [keyword3, a]

    if first_4_match(input):
        print('hi')
        a = pair_matcher_util(input)
        print(a)'''

class main:
    print(f'hi im from main: {process_keywords(keyword_list_test)}')

