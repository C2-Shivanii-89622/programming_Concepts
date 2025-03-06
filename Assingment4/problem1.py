#finds the longest word in a list of strings. Use 
#map() to calculate the length of each word, and filter() to get the word with the 
#maximum length.


list_of_strings=[" Shivani","Niraj","Yash","Sanjay"]

print(list_of_strings)

list1=  list(map(len,list_of_strings))

maximum=max(list1)

longest_word=list(filter(lambda n:len (n)==maximum, list_of_strings))

print( "longest_word:",longest_word)