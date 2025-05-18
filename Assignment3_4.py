def Repetition(no,Data):
    count = 0
    for i in Data:
        if i == no:
            count= count+1


    print("number of times the element repeated: ",count)
        
    



def main():
    print("enter the size :")
    size = int(input())

    Data=list()

    print("enter the list")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("the entered list is ")

    for j in Data:
        print(j)

    print("enter a number to find repetition")
    no=int(input())

    Repetition(no,Data)

if __name__ == "__main__":
    main()