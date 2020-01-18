#1 Letter Summary
# word = input("Enter a word >>")

# empty_dict = {}
# for letters in word:
#     if letters not in empty_dict:
#         empty_dict[letters] = 0
#     empty_dict[letters] += 1
# print(empty_dict)

#2 Word Summary
user_input = input("Please enter a sentence (include a period or space at the end): ")

empty_dict = {}
word_dump = ""
for letter in user_input:
    if letter == " "  or letter == ".":
        if word_dump not in empty_dict:
            empty_dict[word_dump] = 0
            empty_dict[word_dump] += 1
            word_dump = ""
        else:
            empty_dict[word_dump] += 1
            word_dump = ""
    else: 
        word_dump += letter
print(empty_dict)
    



