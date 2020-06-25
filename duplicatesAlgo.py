# my_list = ["dog", "cat", "bird"]

# for (index, value) in my_list: 
#     print(index, value)



the_list = [1, 1, 2, 3, 4, 4]

def removeDuplicates(list):
    cleanedList = []
    for num in list:
        if num not in cleanedList:
            cleanedList.append(num)
    print(cleanedList)
    return len(cleanedList)

print(removeDuplicates(the_list))