#1 Smallest Number
# liste = [7, 5, 2, 6, 1, 3]
# def smallest(the_list):
#     the_list.sort()
#     small = the_list[0]
#     print(small)
# smallest(liste)

#alt no built-in function
# liste = [7, 5, 2, 6, 1, 3]
# def smallest_nobilt(myList):
#     place_holder = myList[0]
#     for num in myList:
#         if num < place_holder:
#             place_holder = num
#     return place_holder

#2 Largest Number
# liste2 = [2, 5, 1, 6, 3, 5]
# def largest(list_input):
#     sorted_list = sorted(list_input)
#     big_boy = sorted_list.pop()
#     print(big_boy)
# largest(liste2)

#3 Find shortest string
# list_of_strings = ["this", "that", "seven", "banana", "california"]
# def shortest(input):
#     the_shortest = ""
#     for i in input:
#         length = len(i)
#         if length > len(the_shortest):
#             the_shortest = i
#     return the_shortest
# runner = shortest(list_of_strings)
# print(runner)

#4 Find longest string
# list_of_strings = ["california", "that", "seven", "banana", "cat"]
# def largest(input):
#     sharty = ""
#     for i in input:
#         length = len(i)
#         if i[0]:
#             sharty = i
#         if length < len(sharty):
#             sharty = i
#     return sharty
# runner = largest(list_of_strings)
# print(runner)



