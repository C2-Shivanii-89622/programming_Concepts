#Write a Python program that filters out all strings that have more than 5 
#characters from a list of strings using the filter() function. 
words=['Red', 'Green', 'Yellow', 'Purple', 'Orange']

print(words)
length=4
big_words= list(filter(lambda n: len(n)>length, words))

print(big_words)



 