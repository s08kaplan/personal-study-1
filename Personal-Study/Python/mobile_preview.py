# -*- coding: utf-8 -*-
"""mobile_preview.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NZBV-T1LeDPK11g8e6uvXapkYmRp2xSg
"""

def New(*num):
     return (sum(i**2 for i in num))**0.5

def area_triangle(a,b):
    return (a*b)/2

def area_rectangle(a,b):
     return a*b

a = int(input("Please enter a positive integer : "))
b = int(input("Please enter a positive integer: "))
x = New(a,b)
y = area_triangle(a,b)
z = area_rectangle(a,b)

if x > y and x > z:
     print("hypotenuse won")
elif y > x and y > z:
     print("Triangle won")
else:
     print("Rectangle won")

import random

x = random.randint(1,100)
y ={
   a:"Adam",
   b:"Brian",
   c:"Cynthia",
   d:"David"
}
count = 0
print("Let\'s play a game")
print("You have 5 guesses")
print("If you find the number or one of the names you'll win")
z = int(input("Please enter a number from 0 to 100 : "))
q = input("Please guess a name : ")
q_new = q.title()
if (q_new == y.items(a) or q_new ==y.items(b) or q_new == y.items(c) or q_new == y.items(d)) or x > z :

  count+=1

  print(f"Higher than your guess and {5-count} guesses left")
elif (q_new == y.items(a) or q_new ==y.items(b) or q_new == y.items(c) or q_new == y.items(d)) or x < z :
  count+=1
  print(f"Less than your guess and {5-count} guesses left")

import random
x = random.randint(1,100)
y = int(input("Please enter a number from 0 to 100 : "))
count = 0
while count < 6:
    if y < x :
       print("higher than your guess")
       print(int(input("Please guess again : ")))
       count+=1
    elif y > x:
       print("Less than your guess")
       print(int(input("Please guess again : ")))
       count+=1
    else:
       print("You're good at this game")

def is_leap(year):
    leap = False
    if year % 4 == 0:
        return (not leap)
    else:
        return leap
year = int(input())
print(is_leap(year))

def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        return leap

year = int(input("Enter a year: "))
print(is_leap(year))

def is_leap(year):
    leap = False
    if year % 4 == 0:
       if year%400==0:
          return (not leap)
    elif year%100!=0:
        return leap
    else:
        return leap
year = int(input())
print(is_leap(year))

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Read the year from input
year = int(input())

# Call the is_leap function and print the result
print(is_leap(year))

n = int(input())
for i in range(1,n+1):
    x = i
    i+=i
    print(x,end="")

x = int(input())
y = int(input())
z = int(input())
n = int(input())

result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k<n ]
print(result,end="")

x = int(input("Please enter a number list you want : "))
x = list(x)
for i in x:
    y= max(i)
    z=x.remove(y)
    for j in z:
       second = max(j)
print(second)

import math

x = [1,23,25,43,16,34,76,98]
largest = max(x)
x.remove(largest)
second_largest=max(x)

x = int(input("Enter a number : "))
y=[]
for i in range(1,x+1):
    y.append(i)
    result= sorted(y,reverse=True)

print(result[1])

n = int(input())
arr = list(map(int,input().split()))
arr = list(set(arr))
result = sorted(arr,reverse=True)
print(result[1])

#Write a function to check if a given string is a palindrome
def palindrome(value):
    if value[::] == value[-1::-1]:
       print(f"Your sentence {value} is a palindrome")
    else:
       print("Sorry your sentence is not a palindrome")
palindrome("Night")
palindrome("aka")

#Create a program that takes a list of words and returns a new list containing only the words with even lengths.
your_list = input("please enter a sentence with a few words : ")
even_list = []
def even_length(value):
    words= list(your_list.split())
    for i in words:
        if len(i) % 2 == 0:
           even_list.append(i)
           print(even_list)
even_length(your_list)

def fibonacci_recursive(n):
      if n <= 0:
         return 0
      elif n == 1:
         return 1
      else:
         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Example usage
n = int(input("Enter the value of n: "))
result = fibonacci_recursive(n)
print("The", n, "th term of the Fibonacci sequence is:", result)

#Kth Largest Element: Write a function to find the kth largest element in an unsorted list.

my_list = [1, 2, 3, 23, 45, 16, 61, 89, 36]
n=int(input("which largest number should I find for you : "))
def largest_num(value):
     my_list = list(set(my_list))
     my_list = sorted(my_list,reverse=True)
     print(my_list[n])
largest_num(my_list)

'''Certainly! Here are a few programming problems for you to solve using Python:

Problem 1: Write a Python program to find the factorial of a number.

Problem 2: Write a Python program to check if a given number is prime or not.

Problem 3: Write a Python program to reverse a string.

Problem 4: Write a Python program to find the sum of all the elements in a list.

Problem 5: Write a Python program to remove duplicates from a list.

Choose any problem you'd like to solve, and I'll be happy to provide guidance and assistance along the way!'''

#chatgpt
my_list = [1, 2, 3, 23, 45, 16, 61, 89, 36]
k = int(input("Which largest number should I find for you: "))

def kth_largest_number(lst, k):
    unique_list = list(set(lst))
    sorted_list = sorted(unique_list, reverse=True)

    if k > 0 and k <= len(sorted_list):
        return sorted_list[k - 1]  # Adjust for 0-based indexing
    else:
        return None  # Return None if k is out of range

result = kth_largest_number(my_list, k)

if result is not None:
    print(f"The {k}th largest number is:", result)
else:
    print("Invalid k value. Please enter a valid k.")

#3)
sent = input("please enter a string : ")
reverse_input = []
def reverse_sent(sent):
   a = sent[::-1]
   reverse_input.append(a)

reverse_sent(sent)
print(reverse_input)

#2)chatgpt
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6

    return True

# Input from the user
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

def find_sum(elements):
    total = 0
    for element in elements:
        total += element
    return total

# Input from the user
numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]

sum_of_elements = find_sum(numbers)
print("Sum of the elements:", sum_of_elements)

#Problem 5: Write a Python program to remove duplicates from a list.

def remove_duplicate(item):
    user = input("Please enter some values : ")
    user  = set(list(user.split()))
    return user
print(user)
remove_duplicate(user)

def try_1(items):
    u_list = set(items.split())
    return u_list

u_list = input("Enter some values with spaces among them: ")
result = try_1(u_list)
print(result)

def try_1(items):
    u_list = set(items.split())
    return u_list


u_list = input("Enter some values with spaces among them: ")
result = try_1(u_list)
print(try_1(u_list))

'''Given a sentence, write a Python
program to reverse the order of words
in the sentence.'''

def given_reverse(item):
    given =item.split()
    reversed_given = ' '.join(reversed(given))
    return reversed_given
given = "hi how are you "
print(given_reverse(given))
print(given.index("you"))

def factorial(n):
    i = 1
    while n>=1:
       i*=n
       n -= 1
    return i
num = int(input ("Please enter a number : "))
print(factorial(num))

'''Exercise 9: Find the largest item
from a given list'''
given_list = [1,4,16,23,18,17,36,"Ali","Daniel","Jenny", "Alice"]
numbers = []
names = []
for i in given_list:
    if type(i) == int:
       numbers.append(i)
    else:
       names.append(i)
print(numbers)
print(names)

'''Exercise 9: Find the largest item
from a given list'''
import math
given_list = [1,4,16,23,18,17,36,"Ali","Daniel","Jenny", "Alice"]
numbers = []
names = []
for i in given_list:
    if type(i) == int:
       numbers.append(i)
       new_num = sorted(numbers,reverse=True)
    else:
       names.append(i)
    names = names.split()
    for j in names:

       result = max(len(j))

print(numbers)
print(names)
print(f"the largest number in your list is : {new_num[0]}")
print(f"the largest word in your list is : {result} ")

given_list = [1, 4, 16, 23, 18, 17, 36, "Ali", "Daniel", "Jenny", "Alice"]
numbers = []
names = []

for item in given_list:
    if isinstance(item, int):
        numbers.append(item)
    else:
        names.append(item)

largest_number = max(numbers)

longest_word = max(names, key=len)

print(f"The largest number in the list is: {largest_number}")
print(f"The longest word in the list is: {longest_word}")

given_list = [1, 4, 16, 23, 18, 17, 36, "Ali", "Daniel", "Jenny", "Alice"]
largest_number = None
longest_word = ""

numbers = []
names = []

for item in given_list:
    if isinstance(item, int):
        numbers.append(item)
        if largest_number is None or item > largest_number:
            largest_number = item
    elif isinstance(item, str):
        names.append(item)
        if len(item) > len(longest_word):
            longest_word = item

print(f"The largest number in the list is: {largest_number}")
print(f"The longest word in the list is: {longest_word}")

'''10. Write a Python program that
accepts an integer (n) and computes
the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615'''
n= input("Please enter a number : ")
n = str(n)
num1 = n+n
num2 = n + n + n
result = int(n) + int(num1) +int(num2)
print(result)

'''Problem: Given a list of integers,
use map and a lambda function
to create a new list containing
the squares of the original numbers.'''

num = [23,15,17,26,34,28,91]
sqr = list(map(lambda x: x**2, num))
print(sqr)

'''Problem: Write a Python program
to filter out all the even numbers
from a list of integers using
the filter function and a
lambda function.'''

list_1 = input("Please enter some integers with space between them : ")
list_1 = list(map(int,list_1.split()))
evens = list(filter(lambda x: x % 2 ==0,list_1))
print(evens)

'''Problem: Given a list of strings,
use map and a lambda function
to create a new list containing
the lengths of each string.'''

a = ["ali", "burak", "jenny", "alice","robert", "jennifer", "daniel"]
len_items = list(map(lambda x : len(x),a))
print(len_items)

a = ["ali", "burak", "jenny", "alice", "robert", "jennifer", "daniel"]
new_a = list(map(lambda x: (x, len(x)), a))
print(new_a)

'''Problem: Implement a function
that takes a list of numbers and
a threshold value. Use filter and
a lambda function to return a
new list with only the numbers
greater than the threshold.'''

def wanted(numbers):
    desire = list(filter(lambda x : x > 15,numbers))
    return desire
num = [1,13,2,4,3,46,53,77,8,6,5]
print(wanted(num))

# chatgpt solution
def wanted(numbers, threshold):
    desire = list(filter(lambda x: x > threshold, numbers))
    return desire

num = [1, 13, 2, 4, 3, 46, 53, 77, 8, 6, 5]
threshold_value = 15
result = wanted(num, threshold_value)
print(result)

'''Problem: Write a Python program
to capitalize the first letter of
each word in a list of strings
using map and a lambda function.'''

user_list = input("Please write some strings with spaces between them : ")
def capitalize_func(value):
  cap = list(map(lambda s : s.capitalize(),value.split()))
  return cap

print(capitalize_func(user_list))

'''Problem: Given a list of names,
use filter and a lambda function
to filter out all the names that
have fewer than 5 characters.'''

user_choice = input("Please enter some names with spaces between them : ")
def filt_name(names):
  last_list = list(filter(lambda s : len(s) < 5, names.split()))
  return last_list
print(filt_name(user_choice))

def filt_name(names):
    last_list = list(filter(lambda s: len(s) < 5, names.split()))
    last_list = [name.capitalize() for name in last_list]  # Capitalize the first letter
    return last_list

user_choice = input("Please enter some names with spaces between them: ")
result = filt_name(user_choice)
print(result)

'''Problem: Write a Python program
to convert a list of temperatures
in Celsius to Fahrenheit using map
and a lambda function. The formula
is F = (C * 9/5) + 32.'''

def converter(number):
    result = lambda x : (x *9/5) + 32
    return result(number)

print(converter(30))

celsius_temps = [25, 30, 15, 10, 5]

fahrenheit_temps = list(map(lambda c: (c * 9/5) + 32, celsius_temps))

print("Celsius Temperatures:", celsius_temps)
print("Fahrenheit Temperatures:", fahrenheit_temps)

your_list = input("Please enter some strings with spaces between them: ")

def vowel_start(value):
    vowels = ['a', 'e', 'i', 'o', 'u']
    new = list(filter(lambda s: s[0].lower() in vowels, value.split()))
    return new

result = vowel_start(your_list)
print(result)

'''Problem: Implement a function
that takes a list of strings and
returns a new list containing only
the strings that start with a vowel.'''
your_list = input("Please enter some strings with spaces between them: ")


def vowel_start(value):
    vowels=['e','i','o','u','a']
    new = list(filter(lambda s : s[0].lower() in vowels,value.split()))
    return new

result = vowel_start(your_list)
print(result)

'''Problem: Given a list of numbers,
use map and a lambda function
to calculate the factorial of
each number.'''

def factorial(n):
    return n * factorial(n - 1) if n > 0 else 1

numbers = [5, 3, 7, 0, 10]
result = list(map(factorial, numbers))
print(result)

def factorial(n):
    return n * factorial(n - 1) if n > 0 else 1

numbers = [5, 3, 7, 0, 10]
result = list(map(factorial, numbers))
print(result)

def factorial(number):
    if number == 1:
       return 1
    elif number <= 0 :
       return 0
    else:
       result = number * factorial(number  - 1)
       return result
print(factorial(5))

'''Problem: Write a Python program to
find the common elements between
two lists using filter and a lambda
function.'''

a = [1,3,5,4,7,10]
b = [1,5,8,9,10]

def common(k,l):
    c = list(filter(lambda x : x in k,l))
    return c

print(common(a,b))

'''Problem: Implement a function that
takes a list of strings and returns
a new list containing only the strings
that are palindromes'''
your_list = input("Please enter some strings with spaces between them : ")
def palindrome(sentence):
    new = list(filter(lambda s: s[::]==s[::-1],sentence.split()))
    return new
print(palindrome(your_list))

'''Problem: Implement a function that
takes a list of strings and returns
a new list containing only the strings
that are palindromes'''
your_list = input("Please enter some strings with spaces between them : ")
def palindrome(sentence):
    new = list(filter(lambda s: s.lower()[::]==s.lower()[::-1],sentence.split()))
    return new
print(palindrome(your_list))

'''Problem: Given a list of dictionaries
containing student information
(name, age, grade), use map and
a lambda function to create a new list
of student names.'''

a = {
       "name" : "Adam",
       "age" : 23,
       "grade" : 80
       }
b = {
       "name" : "Jenny",
       "age" : 25,
       "grade" : 85
}
c = {
       "name" : "Daniel",
       "age" : 22,
       "grade" : 90
}
name_list = list(map(lambda s: s["name"], (a,b,c)))
age_list = list(map(lambda n: n["age"],(a,b,c)))
grade_list = list(map(lambda grade : grade["grade"],(a,b,c)))
print(name_list)
print(age_list)
print(grade_list)

'''Problem: Write a Python program to
filter out all the negative numbers
from a list of integers using filter
and a lambda function.'''
numbers = input("Please enter some positive and negative integers : ")
numbers = list(map(int,numbers.split()))
def chosen(number):
    negatives = list(filter(lambda x : x < 0,number))
    return negatives
print(chosen(numbers))

'''Write a Python program that takes
a string as input and prints the
number of uppercase and lowercase
letters in the string.'''

def number_chosen(sentence):
    upper_count = sum(1 for char in sentence if char.isupper())
    lower_count = sum(1 for char in sentence if char.islower())
    return upper_count, lower_count

words = input("Please enter some strings with uppercase and lowercase letters mixed with spaces between the strings: ")
upper_count, lower_count = number_chosen(words)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)

#chatgpt solution
def count_upper_lower(sentence):
    upper_count = 0
    lower_count = 0

    for char in sentence:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1

    return upper_count, lower_count

words = input("Please enter some strings with uppercase and lowercase letters mixed with spaces between the strings: ")
upper_count, lower_count = count_upper_lower(words)
print("Number of uppercase letters:", upper_count)
print("Number of lowercase letters:", lower_count)