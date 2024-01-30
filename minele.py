def fmin(array, l):
     
    min_element = array[0];
    # find minimum element
    for i in range(l) :
        if array[i] < min_element :
            min_element = array[i]
 
    return min_element;
 
# input
array = [5, 6, 1, 2, 3, 4]
l = len(array)

print(fmin(array,l))
