import os
import re

print()

file = os.path.join("Resources","paragraph_2.txt")

with open(file,'r') as text:
    lines = text.read()
    words=lines.split()
    number_of_words=len(words)
    sum=0
    for word in words:
        number_of_letters=len(word)
        sum=sum+number_of_letters
    avgLength=sum/number_of_words
    sents = lines.split('.')
avg_len = sum(len(x.split()) for x in sents) / len(sents)


print("Paragraph Analysis")
print("-----------------")
print("Approximate Word Count:", number_of_words)
print("Approximate Sentence Count:", lines.count("."))
print("Average Letter Count:", avgLength)
print("Average Sentence Length:", avg_len)
print()