a=float(input('Enter any positive number: '))
print(a)
a_bas=-a
a_haut=a
if (a>0):
    while (a_haut-a_bas)>0.001:
        if (((a_haut+a_bas)/2)*((a_haut+a_bas)/2)>a):
            a_haut=(a_haut+a_bas)/2
        else:
            a_bas=(a_haut+a_bas)/2
    print(str(a_bas) + ' et ' + str(a_haut))
    a=((a_haut+a_bas)/2)*((a_haut+a_bas)/2)
    print(a)
else:
    print('It doesn\'t works with negative numbers' )    