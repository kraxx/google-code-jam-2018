def troubleSort(num, l, arr):
    done = False
    while not done:
        done = True
        for x in range(l - 2):
            if arr[x] > arr[x + 2]:
                arr[x], arr[x + 2] = arr[x + 2], arr[x]
                done = False
    for x in range(l - 1):
        if arr[x] > arr[x + 1]:
            print("Case #" + str(num) + ": " + str(x))
            return
    print("Case #" + str(num) + ": OK")
    return
    
# Main
numTests = int(input())
for x in range(numTests):
    l, arr = int(input()), list(map(int, input().split(" ")))
    troubleSort(x, l, arr)