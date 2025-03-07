def count_frequencies(numbers):
    count_dict = {}
    
    for num in numbers:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    return count_dict

numbers_list = [1, 2, 4, 2, 6, 2, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 9, 23]

output = count_frequencies(numbers_list)
print(output)
