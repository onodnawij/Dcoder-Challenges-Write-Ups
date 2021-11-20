# Solution

## Understanding
I got a circle of `N` numbers that consists of `0` to the `N-1`. The challenge is to find the partner of `X` number which is standing radially opposite to it in the circle. With this description, I assume that the input will always an even number because every `X` number have it's own partner.

## Try

### Accepting The Inputs
The input is a single line string of `N` and `X` separated with space.\
So I splitted and converted them to integers.
```python
N, X = [int(x) for x in input().split(' ')]
```

### Do the Logical
Radially opposite.
For example look at the analog clock. The radially opposite of 1 is 7.
So, position 1 in clock is radially opposite to position 7.
That means:
```
rad_opposite = x + (length / 2)			# lenght is the length of the circle
					 7 = 1 + (12 / 2)					# length of analog clock is 12
```
So my code goes like this:
```python
_X = X + N//2			# find the position of the partner
```
Next, I create condition if `_X` is bigger than `N-1` then subtract it with the `N` to make it circle way just like analog clock. Then printed it.
```python
if _X > N-1:
	_X -= N

print(_X)
```

### It Works!

## Wrap Up
The final code will be like this:
```python
N, X = [int(x) for x in input().split(' ')]
_X = X + N//2

if _X > N-1:
	_X -= N

print(_X)
```

### Solved!