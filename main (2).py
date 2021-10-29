num=int(input('Please Enter Number With 4 Digits:'))
result=0
if num>=1000 and num<10000:
    while num>0:
       digit=num%10
       result+=digit
       num=num//10
print(result)
num1=int(input("enter Digit You want To Inverse:"))
single=num1%10
thus=single*1000
hund=(num1//10)#%10*100
ten=hund//10#%10*10
thousand=ten//10#*1
inverse=thus+hund%10*100+ten%10*10+thousand
print('Inverse: ',inverse)
z=int(input('Enter A Number To Check If Palindrom:'))
if (z//1000 ==z%10) and ((z//100%10)==z//10%10):
    print("The Number Is Palindrom")
else:
    print('Not Palindrom')