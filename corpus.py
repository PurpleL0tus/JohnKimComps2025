import json
import re

with open('data.json', 'r') as file:
    data = json.load(file)


'''print(json.dumps(data, indent=4))
print(data[4])
print(data[4]['regex'])'''

print(f'this many regexs {len(data)}')
for i in range(len(data)):

    regex = data[i]['regex']
    regex = re.sub(r" ", "", regex)
    regex = re.sub(r"   ", "", regex)
    regex = re.sub("\n", "", regex)
    regex = re.sub("\(\?#.*\)", "", regex)

    print(regex)
    print('--')




    file1 = open("corpus.txt", "a")
    file1.write(f"{regex}    ")  # tsv
    file1.close()
