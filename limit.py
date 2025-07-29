# import random
# a=[]
# n=int(input('Enter n : '))
# for i in range(n):
#     x=2*i/(i+1)
#     a.append(x)
# sum=0
# for i in a:
#     # print(i)
#     sum+=i
# print('Limit value : ',a[-1])

'''

traingular number:
n(n+1)/2
n=1
.
n=2
.
..
n=3
.
..
...



Enter how many dice u will want to toss at a time : 60
no of even number in dice :  12
P(Even) :  0.2
'''
n=int(input('Enter n : '))
y=0
for i in range(n+1):
    x=(10*i*i+3*i+100)/(2*i*i-5*i-100)
    y=x
print(y)
'''
Enter n : 1000
5.014351247948799
Enter n : 1000000
5.0000140003350015
'''

