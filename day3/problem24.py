# What is the most frequent word in the following paragraph?
#     paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'


from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

split_it = paragraph.split()

Counter = Counter(split_it)

most_occur = Counter.most_common(5)

print(most_occur)

