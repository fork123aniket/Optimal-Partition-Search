# Optimal Partition Search 

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.6](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-395/)

## Overview and Functionality

- Official Implementation of the paper - "***Optimal Partition Search***" [(***IEEE Xplore***)](https://ieeexplore.ieee.org/document/8869459) [(***ResearchGate***)](https://www.researchgate.net/publication/336638736_Optimal_Partition_Search)
- Searches for the optimal number of partitions required to speed up the search process
- Works for arrays having any data type (int, float, char, long, etc.)
- Independent of the order of the elements in the array, i.e. can work for both sorted and unsorted array settings

## Usage

- Make sure you have ***Python version 3.9 or greater*** installed on your system
- Run the following command on the terminal to install this package:
 ```
  pip install Optimal-Partition-Search
  ```
- More details on how to install this package and other relevant information can be found [***here***](https://pypi.org/project/Optimal-Partition-Search/0.0.1/)

## Example

 ```
# test.py
 
from Optimal_Partition_Search import optimal_partition_search
import random
import numpy as np

# Example for array having integer values
array = random.sample(range(150), 100)
print(f'array: {array}')
element = int(input("Enter the item you want to search\n"))
optimal_partition = optimal_partition_search(array, element)
print("Optimal no. of partitions", optimal_partition)

# Example for array having float values
array = np.random.uniform(low=600.5, high=705.2, size=(10,))
print(f'array: {array}')
element = float(np.random.choice(array, 1))
optimal_partition = optimal_partition_search(array, element)
print("Optimal no. of partitions", optimal_partition)

# Example for array having character and string values
array = ['a', 'c', 'q', 'l', 'h', 's', 'tr', 'input']
print(f'array: {array}')
element = input("Enter the item you want to search\n")
optimal_partition = optimal_partition_search(array, element)
print("Optimal no. of partitions", optimal_partition)
  ```

Use the following command to run the examples given in the `test.py` file above: 
 ```
  python test.py
 ```
