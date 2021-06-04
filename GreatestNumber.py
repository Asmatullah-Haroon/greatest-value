# Take three values from user and find the greatest number from them?

a=int(input('Enter the first number:'))
b=int(input('Enter the second Number:'))
c=int(input('Ente the Third Number:'))
if a>b and a>c:
    print('the value of A is',a,'highest velue')
elif b>a and b>c:
    print('the value of B is',b,'highest velue')
elif c>a and c>b:
    print('the value of C is',c,'highest velue')
else:
   print('the value is equls')