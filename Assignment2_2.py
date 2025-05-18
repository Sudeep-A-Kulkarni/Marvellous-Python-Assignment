import sys

def main():
    #print("enter a number")
    #n = int(input())
    n = int(sys.argv[1])
    for i in range(1,n+1):
        
        print(n*("*\t"))

if __name__=="__main__":
    main()