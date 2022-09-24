from random import randint


def bucket_sort(input_list):
    max_value = max(input_list)
    size = max_value/len(input_list)

    buckets_list = []
    for x in range(len(input_list)):
        buckets_list.append([]) 

    for i in range(len(input_list)):
        j = int (input_list[i] / size)
        if j != len (input_list):
            buckets_list[j].append(input_list[i])
        else:
            buckets_list[len(input_list) - 1].append(input_list[i])

    for z in range(len(input_list)):
        insertion_sort(buckets_list[z])
            
    final_output = []
    for x in range(len (input_list)):
        final_output = final_output + buckets_list[x]
    return final_output

def insertion_sort(bucket):
    for i in range (1, len (bucket)):
        var = bucket[i]
        j = i - 1
        while (j >= 0 and var < bucket[j]):
            bucket[j + 1] = bucket[j]
            j = j - 1
        bucket[j + 1] = var

def quickSort(array):
    if len(array) <= 1:
        return array

    element = array[0]
    left = list(filter(lambda x: x < element, array))
    center = [i for i in array if i == element]
    right = list(filter(lambda x: x > element, array))

    return quickSort(left) + center + quickSort(right)

array = []
for i in range(10000):
    array.append(randint(0, 100))
print("Original array\n", array)
print("\nBucket sort\n", bucket_sort(array))
print("\nQuick Sort\n", quickSort(array), "\n")