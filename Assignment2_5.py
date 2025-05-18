import sys

def ChkPrime(no):
    count = 0
    for i in range(1,no+1):
        if no%i == 0:
            count+=1
        else:
            pass

    if count ==2:
        print("number is a prime number ")
    else: 
        print ("number is not a prime number")


def main():
    #print("enter a number :")
    #no = int(input())
    no = int(sys.argv[1])
    ChkPrime(no)




if __name__ =="__main__":
    main()
