# 1 Multiply Vectors
# list1 = [2, 4, 5]
# list2 = [2, 3, 6]
# new_list = []

# for i in range(len(list1)):
#     new_list.append(list1[i] * list2[i])
# print(f"{list1} X {list2} = {new_list}")

#2 Matrix Addition
# dim1 = [[2, -2], [5, 3]]
# dim2 = [[2, -2], [5, 3]]
# result_list = []

# for index1 in range(len(dim1)):
#     for index2 in range(len(dim2)):
#         if index1 == index2:
#             working_list = []
#             sum1 = dim1[index1][0] + dim2[index2][0]
#             sum2 = dim1[index1][1] + dim2[index2][1]
#             working_list.append(sum1)
#             working_list.append(sum2)
#             result_list.append(working_list)
# print(working_list)

#3 Matrix Addition II
# dim1 = [[2, -2, 3], [5, 3, 3]]
# dim2 = [[2, -2, 4], [5, 3, 4]]
# result_list = []

# for index1 in range(len(dim1)):
#     for index2 in range(len(dim2)):
#         if index1 == index2:
#             working_list = []
#             sum1 = dim1[index1][0] + dim2[index2][0]
#             sum2 = dim1[index1][1] + dim2[index2][1]
#             sum3 = dim1[index1][2] + dim2[index2][2]
#             working_list.append(sum1)
#             working_list.append(sum2)
#             working_list.append(sum3)
#             result_list.append(working_list)
# print(result_list)

#4 De-dup
# list1 = [1, 1, 2, 3, 4, 4, 5, 5, 6, 7, 7, 8]
# new_list = []
# for i in list1:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

#5 Leetspeak
# shakespeare = """All that glitters is not gold
# Fair is foul, and foul is fair: Hover through the fog and filthy air.
# Life ... is a tale Told by an idiot, full of sound and fury, Signifying nothing."""
# shake_upper = shakespeare.upper()
# shake_list = list(shake_upper)
# leet_shake = []

# leet = {"A" : "4", "E" : "3", "G" : "6", "I" : "1", "O" : "0", "S" : "5", "T" : "7"}
# for letter in shake_upper:
#     if letter in leet:
#         letter = leet[letter]
#         leet_shake.append(letter)
#     else:
#         leet_shake.append(letter)
# final = "".join(leet_shake).lower()
# print(final)




    





