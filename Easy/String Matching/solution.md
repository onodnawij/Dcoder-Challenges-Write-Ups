# Solution

## Understanding
Given string `N` and favorite string `F` separated by a space, I must make sure if `F` is in the `N` sequence or not. And the output must be `Yes` or `No`.
Almost forget, there is some test cases within case denoted as `T`.

## Try

### Accept the inputs:
Assign the `T` for the loop then split `N` and `F` inside it.
```python
for t in range(int(input())):
	N, F = input().split(' ')
```

### Do the Logical
In Python, we can check if some string is in the other string sequence like checking wether an element is in the array or not.\
It can be done simply like this
```python
some_string = 'borderless'

x = 'order' in some_string
```
If we printed the `x`, the output will be a [*boolean*](https://www.geeksforgeeks.org/boolean-data-type-in-python/#:~:text=Python%20boolean%20type%20is%20one,whereas%202%3C1%20is%20False.) like this.
```python
print(x)
>>> True
```

So, with that boolean data type, I put it in a condition to make my code returns 'Yes' if `F` is inside `N` sequence and 'No' if not.
```python
    result = 'Yes' if F in N else 'No'
    print(result)
```
Yep. You can make a condition in a single line like that in Python.\
That is equivalent to:
```python
    result = ''
    if F in N:
        result = 'Yes'
    else:
        result = 'No'
    print(result)
```

Submitted it, and it works ! :smile:

## Wrap Up
The final code will be like this:
```python
for t in range(int(input())):
    N, F = input().split(' ')
    result = 'Yes' if F in N else 'No'
    print(result)
```

### Solved!