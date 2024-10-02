n, k = map(int, input().split())
arr = input().split()

for i in range(0, len(arr)):
    arr[i] = int(arr[i])

arr.sort()

for i in range(0, k):
    maxnumber = max(arr)
    arr.remove(maxnumber)

print(maxnumber)


