## 7.7 List EXERCISES

# # 1
# 
# try:
#     lst = []
#     print("PRESS ANY LETTER TO END")
#     while True:
#         lst_items = int(input("Enter a number: "))
#         lst.append(lst_items)
# except Exception:
#     print("Done!\n")
# finally:
#     print("a.) Total items in the list: ",len(lst))
#     print("b.) Last item: ", lst[len(lst)-1])
#     print("c.) Reversed list: ", lst[::-1])
#     print("d.) Does it contains a 5?: ", end ='')
#     for i in range(len(lst)):
#         if 5 in lst:
#             print("Yes")
#             break
#         elif i == len(lst)-1:
#             print("No")
#         else:
#             print("No")
#             break
#     print("e.) No. of '5' in the list: ", lst.count(5))
#     first = lst[0]
#     last =  lst[len(lst)-1]
#     del lst[0]
#     del lst[len(lst)-1]
#     lst.sort()
#     print("f.) Deleted first ({}) and last ({}) element, then sorted: {}".format(first, last, lst))
#     x=0
#     for i in range (len(lst)):
#         if lst[i]<5:
#             x+=1
#     print("g.) Items less than 5: ", x)


# # 2
# 
# from random import randint
# lst = []
# for i in range(20):
#     lst.append(randint(1,100))
# print("a.) List: ",lst)
# print("b.) Average of the elements in the list: ", sum(lst)/len(lst))
# print("c.) Largest and the smallest value in the list:\nLargest: {}\nSmallest: {}". format(max(lst), min(lst)))
# lst.sort()
# print("d.) Second largest and second smallest value in the list: \nSecond largest: {}\nSecond smallest: {}". format(lst[1], lst[len(lst)-2]))
# even = [items for items in lst if items%2 == 0]
# print("e.) No. of even numbers in the list: ", len(even))


# # 3
# 
# lst = [8,9,10]
# # a
# lst.remove(lst[1])
# lst.insert(1,17)
# # b
# lst = lst + [4,5,6]
# # c
# lst.remove(lst[0])
# # d
# lst.sort()
# # e
# lst = 2*lst
# # f
# lst.insert(3, 25)
# print(lst)


# # 4

# lst = []
# try:
#     print("Hit 'Enter' when done!")
#     while True:
#         ele = int(input("Enter a number between 1 and 12: "))
#         lst.append(ele)
#         if ele>12 or ele<1:
#             print("Between 1 and 12 only!")
#             del lst[len(lst)-1]
# #         print(lst)
# except Exception:
#     orig_lst = lst[:]
#     print("Done!\n")
# finally:
# #     gt_10 = [integers for integers in lst if integers>10]
# #     for i in range(len(lst)):
# #         x = lst[i]
# #         for j in range(len(gt_10)):
# #             y = gt_10[j]
# #             if x == y:
# #                 gt_10_position_in_lst = lst.index(x)
# #                 del lst[gt_10_position_in_lst]
# #                 lst.insert(gt_10_position_in_lst, 10)
#     i = 0
#     while i < len(lst):
#         if lst[i] > 10:
#             lst[i] = 10
#         i+=1
# print("Original List: ", orig_lst)
# print("Current List", lst)


# # 5
# 
# try:
#     string_lst = []
#     print("Hit 'Enter' when done")
#     while True:
#         string = str(input("Enter a string: "))
#         string = string.replace(string[0], '')
#         string_lst.append(string)
# except Exception:
#     print("Done!")
# finally:
#     print(string_lst)


# # 6
# 
# # a. list with integers 0 to 49
# a_list = []
# for i in range(50):
#     a_list.append(i)
# print(a_list)
# 
# # b. list containing the squares of the integers 1 through 50
# b_list = []
# for i in range(1,51):
#     b_list.append(i**2)
# print(b_list)
# 
# # c. list with a, bb, ccc, ..., z(*26)
# c_list = []
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# alphabet_list = []
# for c in alphabet:
#     alphabet_list.append(c)
# for i in range(1,26):
#     multiplier = i+1
#     alphabet_letters = alphabet_list[i]
#     c_list.append(alphabet_letters*multiplier)
# print(c_list)


# # 7
# 
# numbers_of_elements = int(input("Enter number of elements for both of the lists L and M: "))
# 
# L = []
# for i in range(numbers_of_elements):
#     L.append(int(input("Enter an integer for list L: ")))
# print('')
# M = []
# for i in range(numbers_of_elements):
#     M.append(int(input("Enter an integer for list M: ")))
# print('')
# N = []
# for i in range(numbers_of_elements):
#     N_element = L[i] + M[i]
#     N.append(N_element)
# print('')
# print('L list: ', L)
# print('M list: ', M)
# print('N list: ', N)


# # 8
# 
# factors = []
# number = int(input("Enter an integer to factorized: "))
# i = 1
# while i<=number:
#     if number%i == 0:
#         factors.append(i)
#     i+=1
# print("List of factors of {}: {}".format(number,factors))


# # 9
# 
# from random import randint
# 
# die_possible_sum = [2,3,4,5,6,7,8,9,10,11,12] # 11 elements
# die_result = []
# for i in range(10000):
#     dice_A = randint(1,6)
#     dice_B = randint(1,6)
#     die_sum = dice_A + dice_B
#     die_result.append(die_sum)
# print("sum of two die:\t\tnumber of sums:\t\tprobability:")
# for sum in range(len(die_possible_sum)):
#     result_sum = die_possible_sum[sum]
#     sum_quantity = die_result.count(result_sum)
#     print("{0}\t\t\t{2}\t\t\t{3}% ({1}%)".format((result_sum), round((sum_quantity/len(die_result))*100, 1), sum_quantity, round((sum_quantity/len(die_result))*100)))


# # 10
# 
# lst = [1,2,3,4,5,6,7,8,9,10]
# print("Original list: ",lst)
# last_element = lst[len(lst)-1]
# rev_lst = lst[::-1]
# i = 0
# while i<=len(lst):
#     if i == len(lst)-1:
#         del rev_lst[len(lst)-1]
#         rev_lst.insert(len(lst)-1, last_element)
#         break
#     else:
#         rev_lst[i] = rev_lst[i+1]
#     i+=1
# print("Modified list: ",rev_lst[::-1])

# lst = [1,2,3,4,5,6,7,8,9,10]
# last_element = lst[len(lst)-1]
# new_lst = [last_element]
# i=0
# while i<=len(lst):
#     if i == len(lst)-1:
#         break
#     else:
#         new_lst.append(lst[i])
#     i+=1
# print("Original list: ",lst)
# print("Modified list: ",new_lst)


# # 11
# 
# list_of_ones_and_zeroes = [1]
# for i in range(11):
#     for j in range(i):
#         list_of_ones_and_zeroes.append(0)
#     list_of_ones_and_zeroes.append(1)
# print(list_of_ones_and_zeroes)


# # 12
# from random import randint
# 
# zeroes_and_ones = []
# for i in range(100):
#     zeroes_and_ones.append(randint(0,1))
# print(zeroes_and_ones)
# 
# list_breaker = 5
# zeroes_and_ones.append(list_breaker)
# ones_counter_list = []
# zeroes_counter_list = []
# for i in range(len(zeroes_and_ones)):
#     ones_counter = 0
#     zeroes_counter = 0
#     if i >= (len(zeroes_and_ones)-1):
#         break
#     while (zeroes_and_ones[i] == zeroes_and_ones[i+1]):
#         if zeroes_and_ones[i] == 1:
#             ones_counter+=1
#         elif zeroes_and_ones[i] == 0:
#             zeroes_counter+=1
#         elif i+1 >= len(zeroes_and_ones)-1:
#             break
#         ones_counter_list.append(ones_counter)
#         zeroes_counter_list.append(zeroes_counter)
#         i+=1
# print("Largest run of successive ones (1's): ", max(ones_counter_list)+1)
# print("Largest run of successive zero (0's): ", max(zeroes_counter_list)+1)


# # 13
# 
# lst = [1,1,2,3,3,3,4,4,0,0,5,4,4,5]
# new_lst = []
# 
# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)
# print('Original list:\t',lst)
# print('New List:\t',new_lst)


# # 14
# 
# measurements = ['Foot to Inches conversion ', 'Foot to Yard conversion ', 'Foot to Mile conversion ',
#                 'Foot to Millimeter conversion ', 'Foot to Centimeter conversion ', 'Foot to Meter conversion ',
#                 'Foot to Kilometer conversion ']
# formula = [12, (1/3), (1/0.000189394), 304.8, 30.48, 0.3048, 0.0003048]
# unit = ['in', 'yrd', 'mi', 'mm', 'cm', 'm', 'km']
# 
# i = 0
# for conversion in measurements:
#     print("Press '{}' if {}". format(i+1, conversion))
#     i+=1
# choose = int(input('Enter measurement of choice: ')) - 1
# 
# print('\n%s:'%(measurements[choose]).upper())
# foot = int(input('Enter value of foot: '))
# print('{}ft = {}{}'.format(foot,round(formula[choose]*foot, 5), unit[choose]))


# # 15
# 
# from string import punctuation
# from random import randint
# 
# print('Enter letters and functions only!')
# alphabet = [c for c in 'abcdefghijklmnopqrstuvwxyz']
# 
# word = input('Enter a message: ')
# word = word.lower()
# word_list = [c for c in word]
# 
# shift_val = []
# for words in word:
#     for i in range(len(words)):
#         shift_val.append(randint(1,26))
# 
# index = 0
# for char in word_list:
#     
#     # checks if there is space
#     if char == ' ':
#         word_list[index] = word_list[index]
#         
#     # checks if there is punctuations
#     elif any([char==punctuations for punctuations in punctuation]):
#         word_list[index] = word_list[index]
#         
#     else:
#         new_letter_index = (alphabet.index(word_list[index])) + shift_val[index]
#         if new_letter_index >= len(word_list):
#             restartIndex = 26-(alphabet.index(word_list[index]))
#             new_shift_val = shift_val[index] - restartIndex
#             word_list[index] = alphabet[new_shift_val]
#         else:
#             word_list[index] = alphabet[new_letter_index]
#     index+=1
#         
# 
# print('Encrypted message: ',*word_list, sep = '')
# print('shift_val: ',shift_val)
# # print(word_list)
# 
# decrypt = (input('Press \'ENTER\' to decrypt: '))
# 
# jndex = 0
# for char in word_list:
#     
#     # checks if there is space
#     if char == ' ':
#         word_list[jndex] = word_list[jndex]
#         
#     # checks if there is punctuations
#     elif any([char==punctuations for punctuations in punctuation]):
#         word_list[jndex] = word_list[jndex]
#         
#     else:
#         new_letter_index = (alphabet.index(word_list[jndex])) - shift_val[jndex] 
#         print(new_letter_index, end = ', ')
#         if new_letter_index < 0:
#             new_shift_val = 26 - abs(new_letter_index)
#             word_list[jndex] = alphabet[new_shift_val]
#         elif new_letter_index >= 0:
#             word_list[jndex] = alphabet[new_letter_index]
#     jndex+=1
# 
# print('\nDecrypted message: ', *word_list, sep = '')

