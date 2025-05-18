import sys
def main():
    sum = 0
    n = int(sys.argv[1])
    for i in range(1,n):
        if n % i == 0:
            sum += i
        else :
            pass
    print("the sum of factors is ",sum)
if __name__ == "__main__":
    main()