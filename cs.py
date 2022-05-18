from collections import defaultdict
from itertools import count
from math import perm
import random
#print prime numbers in a range
'''
l,u = int(input('enter lower limit: ')), int(input('enter upper limit: '))
for i in range(l, u):  
    t=1
    for j in range(2,i//2):
        if i%j==0:
        t=0
        break
     
  if t:
    if i!=1 and i!=0:
      print(i)

'''


#armstrong number or not?
'''
n=int(input('enter a number: '))
a,b=0,n
while n>0:
  r=n%10
  n//=10
  a+=(r**3)
  
if a==b:
  print('yes')
else:
  print('no')
'''


#armstrong numbers in a range: 
'''
l,u = int(input('enter lower limit: ')), int(input('enter upper limit: '))
for i in range(l, u):
    a=0
    b=i
    while i>0:
        r=i%10
        i//=10
        a+=(r**3)
    
    if a==b:
        print(a)
'''

#print diamond pattern:
'''
n=int(input('enter a number: '))
for i in range(1,n):
    print(' '*(n-i), end=' ')
    for j in range(1, i+1):
        print(' ', end=' ')
    print()

for k in range(n-2,0,-1):
    print(' '*(n-k), end=' ')
    for l in range(k+1,1,-1):
        print(' ', end=' ')
    print()
'''


#number of students in a class
#number of subjects
'''
students = int(input('enter the number of students: '))
toootal = 0
for i in range(1,students+1):
    subjects = int(input(f'enter the number of subjects for student {i}: '))
    marks = [int(input(f'enter the number of marks for subject {k}: ')) for k in range(1,subjects+1)]
   
    print(f'total marks for student {i} are: {sum(marks)}')
    toootal+=sum(marks)

print(f'total marks of the class are: {toootal}')
'''


#marks for students and class...

'''
marks_subjects = {}
students = int(input('enter the number of students: '))

for i in range(1,students+1):

    no_of_subjects = int(input(f'\nenter the number of subjects for student{i}: '))

    subjects = [input(f'\n\tenter name of subject {j} for student {i}: ') for j in range(1,no_of_subjects+1)]
    a=0
    for k in subjects:
        marks_in_k = int(input(f'\n\t\tenter number of marks obtained by student {i} in {k}: '))
        if k not in marks_subjects:
            marks_subjects[k] = 0
        marks_subjects[k] += marks_in_k
        a+=marks_in_k
    
    print(f'\n\t\ttotal marks for student {i} are: {a}')
    
#print(marks_subjects)

for l in marks_subjects.keys():
    print(f'\n\ntotal marks of the class in {l} are {marks_subjects[l]}')
'''

#compare strings by ascii:
'''
s1=input('enter a string: ')
s2=input('enter a string: ')
a=0
greater = max(len(s1), len(s2))
for i in range(greater):
    if s1[i]!=s2[i]:
        if s1[i]>s2[i]:
            print('first string > second string')
            break
        else:
            print('second string > first string')
            break
    else:
        a+=1

if a==len(s1):
    print('both strings are equal')
'''

#count function:
'''
s=input('enter a string: ')
substr = input('enter substring you want to find: ')
count=0
for i in range(len(s)):
    if s[i:i+len(substr)] == substr:
        count+=1
print(count)
'''

#capitalize first charecter of strings
'''
s=input('enter a string: ')
not_chars =' ;''"",./<>|\§!@#$%^&*()1234567890'

for i in range(len(s)):
    if s[i] not in not_chars:
        first_char = s[i]
        break
a = s.index(first_char)
print(s[:a] + first_char.upper() + s[a+1:])
'''

#implement replace
'''
s=input('enter a string: ')
replace=input('replace what: ')
replace_with=input('replace with: ')
a=s.count(replace)
ans=s
#print(a)
while a!=0:

    j=ans.find(replace)
    #print(j)
    ans=ans[:j] + replace_with + ans[j+len(replace):len(ans)]
    a-=1

print(ans)
'''

#number of occurences of each element in a list
'''
n=int(input('enter the number of elements in list: '))
l = [int(input(f'enter {i+1} element of list: ')) for i in range(n)]

digits_value={}

for j in l:
    if j not in digits_value:
        digits_value[j]=0
    digits_value[j]+=1

print()
for k in digits_value.keys():
    print(f'number {k} occurs {digits_value[k]} times in the list')
'''

#smallest and largest element in a list:
'''
n=int(input('enter number of elements in list: '))
l =[int(input(f'enter {i+1} element of list: ')) for i in range(n)]

a=0
for j in l:
    if j>a:
        a=j
b=a
for k in l:
    if k<b:
        b=k


print(f'smallest element is {b}')
print(f'largest element is: {a}')
'''

#reverse list:
'''
n=int(input('enter number of elements in list: '))
l =[int(input(f'enter {i+1} element of list: ')) for i in range(n)]

for j  in range(0,n//2):
    l[j], l[-j-1] = l[-j-1], l[j]

print(l)
'''

#swap adjacent elements of a list
'''
n=int(input('enter number of elements in list: '))
l =[int(input(f'enter {i+1} element of list: ')) for i in range(n)]
if n%2==0:
    for i in range(0,len(l),2):
        l[i], l[i+1] = l[i+1], l[i]
    print(l)
else:
    print('list has odd elements')
'''

#make 2 lists of elements with multiple occurences and single occurence in a given list
'''
n=int(input('enter number of elements in list: '))
l=[int(input(f'enter {i+1} element of list: ')) for i in range(n)]
multiple_elements = []
single_element = []
digits_value={}

for j in l:
    if j not in digits_value:
        digits_value[j]=0
    digits_value[j]+=1

for k in digits_value.keys():
    if digits_value[k] > 1:
        multiple_elements.append(k)
    else:
        single_element.append(k)

print(f'list of multiple elemetnst is : {multiple_elements}')
print(f'list of single elements is : {single_element}')

#same thing but with lists:

n=int(input('enter number of elements in list: '))
l=[int(input(f'enter {i+1} element of list: ')) for i in range(n)]

multiple_elements=[]
multiple_elememts_multiple=[l[i] for i in range(len(l)) if l[i] in l[i+1:]+l[:i]]
for j in multiple_elememts_multiple:
    if j not in multiple_elements:
        multiple_elements.append(j)

single_elements=[l[i] for i in range(len(l)) if l[i] not in l[i+1:]+l[:i]]

print(multiple_elements)
print(single_elements)

'''

#bubble sort:
'''
l = [7,6,5,3,7,4]
for i in range(len(l)):
    for j in range(i, len(l)):
        if l[i]>l[j]:
            l[i], l[j] = l[j], l[i]
print(l)
'''

#implement insert() function but insert in ascending order:
'''
l=[4,5,8,9]
a=int(input('enter element to be inserted: '))
if a>l[-1]:
    l = l + [a]
elif a<l[0]:
    l = [a] + l
else:
    for i in range(len(l)):
        if a>l[i] and a<l[i+1]:
            l = l[:i+1] + [a] + l[i+1:]
            break
print(l)
'''

#print element with highest frequency:
'''
n=int(input('enter number of elements in list: '))
l=[int(input(f'enter {i+1} element of list: ')) for i in range(n)]
a=0
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if l[i]==l[j]:
            c+=1
    if a<=c:
        a=c
        ans=l[i]
print(ans)
'''

#combination of list of numbers and letters
'''
letters = ['a','b','c','d']
numbers = [1,2,3]
combination = []

for i in numbers:
    for j in letters:
        combination.append(str(i)+str(j))
print(combination)
'''

#longest string in list of strings:
'''
strings = ['abcas', 'abcdasdfasf', 'abcdef', 'ok']
a=0
for i in strings:
    c=0
    for j in i:
        c+=1
    if a<=c:
        a=c
        ans=i
print(ans)
'''

#reverese all strings in list:
'''
strings = ['abc', 'abcd', 'abcde', 'abcdef', 'ok']
for i in range(len(strings)):
    letters = [j for j in strings[i]]
    for ii in range(len(letters)//2):
        letters[ii], letters[-ii-1] = letters[-ii-1], letters[ii]
    a=''
    for iii in letters:
        a+=iii
    strings[i] = a
print(strings)
'''
#merge to lists in ascending order in 3rd list:

'''
l1 = [2,3,5,6,10,11]
l2 = [1,2,4,7,8,9,11]
l3=[]
k,j=0,0
while j!=len(l1) or k!=len(l2):
    if l1[j] > l2[k]:
        l3.append(l2[k])
        k+=1

    elif l1[j] < l2[k]:
        l3.append(l1[j])
        j+=1

    elif l1[j]==l2[k]:
        l3.append(l1[j])
        j+=1
        k+=1

less = min(j,k)
if less==j:
    l3+=l1[j:]
else:
    l3+=l2[k:]
print(l3)

'''
#to check if second digit of number is even:
'''
n = int(input("enter a number: "))

while n>100:
    n//=10

second_digit = n%10
if second_digit%2==0:
    print('even')
else:
    print('odd')
'''

#toggle case of string:
'''
s = input('enter a string: ')
a = ''
for i in s:
    if i.isupper():
        a+=i.lower()
    else:
        a+=i.upper()
print(a)
'''


# s1 = input('enter first string: ')
# s2 = input('enter second strng: ')
# if len(s1) >= len(s2):
#     bigger = s1
#     smaller = s2
# else:
#     bigger = s2
#     smaller = s1
# for i in range(len(smaller)):
#     if smaller[i]!=bigger[i]:
#         if ord(bigger[i]) > ord(smaller[i]):
#             greaterstring = bigger
#             break
#         elif ord(smaller[i]) > ord(bigger[i]):
#             greaterstring = smaller
#             break
#     else:
#         greaterstring=bigger

#hw 1
'''
a = input('enter string: ')
d = {}
for i in a:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
'''
#hw 2
'''
a = input('enter string: ') + ' '
d = {}
words=[]
tmp=''
for i in a:
    if i==' ':
        words.append(tmp)
        tmp=''
    else:
        tmp += i

for i in words:
    if i in d and i!='':
        d[i]+=1
    else:
        d[i]=1
print(d)
'''

#dictionary storage program:
'''
d = {}

while True:
    print('1)Chnage values\n2)Add new value\n3)Delete value\n4)View dictionary\n5)view highest overall marks\n6)view highest mark in each subject\n7)exit')
    choice = input('>>')

    while choice not in ['1','2','3','4','5','6','7']:
        print('Invalid option.')
        choice = input('>>')

    if choice=='1':

        if d == {}:
            print('dictionary is empty')        
            continue
        else:
            # avg_marks_list = []
            print('select which value to change: ')
            for i in d:
                print(f'{i}) roll number {i} : name-{d[i][0]}, mark1-{d[i][1]}, mark2-{d[i][2]}, mark3-{d[i][3]}')
            
            # highest_avg= avg_marks_list.index(max(avg_marks_list))
            # print(f'Highest marks are of: roll number: {highest_avg} name-{d[highest_avg][0]}')


            n = int(input('>>'))
            print(d[n])

            print('select which value to be changed: ')
            print('1)name\n2)mark1\n3)mark2\n4)mark3')
            value_to_change = input('>>')

            if value_to_change=='1':
                print('enter new name: ')
                new_name = input('>>')
                d[n][0] = new_name
                print('name of student has been changed succesfully.')
            
            elif value_to_change=='2':
                print('enter new mark1: ')
                new_mark1 = int(input('>>'))
                d[n][1] = new_mark1
                print('mark1 of student has been changed succesfully.')
            
            elif value_to_change=='3':
                print('enter new mark2: ')
                new_mark2 = int(input('>>'))
                d[n][2] = new_mark2
                print('mark2 of student has been changed succesfully.')

            elif value_to_change=='4':
                print('enter new mark3: ')
                new_mark3 = int(input('>>'))
                d[n][3] = new_mark3
                print('mark3 of student has been changed succesfully.')  
        
    elif choice=='2':
        print('enter new roll number: ')
        _roll_no = int(input('>>'))
        if _roll_no in d:
            print('\nThis roll number already exits, are you sure you want to overrite existing values? (y/n)\n')
            aa = input('>>')
            if aa=='y':
                print('enter name: ')
                name = input('>>')
                marks = [int(input(f'enter new mark {i}: ')) for i in range(1,4)]
                marks.insert(0,name)
                d[_roll_no] = marks
                print(f'\nnew value added - roll number {_roll_no} : name-{d[_roll_no][0]}, mark1-{d[_roll_no][1]}, mark2-{d[_roll_no][2]}, mark3-{d[_roll_no][3]}\n')

            elif aa=='n':
                continue
        else:
            print('enter name: ')
            name = input('>>')
            marks = [int(input(f'enter new mark {i}: ')) for i in range(1,4)]
            marks.insert(0,name)
            d[_roll_no] = marks
            print(f'\nnew value added - roll number {_roll_no} : name-{d[_roll_no][0]}, mark1-{d[_roll_no][1]}, mark2-{d[_roll_no][2]}, mark3-{d[_roll_no][3]}\n')

    elif choice=='3':
        if d == {}:
            print('\ndictionary is empty\n')        
            continue
        else:
            print('select which value to delete: ')
            for i in d:
                print(f'{i}) roll number {i} : name-{d[i][0]}, mark1-{d[i][1]}, mark2-{d[i][2]}, mark3-{d[i][3]}')
        n = int(input('>>'))
        del d[n]
        print('value has been deleted.')

    elif choice=='4':
        if d == {}:
            print('dictionary is empty')
            continue
        else:
            print()
            for i in d:
                print(f'{i}) roll number {i} : name-{d[i][0]}, mark1-{d[i][1]}, mark2-{d[i][2]}, mark3-{d[i][3]}')
            print()
    
    elif choice=='5':
        if d == {}:
            print('dictionary is empty')
            continue
        else:
            avg_all = [d[i][1]+d[i][2]+d[i][3] for i in d.keys()]
            highest = avg_all.index(max(avg_all))

            print(f'\n{d[highest+1]}\n')

    # elif choice=='6':
    #     m1,m2,m3 = [d[i][1] for i in d.keys()], [d[i][3] for i in d.keys()], [d[i][3] for i in d.keys()]
    #     print(m1, m2, m3)

        
    #     print(f'highest mark1 = {d[n1][0]}:{max(m1)}')

    elif choice=='7':
        exit(0)
'''

#read list of strings then arrange in alphabetical order:
'''
n = int(input('enter number of strings in list: '))
ok = [input(f"enter {i+1} string: ") for i in range(n)]
for i in range(1,len(ok)):
    j=i
    while j>0 and ok[j]<ok[j-1]:
        ok[j],ok[j-1] = ok[j-1],ok[j]
        j-=1
print(ok)
'''

#print element which has highest number of factors

#input list of numbers: 
'''
a = [int(input(f"enter {i+1} element of list: ")) for i in range(int(input("enter number of elements in list: ")))]

#set 2 variables to 0
ans=0
ok=0

#traverse the list
for i in a:
    #factors of any number exist between 1 and half of that number, ex. all factors of 20 are less than or equal to 10
    factors = len([j for j in range(1,(i//2)+1) if i%j==0])
    #so, for each number in the range 1 to the half of the element+1, if the element is divisible, it is a factor.
    #put all these fators in a list and so, total number of factors is the length of the list

    #if current number of factors is more than previous, ans = current number of factors and ok = the element
    if factors>ans:
        ans = factors
        ok = i

if ok==1: print("all are prime numbers")
else: print(ok)
'''

#Merge 2 dictionaries, if same key in both, take value of 2nd dict.
'''
al = int(input("enter length of dictionary A: "))
bl = int(input("enter length of dictionary B: "))

a = {input(f'enter key {i+1} for dict A: '): input(f'enter value for key {i+1}: ') for i in range(al)}
b = {input(f'enter key {i+1} for dict B: '): input(f'enter value for key {i+1}: ') for i in range(bl)}

# a = {'a':1, 'b':2, 'c':3}
# b = {'a':90, 'e':99, 'c':800}

c = {}
for i in a:
    if i in b:
        c[i] = b[i]
    else:
        c[i] = a[i]

for i in b:
    if i not in c:
        c[i] = b[i]
print(c)
'''

#print pythagorean triplets
'''
t = ()

h=1
while len(t)<5:
    for i in range(h):
        for j in range(i):
            if h**2 == i**2 + j**2:
                t+=((h,i,j),)
    h+=1
print(t)
'''
#?
'''
names1 = ['Ajit', 'Binay', 'Chandan', 'Diwan']
names2 = names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum = 0
# print(type((names1, names2, names3)))
for ls in (names1, names2, names3):
    if ls[0] == 'Alice':
        sum += 1
    if ls[1] == 'Bob':
        sum += 10
print (sum)
'''

#input a dictionary and reverse its key value pairs and print
'''
a = {input(f'enter {i+1} key: ') : input(f'enter {i+1} value: ') for i in range(int(input('enter length of dict: ')))}
rev = {a[i]:i for i in a}

print(f'reversed dictionary: {rev}')
'''

#phone number program: 
'''
n = int(input('enter no. of friends: '))
d = {input(f'enter name of {i+1} friend: '): int(input(f'enter number of {i+1} friend: '))for i in range(n)}
print(d)
while True:
    print('1)View dictionary\n2)Add new friend\n3)Delete friend\n4)Modify phone number of existing friend')
    c = int(input('>>'))
    if c==1:
        print(d)
    elif c==2:
        f = input('enter name of friend: ')
        no = int(input('enter phone number: '))
        d[f]=no
        print('number added! ')
    elif c==3:
        j=0
        for i in d:
            print(f'{j+1}) {i}: {d[i]}')
        f = input('enter name of friend to be removed: ')
        del d[f]
        print('friend removed! ')
    elif c==4:
        j=0
        for i in d:
            print(f'{j+1}) {i}: {d[i]}')
        f = input('enter name of friend who\'s phone no. is to be changed: ')
        nn = int(input('enter new phone no.: '))
        d[f] = nn
        print('phone no. changed! ')
'''

#password generator: 
#upper case, lower case, special char, digits ===> 2 each
'''
import secrets, string
from itertools import permutations
import scrypt, pyaes

passw = ''

#number of uppercase
nuper = int(secrets.choice('123')) 
upper = ''.join(secrets.choice(string.ascii_uppercase) for i in range(nuper))

#number of lowercase
nlower = int(secrets.choice('123'))
lower = ''.join(secrets.choice(string.ascii_lowercase) for i in range(nlower))

#number of digits
nd = int(secrets.choice('123'))
digits =  ''.join(secrets.choice(string.digits) for i in range(nd))

#number of special
ns = int(secrets.choice('123'))
special = ''.join(secrets.choice('!@#$%^&*-=<>\/[]{}()') for i in range(ns))

passw = upper+lower+digits+special

#max len passw=12, min=4
if len(passw)<8:
    passw+=''.join(secrets.choice(string.printable) for i in range(8-len(passw)))
while len(passw)>8:
    n = int(secrets.choice(''.join(str(i) for i in range(len(passw)))))
    passw = passw[:n]+passw[n+1:]

#all perms
perms = [''.join(p) for p in permutations(passw)]
perms = random.sample(perms, len(perms))

#random perm
p = int(secrets.choice(''.join(str(i)for i in range(len(perms)))))

passw = perms[p]
print(f'password generated = {passw}')

#encrypt passw
asci = lambda x: ord(x)

encrypted=''

for i in passw:
    r = asci(i)
    if r in range(0,144000):
        r+=20

    encrypted+=chr(r)

print(f'encrypted = {encrypted}')
decrypted=''

for i in encrypted:
    d = asci(i)
    if d in range(20, 144005):
        d-=20

    decrypted+=chr(d)

print(decrypted)

'''

#list arranged in ascending  order, some elements repeated, replace element with sum of all occurences
'''
import secrets, string
s = ''.join(secrets.choice(string.digits) for i in range(10))
l = [int(i) for i in s] #generates random list(len=10) of ints

print(l)
oc={}

for i in l:
    if i not in oc:
        oc[i]=0
    oc[i]+=1
print(oc)

l2 = [i for i in oc]

for i in range(len(l2)):
    l2[i]=l2[i]*oc[l2[i]]
l = l2    
print(l)
'''

#given list of words, generate all possible combinations of words
'''
l = ['this', 'is', 'all', 'init']
def permutations(x : list)-> list:
    if len(x)==1: return [x]
    res=[]
    for i in range(len(x)):
        fixed = x[i]
        for p in permutations(x[:i]+x[i+1:]):
          res+=[[fixed]+p]
    return res

print(permutations(l))
'''

#check if palindrome
'''
n = int(input('enter length of list: '))
l = (input('enter string: ')for i in range(n))
for i in l:
    if i==i[::-1]: print(f'{i} is a palindrome')
'''

pn = []
# i=6
# while len(pn)<5:
#     sdiv = [j for j in range(1,int(i**0.5)+1) if i%j==0]
#     # print(sdiv)
#     if sum(sdiv)==i:
#         pn += [i]
#     # print(i)
#     i+=1

# print(pn)


#perfect numbers:

def c():
    n=6
    while True:
        yield n
        n+=1

# for i in c(): print(i)

def p():
    pn=[]
    for i in c():
        if sum([j for j in range(1,i//2+1) if i%j==0])==i:
            yield i
co=0
for i in p():
    if co<4:
        co+=1
        print(i)
        print(co)
    else:
        quit()


