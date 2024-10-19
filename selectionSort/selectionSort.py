def find_smallest(arr, start_index):
  if start_index >= len(arr):
    return None, None

  # Stores the smallest value
  smallest = arr[start_index]
  # Stores the index of the smallest value
  index = start_index

  for i in range(start_index, len(arr)):
    if arr[i] < smallest:
      index = i
      smallest = arr[i]
  return smallest, index

def selection_sort(arr):
  for i in range(len(arr)):
  # Finds the smallest element and its index in the array from index i
    smallest, smallest_index = find_smallest(arr, i)
    if smallest and smallest_index:
      # Swap the smallest element with the element at index i
      arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
  return arr

print(selection_sort([5, 3, 6, 2, 10])) # [2, 3, 5, 6, 10]
print(selection_sort(["banana", "orange", "apple"]))  # ['apple', 'banana', 'orange']