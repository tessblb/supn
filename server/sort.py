def bubbleSort(nums):
    for i in range(0, len(nums) - 1):  
        for j in range(len(nums) - 1):  
            if(nums[j] > nums[j + 1]):  
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums  

def quickSort(array):
    if len(array) < 2:
          return array
    else:
          pivot = array[0]
          less = [i for i in array[1:] if i <= pivot]

          greater = [i for i in array[1:] if i > pivot]

          return quickSort(less) + [pivot] + quickSort(greater)

def mergeSort(x):
    result = []
    if len(x) < 2:
        return x
    mid = int(len(x)/2)
    y = mergeSort(x[:mid])
    z = mergeSort(x[mid:])
    while (len(y) > 0) or (len(z) > 0):
        if len(y) > 0 and len(z) > 0:
            if y[0] > z[0]:
                result.append(z[0])
                z.pop(0)
            else:
                result.append(y[0])
                y.pop(0)
        elif len(z) > 0:
            for i in z:
                result.append(i)
                z.pop(0)
        else:
            for i in y:
                result.append(i)
                y.pop(0)
    return result
