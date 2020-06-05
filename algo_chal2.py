#1. Callatz Conjecture

# def collatz(num):
#     while (num != 1):
#         if num % 2 == 0:
#             num /= 2
#         else:
#             num = (num * 3) + 1
#         print(num)

# collatz(20)

#2. Palondromic number
# def palon():
#     while True:
#         palo_holder = 0
#         for x in range(100, 1000):
#             for y in range(100, 1000):
#                 palo_worker = x * y
#                 if (str(palo_worker)) == ((str(palo_worker))[::-1]):
#                     if palo_worker > palo_holder:
#                         palo_holder = palo_worker
#         print(palo_holder)
#         break

# palon()

#3. Smallest evenly divisibly by all numbers from 1 to 20
# def smallest():
#         num_check = 2520
#         not_found = True
#         while not_found:
#             truths = 0
#             if truths != 20:
#                 print(num_check)
#                 for ran in range(1, 21):
#                     if num_check % ran == 0:
#                         truths += 1
#                     else:
#                         num_check += 2520
#                         truths = 0
#                         break
#             else: 
#                 print("finished: ", num_check)
#                 not_found = False


# smallest()

