def LargestNumber(Data):
    largest = Data[0]
    for i in  Data:
        if i > largest:
            largest = i
    print("The largest number is:", largest)

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

    LargestNumber(Data)


if __name__ == "__main__":
    main()

   