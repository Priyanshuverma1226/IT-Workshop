# Clean the following text. After cleaning, count three most frequent words in the string.
# sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

# print(clean_text(sentence));
# I am a teacher and I love teaching There is nothing as more rewarding as educating and empowering people I found teaching more interesting than any other jobs Does this motivate you to be a teacher
# print(most_frequent_words(cleaned_text)) # [(3, 'I'), (2, 'teaching'), (2, 'teacher')]


import re
from collections import Counter

def most_freq(s):

    split_it = s.split()

    Counter = Counter(split_it)

    most_occur = Counter.most_common(5)

    print(most_occur)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''


# Import the re module

# string with special characters 
print("String before conversion: ",sentence)
#using regular expression with the sub() method
normal_string =re.sub("[^A-Z]", "", sentence,0,re.IGNORECASE)
print("String after conversion: ",normal_string)


most_freq(normal_string)

