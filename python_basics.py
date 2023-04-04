


num =  3
print(type(num))
 #will drop the decimal on the division just integer result
print(3//2)

#exponent
print(3**2)
#absolute
print(abs(-2))
#round
print(round(3.75))

num1 = '100'
num2 = '200'
print(num1+num2)
#cast these strings to integers
num1 = int(num1)
num2 = int(num2)
print(num1+num2)

#Lists
#list of values
#indexing  in python starts from 0. 
courses = ['History','Math','phy', 'CS']
print(courses)

print(len(courses))
print(courses[3])
print(courses[-1])
#courses[0:2] will print courses at 0 and 1 index not 2.
print(courses[0:2])
print(courses[2:])

#add an element towards the end of the list - use append
courses.append('Art')
print(courses)

#add an element at a specific index - use insert(index, element). This is will move all the elements by  one unit from index it was added
courses.insert(0,'Bio')
print(courses)

courses = ['History','Math','phy', 'CS']
courses_2 = ['Art','Bio']
#using insert here will create a list of lists. Hence use extend
courses.insert(0,courses_2)
print(courses)

#add another list of items to a list : extend(): This is will add art and bio to the end of courses
courses = ['History','Math','phy', 'CS']
courses_2 = ['Art','Bio']
courses.extend(courses_2)
print(courses)

#remove a specific value from a list
courses.remove('Math')
print(courses)

#use pop to remove the last element from the list. This will also return the values of the element that was popped
popped = courses.pop()
print(popped)
print(courses)

#sorting a list: 
#1. reverse(): it will directly apply the change on the list
courses.reverse()
print(courses)

#2. sort() for string it will sort according to the starting alphabet . sorted will not directly change the list  
print(sorted(courses))


#min 
#max
#sum

num_1 = [1,5,3,4,7]
print(min(num_1))
print(max(num_1))
print(sum(num_1))

#index of a certain value in the list : index()
print(courses.index('CS'))

#if a values in the list or not in()
print('CS' in courses)
print('Bio' in courses)

#enumerate():  access the index and value in the lisst
for index, course in enumerate(courses):
    print(index, course)

for index, course in enumerate(courses, start =1):
    print(index, course)


#join() elements of string by a delimiter 
courses_str = ' - '.join(courses)
print(courses_str)

#split(): split the elements separated from a delimiter
new = courses_str.split(' - ')
print(new)

#Empty list (2methods)
empty_list =[]
empty_list = list()


#TUPLEs: are just like lists by immutable: meaning cannot change their values

#creating a list : Lists are mutable: can be changed
list_1 = ['Hist','Math','Phy','CS']
list_2 = list_1

print(list_1)
print(list_2)

#here changing one value in index 0 in the list_1 can alter the value in 0th index in list_2
list_1[0] = 'Art'
print(list_1)
print(list_2)

#so in cases where you don't want the values of the elements to change, use tuples
tup_1 = ('Hist','Math','Phy','CS')
tup_2 = list_1

print(tup_1)
print(tup_2)

#here changing one value in index 0 in tup_1 will throw an error " TypeError: 'tuple' object does not support item assignment"
tup_1[0] = 'Art'
print(tup_1)
print(tup_2)

#empty tuple (2methods)
empty_tuple = ()
empty_tuple = tuple()



#SETS : Unordered and immutable
#SETS only stores unique values
courses = {'Hist','Math','Phy','CS'}
print(courses)

#Sets can store only unique values
courses = {'Hist','Math','Phy','CS','CS'}
print(courses)

#intersection and difference
#intersection() : shows only the common elements in both sets
cs_courses = {'Hist','Math','Phy','CS'}
art_courses = {'Hist','Math','Design','Art'}
print(cs_courses.intersection(art_courses))

#difference() : shows only the elements that are different in cs_courses that are not in art_courses
print(cs_courses.difference(art_courses))

#union() :  shows all elements in both sets
print(cs_courses.union(art_courses))

#empty set
#this will not work empty_set = {}
empty_set = set()


#DICTIONARIES {'key':'value'}
student = {'name':'John', 'age': 25, 'courses':['Math','CS']}
print(student['courses'])

#Accessing using .get() will return None if the key does not exist. Can also set it to 'Not found' if the key is not found in the dictionary
print(student.get('phone'))
print(student.get('phone','Not found'))

#update() :  to update the student information
student.update({'name': 'Jane', 'age' : 26,'phone': '555-555'})
print(student)


#del : To delete a key
del student['age']
print(student)

#pop() : To delete a key
student.pop('phone')
print(student)

#len() : to get number of keys in the dictionary
print(len(student))

#keys() :  to get the keys of the dictionary
print(student.keys())

#item() : to get both keys and values
print(student.items())

#traversing through dictionary using for loop
for key, value in student.items():
    print(value)


"""CONDITIONALS (IF ELSE)
#if (condition):
        #statement
#elif (condition):
    #statement
#else :
    #statement """

#Loops and interations
#for loop
nums = [1,2,3,4,5]
for num in nums:
    print(num)

#break: break out of loop
for num in nums:
    if num == 3:
        print('Found!')
        break
    print(num)

#continue: to ignore a step in the loop. Even after finding 3, instead of breaking our of the loop, it will continue to process 4 and 5
for num in nums:
    if num == 3:
        print('Found!')
        continue
    print(num)


#nested loop
for num in nums:
    for letter in 'abc':
        print(num,letter)
#range : continuous values from 0. If want to start from another value, give starting value also
for i in range(10):
    print(i)

for i in range(1,10):
    print(i)

#while loop
x=0
while x<10:
    print(x)
    x+=1

x=0
while True:
    if x==5:
        break
    print(x)
    x+=1


#FUNCTIONS
#def to define a function
#To leave the function blank without any functionality, use pass keyword to not throw an error
def hello_func():
    pass

def hello_fun():
    print("Hello")

hello_fun()

def hello_fun1():
    return 'Hello Function'

print(hello_fun1().lower())

#passing parameter and a default value for one of the parameter
def hello_fun2(greeting, name = 'You'):
    return '{},{}'.format(greeting,name)

print(hello_fun2('Hi'))

#args (non keyword argument)
#kwargs (keyqord argument): A keyword argument is where you provide a name to the variable as you pass it into the function.
#We use the “wildcard” or “*” notation like this – *args OR **kwargs – as our function’s argument when we have doubts 
# about the number of  arguments we should pass in a function.

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['March','Art']
info = {'name':'John','age':22}
#passing courses and info directly will not unpack courses to positional argument and info to keyword argument
student_info(courses,info)
#so for automatic unpacking use
student_info(*courses,**info)

#IMPORTING MODULES
#importing a user defined python script my_module from the same directory of this python_basics.py file
import my_module
courses = ['History','Math','phy', 'CS']
index = my_module.find_index(courses,'Math')
print(index)

#we can specify a nickname for my_module so that we don't have to keep writing my_module every time
import my_module as mm
courses = ['History','Math','phy', 'CS']
index = mm.find_index(courses,'Math')
print(index)

#if you just want to import a function from my_module instead of the entire script
#will give access to only this function find_index
from my_module import find_index
courses = ['History','Math','phy', 'CS']
index = find_index(courses,'Math')
print(index)

#will give access to only this function find_index and test variable in my_module script
from my_module import find_index, test
courses = ['History','Math','phy', 'CS']
index = find_index(courses,'Math')
print(index)
print(test)

#to import everything use *
from my_module import *
courses = ['History','Math','phy', 'CS']
index = find_index(courses,'Math')
print(index)
print(test)

#sys.path module will return the directories that python is looking for when I import my_module
#it looks in the same directory of this current file from which we are importing my_module, python standard libraries, etc
from my_module import find_index, test
import sys
print(sys.path)

#now if I moved my_module to another location different from the same directory that this file is stored:
#it will throw an error saying no module names my_module. 
# one approach: So we need to add this changed path to sys.path.append to ask python to look for this module in the new location
import sys
sys.path.append('/Users/anuram/Desktop/trial')
from my_module import find_index, test

#method 2: include this path in the environment variable

#os module in python: this willgive access to the underlying operating system
import os
#getcwd() : current working directory
print(os.getcwd())
#os.chdir('path'): change working directory
#os.listdir(): will list all the files in the current working directory
print(os.listdir())
#os.makedirs('path'): create sub directories and nested sub folders
#os.mkdir('path'): can only make one subdirectory at a time cannot create layers of sub folders
#os.rmdir('path'): remove a directory 
#os.removedirs('path'): remove sub directories
#os.rename('original name','new name'): rename a file
#os.stat('file name'): status and other info about th e file
#os.walk: to traverse through the directory: all files names, subfolders
import os
for dirpath, dirnames, filenames in os.walk('/Users/anuram/Desktop/'):
    print('current path:', dirpath)
    print('directories:', dirnames)
    print('Files:', filenames)

#os.path.join(path1, file 1): can join a path and file name to generate a new path

#Read and write a file
