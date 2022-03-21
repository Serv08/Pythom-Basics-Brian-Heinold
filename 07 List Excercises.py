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

lst = []
try:
    print("Hit 'Enter' when done!")
    while True:
        ele = int(input("Enter a number between 1 and 12: "))
        lst.append(ele)
        if ele>12 or ele<1:
            print("Between 1 and 12 only!")
            del lst[len(lst)-1]
#         print(lst)
except Exception:
    orig_lst = lst[:]
    print("Done!\n")
finally:
#     gt_10 = [integers for integers in lst if integers>10]
#     for i in range(len(lst)):
#         x = lst[i]
#         for j in range(len(gt_10)):
#             y = gt_10[j]
#             if x == y:
#                 gt_10_position_in_lst = lst.index(x)
#                 del lst[gt_10_position_in_lst]
#                 lst.insert(gt_10_position_in_lst, 10)
    i = 0
    while i < len(lst):
        if lst[i] > 10:
            lst[i] = 10
        i+=1
print("Original List: ", orig_lst)
print("Current List", lst)
    