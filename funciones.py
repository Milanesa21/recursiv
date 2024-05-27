def quicksort(arr):
    # Si el array es menor o igual a 1, retornamos el array
    if len(arr) <= 1:
        return arr
    else:
        # Definimos el pivote
        pivote = arr[1]
        # definimos el array menor y el array mayor
        menor= [x for x in arr[0:] if x < pivote]
        mayor= [x for x in arr[0:] if x > pivote]
        # Retornamos la concatenación de los arrays menores, el pivote y los arrays mayores
        return(quicksort(menor)+([pivote])+ quicksort(mayor))

# Imprimimos el resultado de la función quicksort con los parametros que le pasamos
print(quicksort([10, 5, 2, 3,11 ,1 , 69, 4,]))