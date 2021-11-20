# Solution

## Understanding
Symmetric Matrix is a matrix that has same shape and value with the transposed version of it.
Given `N` x `N` shape matrix, the challenge is to check if it is symmetric or not.

## Try

### Accepting The Inputs
Looking at the sample input, I must use a loop to build the matrix.
```python
matrix = [input().split(' ') for i in range(int(input()))]
```

If you dont understand the code above, you can take a look at this [Rotate Array Solution](https://github.com/onodnawij/Dcoder-Challenges-Write-Ups/blob/master/Easy/Rotate%20Array/solution.md#accept-the-inputs)

### Do the Logical
Luckily, [numpy](https://numpy.org/) is available in Dcoder. Then I'll use it for easier transposing.
First, convert the matrix to `numpy.array`
```python
import numpy as np

matrix = np.array(matrix)
print(matrix)
>>>[['1' '0' '0']
    ['0' '2' '1']
    ['0' '1' '1']]
```
To transpose it, it's pretty straightforward
```python
matrix.transpose()
>>>[['1' '0' '0']
    ['0' '2' '1']
    ['0' '1' '1']]
```
Finally, check the equality between the original and transposed matrix, and make condition for the output.
```python
symmetric = np.array_equal(matrix, matrix.transpose())
print('YES' if symmetric else 'NO')
```

### Done! :smile:

## Wrap Up
The final code will be like this:
```python
import numpy as np

matrix = [input().split(' ') for i in range(int(input()))]
matrix = np.array(matrix)
symmetric = np.array_equal(matrix, matrix.transpose())
print('YES' if symmetric else 'NO')
```

### Solved!