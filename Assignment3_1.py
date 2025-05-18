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



if __name__=="__main__":
    main()