#1 Letter Summary
# word = input("Enter a word >>")

# empty_dict = {}
# for letters in word:
#     if letters not in empty_dict:
#         empty_dict[letters] = 0
#     empty_dict[letters] += 1
# print(empty_dict)

#2 Word Summary
# user_input = input("Please enter a sentence (include a period or space at the end): ")

# empty_dict = {}
# word_dump = ""
# for letter in user_input:
#     if letter == " "  or letter == ".":
#         if word_dump not in empty_dict:
#             empty_dict[word_dump] = 0
#             empty_dict[word_dump] += 1
#             word_dump = ""
#         else:
#             empty_dict[word_dump] += 1
#             word_dump = ""
#     else: 
#         word_dump += letter
# print(empty_dict)

# #alt
# sent_histogram = {}
# entered_sentence = input("Please enter a sentence...")
# sent_to_words = entered_sentence.split()

#3 Sorting a Histogram
# user_input = input("Please enter a sentence (include a period or space at the end): ")

# empty_dict = {}
# word_dump = ""
# for letter in user_input:
#     if letter == " "  or letter == ".":
#         if word_dump not in empty_dict:
#             empty_dict[word_dump] = 0
#             empty_dict[word_dump] += 1
#             word_dump = ""
#         else:
#             empty_dict[word_dump] += 1
#             word_dump = ""
#     else: 
#         word_dump += letter

# top1 = [0, 0]
# top2 = [0, 0]
# top3 = [0, 0]
# dict__to_tuple = empty_dict.items()
# for words in dict__to_tuple:
#     if words[1] > top1[1]:
#         top1[0] = words[0]
#         top1[1] = words[1]
#     elif words[1] > top2[1]:
#         top2[0] = words[0]
#         top2[1] = words[1]
#     elif words[1] > top3[1]:
#         top3[0] = words[0]
#         top3[1] = words[1]
# print("The top three words are:")
# print(top1)
# print(top2)
# print(top3)






