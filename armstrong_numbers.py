'''
#armstrong number or not?
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

'''
#armstrong numbers in a range: 

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
