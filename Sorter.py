def sorter(arr, n): 
      

    evenArr = [] 
    oddArr = [] 

    for i in range(n): 
        if ((i % 2) == 0): 
            evenArr.append(arr[i]) 
        else: 
            oddArr.append(arr[i]) 

    evenArr = sorted(evenArr) 
    oddArr = sorted(oddArr) 
    oddArr = oddArr[::-1] 
  
    i = 0
    for j in range(len(evenArr)): 
        arr[i] = evenArr[j] 
        i += 1
    for j in range(len(oddArr)): 
        arr[i] = oddArr[j] 
        i += 1

x = int(input("Enter a number")) 
    arr = []
    for y in range(0,x,1):
        arr.append(y)


n = len(arr) 
sorter(arr, n) 
for i in arr: 
    print(i, end = " ") 
  