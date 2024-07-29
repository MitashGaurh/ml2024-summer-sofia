
def main():
    N = input("Enter a positive number N: ")
    N = int(N)
    
    if N <= 0:
        print("N must be positive.")
        return
    
    numbers = []
    
    i = 0
    while i < N:
        number = input("Enter number " + str(i + 1) + ": ")
        number = int(number)
        numbers.append(number)
        i = i + 1
    
    X = input("Enter number X: ")
    X = int(X)
    
    found = False
    i = 0
    while i < N:
        if numbers[i] == X:
            print("Index of " + str(X) + " is " + str(i + 1))
            found = True
            break
        i = i + 1
    
    if not found:
        print("-1")

if __name__ == "__main__":
    main()
