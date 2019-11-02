my_arr = [8,5,2,6,9,3,1,4,0,7]
def selection_sort(my_arr):
    for i in range(len(my_arr)): #loop for list, index = i
        min_idx = i #index minimum for full array
        for j in range(i+1, len(my_arr)): #loop starting after current iteration of index i, index is j
            if my_arr[min_idx] > my_arr[j]: #compares index minimum to index j
                min_idx = j #sets the index minimum to j, if j is smaller than the index minimum
        temp = my_arr[i] #storing current index for swap
        my_arr[i] = my_arr[min_idx] #swap index i with index minimum
        my_arr[min_idx] = temp #set the index value back to it's original state we stored
    return arr
print(selection_sort(my_arr))   
