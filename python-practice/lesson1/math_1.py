# Write a Python program to count the number of
# items in a dictionary that have a value greater than a certain number.

my_diet = {"apple": 5, "mango":3, "orange": 4, "beans": 8}
value = 5
count = len([x for x in my_diet.values() if x < value])
print(count)


# Declare a function named sum_of_numbers. It takes a number parameter,
# and it adds all the numbers in that range.
def sum_of_numbers(num):
    return sum(range(num+1))

print(sum_of_numbers(10))


 
# create a function that doubles the odd numbers in a list

def double_odd_numbers(lst):
   
    doubled_list = []
    for num in lst:
        if num % 2 != 0: 
            doubled_list.append(num * 2)
        else:
            doubled_list.append(num)
    return doubled_list

lst = [1, 2, 3, 4, 5, 6]
double_odd_numbers(lst)



# Write a Python program to count the number of vowels in a string.
def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for s in string:
     if s in vowels:
         count+=1
    return count
        
# string = "pauline"
# print(count_vowels(string))




# Write a Python program to reverse a given string.
# method 1
# def reverse(s):
#    if len(s)==0:
#        return s
#    else:
#        return reverse(s[1:])+ (s[0])
   
    
# s = "chapati"
# print(reverse(s))

# method 2
# def str_reverse(b):
#     empty =""
#     for i in b:
#         empty = i+empty
#     return empty

# b = "Nairobi"
# print(str_reverse(b))

# method 3
def reversing_str(n):
   strr = n[::-1]
   return strr

n = "Kenya"
print(reversing_str(n))
    

def check(fruits):
    return fruits.pop()
fruits = ["apple", "plum", "pears"]
print(check(fruits))



def set_list(names):
    empty = {}
    for n in names:
        if n in empty:
            empty[n]+=1
        else:
            empty[n] = 1
      
    return empty      
            
empty = ["Juana", "Lisa","Mary", "Mary"]
print(empty)  



def count_list(*string2):
    empty2 = {}
    for x in string2:
        if x in empty2:
            empty2[x]+=1

    else:
        empty2[x]=1  
    return empty2 
string2 = ["Paulineefg"]    
print(count_list(string2))              
     
# sort a nested list in a descending order
def sort_list(nums):
    new_list = []
    for x in nums:
        sorting = sorted(x, reverse=True)
        new_list.append(sorting)
        
    return new_list
    
    
nums = [[2,3,1],[7,8,9]]  
print(sort_list(nums))
         
    
         
         
         



