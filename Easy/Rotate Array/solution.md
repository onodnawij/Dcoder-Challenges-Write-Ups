# Solution

## Understanding
I have an *Array* (or *List* in Python) with `N` length. The challenge is to rotate that array `K` times to the right. \
So, every element on the array move `K` times to the right, and for the last element in the array we move to the front.

## Try

### Accept the inputs:
```python
N, K = [int(x) for x in input().split(' ')]
array = [x for x in input().split(' ')]
```

If you dont understand above code, that is equivalent to code below but the simple way.
```python
array = []

for x in input().split(' '): # the input recieved will only be a single string, so I must split that.
	array.append(x)
```
*refference: [Loop Inside List](https://stackoverflow.com/questions/11479392/what-does-a-for-loop-within-a-list-do-in-python)*

### Do the Logical
So, the logic is, rotating the array to the right is just **separate the last element, then put it on the front of the array**.\
In Python, to call the last element of an array is as simple as `array[-1]`. `-1` means the **first index from the last** of an array. Which means if you put `-2` that means the **second index from the last**.\
And, to call element from index `i` to index `j`, can be done simply by putting `:`.   `array[i:j]`. That will call all elements from index `i` to index `j` **BUT** excluding the element on index `j`. Why ? Please, just deal with it *or google it yourself* :smile:

Rotate the array:
```python
for i in range(K):
	last = array[-1]
	array = [last] + array[:-1]		#notice the bracket outside last. If you add between two arrays, it will make it a joined single array.

print(' '.join(array))					#the output must be in the same format as the sample output.
```

## Wrap Up
The code will be like this:
```python
N, K = [int(x) for x in input().split(' ')]
array = [x for x in input().split(' ')]

for i in range(K):
	last = array[-1]
	array = [last] + array[:-1]

print(' '.join(array))
```

### Solved!