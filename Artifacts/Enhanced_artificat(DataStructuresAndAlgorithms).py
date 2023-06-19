def merge_sort(arr):
 # Base case: If the array has 0 or 1 element, it is already sorted
    if len(arr) <= 1:  
        return arr
     # Find the middle index of the array
    mid = len(arr) // 2 
	# Split the array into two halves: left half from 0 to mid-1
    left_half = arr[:mid] 
    # right half from mid to the end	
    right_half = arr[mid:]  
    # Recursively sort the left half
    left_half = merge_sort(left_half)  
	# Recursively sort the right half
    right_half = merge_sort(right_half)  
    # Merge the sorted left and right halves
    return merge(left_half, right_half)  


def merge(left, right):
# Create an empty list to store the merged result
    merged = []  
	# Initialize pointers for left and right halves
    i = j = 0  
    
    # Compare elements from left and right halves and add them to the merged list in ascending order
    while i < len(left) and j < len(right):
	# Add it to the merged list
        if left[i] <= right[j]:  
		# If the element in the left half is smaller or equal
            merged.append(left[i])  
			 # Move the pointer of the left half to the next element
            i += 1 
			# If the element in the right half is smaller
        else:  
		 # Add it to the merged list
            merged.append(right[j]) 
			# Move the pointer of the right half to the next element
            j += 1  
    
    # Add any remaining elements from the left half to the merged list
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    # Add any remaining elements from the right half to the merged list
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged


# User input
input_str = input("Enter a list of integers (separated by spaces): ")
 # Convert the input string into a list of integers
arr = [int(x) for x in input_str.split()] 

# Sorting
# Sort the array using merge sort
sorted_arr = merge_sort(arr)  
# Print the sorted array
print("Sorted array:", sorted_arr)  
