from Optimal_Partition_Search import optimal_partition_search
import random
import numpy as np

array = random.sample(range(150), 100)
print(f'array: {array}')
element = int(input("Enter the item you want to search\n"))
optimal_partition = optimal_partition_search(array, element)
print("Optimal no. of partitions", optimal_partition)

array = np.random.uniform(low=600.5, high=705.2, size=(10,))
print(f'array: {array}')
element = float(np.random.choice(array, 1))
optimal_partition = optimal_partition_search(array, element)
print("Optimal no. of partitions", optimal_partition)

array = ['a', 'c', 'q', 'l', 'h', 's', 'tr', 'input']
print(f'array: {array}')
element = input("Enter the item you want to search\n")
optimal_partition = optimal_partition_search(array, element)
print("Optimal no. of partitions", optimal_partition)