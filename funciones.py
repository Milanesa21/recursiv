def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[1]
        menor= [x for x in arr[0:] if x < pivote]
        mayor= [x for x in arr[0:] if x > pivote]
        return(quicksort(menor)+([pivote])+ quicksort(mayor))


print(quicksort([10, 5, 2, 3,11 ,1 , 69, 4,]))