def SmallestNumber(Data):
    smallest = Data[0]
    for no in Data:
        if smallest > no:
            smallest = no
    print("the smallest number is: ",smallest)



def main():
    print("enter the size of list :")
    size = int(input()) 

    Data=list()

    print("enter the list ")

    for i in range(size):
        no = int(input())
        Data.append(no)


    print("the entered list is")

    for j in Data:
        print(j)

    SmallestNumber(Data)

        
if __name__ == "__main__":
    main()