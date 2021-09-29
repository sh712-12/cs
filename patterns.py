'''
#   1           [1,2)
#   2 3         [2,4)
#   4 5 6       [4,7)

n=int(input('enter a number: '))
t=1
for i in range(1, n):
  for j in range(1, i+1):
    print(t, end=' ')
    t+=1
  print()
'''

'''
#    1
#  2   2
#3   3  3

n=int(input('enter a number: '))
for i in range(1,n):
  print(' '*(n-i), end=' ')
  for j in range(1, i+1):
    print(i, end=' ')
  print()
'''

'''
#   A
#  B B
# C C C

l = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n=int(input('enter a number: '))
print(l)
for i in range(0, n):
  print(' '*(n-i), end=' ')
  for j in range(0, i+1):
    print(l[i], end=' ')
  print()
'''

'''
n=int(input('enter a number: '))
for i in range(1,n):
  print(' '*(n-i), end=' ')
  for j in range(1, i+1):
    print(i, end=' ')
  print()

for k in range(n-2,0,-1):
  print(' '*(n-k), end=' ')
  for l in range(k+1,1,-1):
    print(k, end=' ')
  print()
'''
