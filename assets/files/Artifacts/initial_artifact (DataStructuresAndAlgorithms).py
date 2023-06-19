def merge_sort(arr):
    if len(arr) <= 1:  # Base case: If the array has 0 or 1 element, it is already sorted
        return arr
    
    mid = len(arr) // 2  # Find the middle index of the array
    left_half = arr[:mid]  # Split the array into two halves: left half from 0 to mid-1
    right_half = arr[mid:]  # right half from mid to the end
    
    left_half = merge_sort(left_half)  # Recursively sort the left half
    right_half = merge_sort(right_half)  # Recursively sort the right half
    
    return merge(left_half, right_half)  # Merge the sorted left and right halves


def merge(left, right):
    merged = []  # Create an empty list to store the merged result
    i = j = 0  # Initialize pointers for left and right halves
    
    # Compare elements from left and right halves and add them to the merged list in ascending order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # If the element in the left half is smaller or equal
            merged.append(left[i])  # Add it to the merged list
            i += 1  # Move the pointer of the left half to the next element
        else:  # If the element in the right half is smaller
            merged.append(right[j])  # Add it to the merged list
            j += 1  # Move the pointer of the right half to the next element
    
    # Add any remaining elements from the left half to the merged list
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Add any remaining elements from the right half to the merged list
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged


# Example usage
arr = [9, 5, 1, 3, 8, 4, 2, 7, 6]
sorted_arr = merge_sort(arr)  # Sort the array using merge sort
print(sorted_arr)  # Print the sorted array
