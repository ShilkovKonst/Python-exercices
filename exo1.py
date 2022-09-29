a=int(input('Enter any int number lesser than 4000: '))
if (0<a<40000):
    b=int(input('Enter another int number lesser than 4000: '))
    if (0<b<40000):
        c=int(input('Enter another int number lesser than 4000: '))
        if (0<b<40000):
            print((a+b+c)/3)
        else: 
            print('wrong number!!!!')
    else: 
        print('wrong number!!!!')
else: 
    print('wrong number!!!!')