#number of digits: 
'''
n=int(input('enter a number: '))
print(f'number of digits are: {len(str(n))}')
'''

#sum of digits:
'''
n=input('enter a number: ')
a=0
for i in range(len(n)):
    a+=int(n[i])
print(f'sum of digits is : {a}')
'''

#largest digit:
'''
n=input('enter a number: ')
a=0
while n>0:
    r=n%10
    n//=10
    if r>a:
        a=r
print(a)
'''

#smallest digit:
'''
n=input('enter a number: ')
a=9
while n>0:
    r=n%10
    n//=10
    if r<a:
        a=r
print(a)
''' 

#sum of even digts and product of odd digits: 
'''
n=input('enter a number: ')
ev,od=0,1
for i in range(len(n)):    
    if int(n[i])%2==0:
        ev+=int(n[i])
    else:
        od*=int(n[i])
print(f'sum of even = {ev}, product of odd = {od}')
'''

#if number is palindrome or not
'''
n=input('enter a nummber: ')
a=n
rn=0
while n>0:
    r=n%10
    n//=10
    rn=r+rn*10
if a==rn:
    print('yes')
else:
    print('no')
'''

#HCF and LCM
'''
a,b=int(input('enter a nummber: ')), int(input('enter a nummber: '))
if a<b:
    j=1
    while (b*j)%a!=0:
        j+=1
    hcf = (a*b)//(a*j)
    print(f'HCF is {hcf}')
    print(f'LCM is {b*j}')

else:
    j=1
    while (a*j)%b!=0:
        j+=1
    hcf = (a*b)//(a*j)
    print(f'HCF is {hcf}')
    print(f'LCM is {a*j}')
'''

#LCM of 3 numbers
'''
nums = [int(input(f"enter {i} number: ")) for i in range(1,4)]
nums=sorted(nums)
# print(nums)
j=1
while (nums[1]*j)%nums[0]!=0:
    j+=1
lcm_smallest_two = nums[1]*j
k=1
if nums[2] < lcm_smallest_two:
    while (lcm_smallest_two*k)%nums[2]!=0:
        k+=1
    print(f'LCM of the 3 numbers is {lcm_smallest_two*k}')
else:
    while (nums[2]*k)%lcm_smallest_two!=0:
        k+=1
    print(f'LCM of the 3 numbers is {nums[2]*k}')
'''

#prime numbers in a range
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

#marks for students and class
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

#implement replace:
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

#number of occurences of each element in a list:
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

#smallest and largest elements in a list wihtout function:
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
'''

#same thing but with lists:
'''
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

