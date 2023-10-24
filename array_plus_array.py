def array_plus_array(arr1,arr2):
    soma = 0
    for i in range(len(arr2)):
        #print(f"array_1: {arr1[i]} | array_2: {arr2[i]}")
        soma += arr1[i] + arr2[i]
    return soma

soma = array_plus_array([1, 2, 3], [4, 5, 6])
print(f"{soma}")