a=int(input('enter a number:'))
sum=0
b=a
while a>=1:
    rem=a%10
    sum=sum+rem
    a=a//10
if b%sum==0:
    print('is harshad number')
else:
    print('not harshad number')  












         