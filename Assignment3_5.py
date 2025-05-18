
def ChkPrime(Data,no):
    count = 0
    sum = 0
    for i in Data:
        for j in range(1,no):
            if no%j == 0:
                count = count + 1
            if count == 2:
                sum = sum+ no



def main():
    print("enter the size: ")
    size = int(input())

    Data = list()

    print('enter list')
    for i in range(size):
        no = int(input())
        Data.append(no)

    print("the entered list is")
    for value in Data:
        print(value)

    ChkPrime(Data,no)
   



if __name__=="__main__":
    main()