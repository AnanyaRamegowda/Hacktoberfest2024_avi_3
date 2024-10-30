# Sample Dictionary
data = {'apple': [3, 7, 1], 'banana': [2, 5, 4], 'orange': [6, 9, 8]}

# Sorting based on the sum of the list values
sorted_data = dict(sorted(data.items(), key=lambda x: sum(x[1])))

# Displaying the sorted dictionary
print(&quot;Using Sorted and Lambda Function&quot;)
print(sorted_data)
