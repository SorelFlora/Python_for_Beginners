#!/usr/bin/env python
# coding: utf-8

# # 2 - Variables and Basic Data Types
# ### Exercise:
# Write a program that asks the user to input their name, age, and favorite
# number. Store these values in appropriate variables, then print a message that
# includes all three pieces of information

# In[6]:


name = str(input("Enter your name: "))
try:
    age = int(input("Enter your age: "))
except:
    print("Just do it!")
fav_number = int(input("Enter your favorite number: "))
print("My name is",name,",", "I am",age, "years old and my favorite number is",fav_number,".")


# # 3 - String Manipulation
# ### Exercise:
# Ask the user to input a word. Create a new string that repeats this word three
# times, adds an exclamation mark at the end, and prints the result.

# In[7]:


word = str(input("Input a word: "))
word = word * 3 
word = word + "!"
print(word)


# # 4 - In-Place Operators
# ### Exercise:
# Start with a variable x set to 5. Use in-place operators to:
# • Add 10 to x.
# • Multiply x by 3.
# • Subtract 15 from x.
# • Print the fnal result.

# In[1]:


x = 5
x += 10
x *= 3
x -= 15
print (x)


# # 5 - Booleans
# ### Exercise:
# Write a program that compares two numbers input by the user. Print True if
# the frst number is greater than the second, and False otherwise.

# In[9]:


number_1 = float(input("a = "))
number_2 = float(input("b = "))
if number_1 > number_2:
    print(True)
else:
    print(False)


# # 6 - If Statements
# ### Exercise:
# Create a simple program that checks if a user-entered number is even or odd.
# Print “Even” if the number is even and “Odd” if it’s not.

# In[2]:


num = int(input("user-entered number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# # 7 - Loops
# ### Exercise:
# Write a program that prints the numbers from 1 to 10 using a while loop. Then
# modify it to print only the even numbers from 1 to 10.

# In[1]:


y = 1
while y <= 10:
    print(y)
    y += 1


# In[1]:


y = 1
while y <= 10:
    if y % 2 == 0:
        print(y)
    y += 1


# # 8 - Functions and Arguments
# ### Exercise:
# Define a function greet user(name) that takes a user’s name as an argument and
# prints a personalized greeting. Call the function with at least three diﬀerent
# names.

# In[11]:


def greet_user(name):
    print("Good Morning " + name)
greet_user("Marc") 
greet_user("Jeanne")
greet_user("Josué")   


# # 9 - Returning from Functions
# ### Exercise:
# Create a function multiply numbers(a, b) that returns the product of two numbers. Use this function to multiply three diﬀerent pairs of numbers, and print
# the results.

# In[11]:


def multiply_number(x,y):
    return(x*y)
x1 = multiply_number(7,8)
x2 = multiply_number(9,4)
x3 = multiply_number(11,10)
print(x1, x2, x3)
type(x1)


# # 10 - Github
# ### Exercise:
# 1 • What is GitHub?
# 
#  • What is the diﬀerence between Git and GitHub?
# 
# 2 • What is GitHub used for, and why is it important?
# 
#  • Create a GitHub repository named Python for Beginners.
# 
#  • Upload your notebook to the GitHub repository.
# 
#  • Convert your notebook to a .py file and upload it to GitHub.

# #### 1.  GitHub: is an online software development platform where people store, track and collaborate on software projects.
# - The difference between Git and GitHub is that: Git is a free, open source version control tool that developers install locally on their personal computers, while GitHub is a pay-for-use online service built to run Git in the cloud. 
# 2. GitHub allows software developers and engineers to create remote, public-facing repositories on the cloud for free.
# - GitHub is important because it allows collaoration with developers from all over the world, its also enables potential developers to contribute and share their knowledge to benefit the global community.
# 
