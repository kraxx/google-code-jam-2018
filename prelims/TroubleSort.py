def tomSort(num, l, arr):
    odds = sorted(arr[0::2])
    evens = sorted(arr[1::2])
    lenOdds = len(odds)
    for x in range(lenOdds - 1):
        if odds[x] > evens[x]:
            print("Case #" + str(num) + ": " + str(x * 2))
            return
        elif evens[x] > odds[x + 1]:
            print("Case #" + str(num) + ": " + str((x * 2) + 1))
            return
    if l % 2 == 0:
        if odds[lenOdds - 1] > evens[lenOdds - 1]:
            print("Case #" + str(num) + ": " + str(l - 1))
            return
    print("Case #" + str(num) + ": OK")
    return
    
# Main
numTests = int(input())
for x in range(numTests):
    l, arr = int(input()), list(map(int, input().split(" ")))
    tomSort(x, l, arr)


"""
Old bruteforce baloney

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
"""