a=int(input('Enter a number: '))
if (a>1):
    for i in range(2,a):
     if a%i == 0:       
       print(f'{a} is not a Prime number ') 
       break
    else:
        print(f'{a} is a Prime number') 
        
else:
    print(f'{a} is less than 1 ')

 