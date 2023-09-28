from random import sample
import csv
import io
import re


ans = []

with io.open('./data/train.tsv','r',encoding='utf8') as train:
    string = train.read()

    for x in re.findall('((?:[^\n]+\n?))', string):
        x.strip().split('\n')
        ans.append(x)

# samples = ans[:int(len(ans) * 1)]
# print(len(samples))
# print(samples)


# samples = sorted(sample(ans, int(len(ans) * 0.01)))
samples = sample(ans, int(len(ans) * 0.01))
# print(type(samples))
# print(samples)
print(len(samples))

# for instance in samples:
#     print(instance)
#     index = instance.split("\t")
#     print("index",index)

with io.open("./data/sample_train.tsv", 'w',encoding='utf8') as f:

    for line in samples:
        f.write(line)

