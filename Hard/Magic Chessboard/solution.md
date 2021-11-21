# Solution

## Understanding
Back in school, to count possible square in a chessboard can be done by sum up the `square` of the numbers 1 to the number of the chessboard size.\
So, If the size is `8` then the possible square in it is `1^2 + 2^2 + 3^2 ... + 8^2`.

## Try

### Accept the inputs:
Looping the test cases:
```python
for t in range(int(input())):
	size = int(input())
```

### Do the Logical
Create a function to count the possible square
```python
def count_square(x):									# x as the size of chessboard
	arr = [i**2 for i in range(1, x+1)] # create an array of range 1 to chess size and square them.
	return sum(arr)										# return summed array
```

### Done!

## Wrap Up
The code will be like this:
```python
def count_square(x):
	arr = [i**2 for i in range(1, x+1)]
	return sum(arr)

for t in range(int(input())):
	size = int(input())

	print(count_square(size))
```

### Solved!