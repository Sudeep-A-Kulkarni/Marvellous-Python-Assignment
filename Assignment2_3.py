import sys

def main():
    #print("enter a number")
    #n = int(input())
    n = int(sys.argv[1])
    factorial = 1
    for i in range(1,n+1):
        factorial = factorial *i

    print("factorial of the numbre is ",factorial)




if __name__ == "__main__":
    main()