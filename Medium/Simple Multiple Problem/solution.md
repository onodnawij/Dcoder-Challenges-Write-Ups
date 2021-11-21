# Solution

## Understanding
Every test case have `T` sub cases.
In each sub case, I have 2 numbers `N` and `M`, the challenge is to find the smallest number that when multiplied by `N` the result is multiple of `M`.

## Try

### Accept the inputs:
Loop the sub cases and get `N` and `M` inside it:
```python
for T in range(int(input())):
	N, M = [int(x) for x in input().split(' ')]
```
With that code, I get, the `N` and `M` and convert them to integer.

### Do the Logical
For example if `N` and `M` is `4` and `7`. The result is `7`.\
**why ?**\
Imagine that `N` and `M` is a fraction `N` / `M`. So in example case, it is `4` / `7`.\
The key is, make the fraction to its [simplest form](https://www.ixl.com/math/lessons/simplest-form#:~:text=What%20is%20simplest%20form%3F,form%20called%20%22lowest%20terms%22.), and then the answer is `M` which is `7`.\
So simplify the fraction until the common factor is no other than 1.

First, get the GCD (Greatest Common Divisor):
```python
	n, m = N 					# make a copy, so the original N and M stay there
	while m:
	    n, m = m, n % m
	gcd = n
```
Then, divide `N` and `M` with the `gcd`:
```python
	N, M = N//gcd, M//gcd		# // means integer division, so the result will remain integer not float
```
**Done!**
The answer is `M`
```python
	print(M)
```
## Wrap Up
The code will be like this:
```python
def simplify_fraction(numer, denom):
    def gcd(n, d)
        while d:
            n, d = d, n % d

        return n

    if denom == 0:
        return False

    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)

    return reduced_num, reduced_den

for T in range(int(input())):
	N, M = [int(x) for x in input().split(' ')]
	N, M = simplify_fraction(N, M)
	print(M)
```

### Solved!