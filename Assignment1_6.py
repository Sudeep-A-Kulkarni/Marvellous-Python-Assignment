def PNZ(num):
    if num<0:
        print('Negative Number ')
    elif num>0:
        print('Positive Number')
    else:
        print('zero')    

print('enter a number: ')
num=int(input())
PNZ(num)