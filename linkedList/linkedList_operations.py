from linkedList import LinkedList

new_list = LinkedList()
node_data = [76, 34, 52, 96]

for data in node_data:
  new_list.insert_at_head(data)
  new_list.print_list()

# Test search function
print("Search for 34")
node = new_list.search(34)

if node:
  print(node.data)
else:
  print(node)

print("Search for -1")
node = new_list.search(-1)
if node:
  print(node.data)
else:
  print(node)

# Test delete function
# 1. Delete the head
# new_list.delete(96)
# print("List after deleting the head: ")
# new_list.print_list()

# Undo delete
# new_list.insert_at_head(96)

# 2. Delete a node 34
new_list.delete(34)
print("List after deleting node 34")
new_list.print_list()

new_list.selection_sort()
print("Sorted list")
new_list.print_list()