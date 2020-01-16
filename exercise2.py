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
# print(result_list)

#alt
a = [[2, -2], [5, 3]]
b = [[2, -2], [5, 3]]
result = [[0, 0], [0, 0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        result[i][j] = a[i][j] + b[i][j]
for r in result:
    print(r)

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

#6 Long-long Vowels
# word = input("Gimme a word >> please >>")
# word_list = list(word.lower())
# long_word = []

# long_vowels = {"aa" : "aaaaa", "ee" : "eeeee", "ii" : "iiiii", "oo" : "ooooo", "uu" : "uuuuu"}
# for letter in word_list:
#     if letter in long_vowels:
#         letter = long_vowels[letter]
#         long_word.append(letter)

#     else: 
#         long_word.append(letter)
# final = ''.join(long_word)
# print(final)

#7 Caesar
# def caesar_encrypt(realText, step):
#     outText = []
#     cryptText = []
	
#     uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#     for eachLetter in realText:
#         if eachLetter in uppercase:
#             index = uppercase.index(eachLetter)
#             crypting = (index + step) % 26
#             cryptText.append(crypting)
#             newLetter = uppercase[crypting]
#             outText.append(newLetter)
#         elif eachLetter in lowercase:
#             index = lowercase.index(eachLetter)
#             crypting = (index + step) % 26
#             cryptText.append(crypting)
#             newLetter = lowercase[crypting]
#             outText.append(newLetter)
#         else: 
#             outText.append(" ")
#     return "".join(outText)

# code = caesar_encrypt('lbh zhfg hayrnea jung lbh unir yrnearq', 13)
# print()
# print(code)
# print()






