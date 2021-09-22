#number of digits: 
'''
n=input('enter a number: ')
print(f'number of digits are: {len(n)}')
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
n=int(input('enter a number: '))
rn=0
while n>0:
    r=n%10
    n//=10
    rn = rn*10 + r
print(f'smallest digit is {str(rn)[-1]}')
'''

#smallest digit:
'''
n=int(input('enter a number: '))
rn=0
while n>0:
    r=n%10
    n//=10
    rn = rn*10 + r
print(f'smallest digit is {str(rn)[0]}')
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
a=0
for i in range(len(n)):
    if n[i] == n[-1-i]:
       a=1
    else:
        a=0
        break
if a==1:
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
