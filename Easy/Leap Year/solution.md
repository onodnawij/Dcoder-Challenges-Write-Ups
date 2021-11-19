# Solution

## Understanding
Reading the problem description, it looks like I must create and array with `N` elements and then slice them to many array that consist of 3 or above elements.\
**Actually it isn't like that**

## Try

### Do the Logical
Logically, I just need to divide `N` by 3, and ignore the remains.\
OK I'll explain it.\
The task is to form groups with 3 or above members from `N` total members.\
Let's use 8 for example. So the groups will be `4` + `4` because the groups cannot be less than 3 members.\
That means if we divide `8` by `3` the result is `2` 3-member-groups with `2` member-remains, right ? Then we add 1 remain to each group until there are no remain left.
```
[3, 3]       #2 remains
[3+1, 3+1]   #0 remains
[4, 4]

or

[3+2, 3]
[5, 3]        #still meet the condition (members >= 3)
```

I think thats enough explanation, because the solution is just a single line :smile:

In Python we can divide numbers and ignore the remains using `//` operator.\
So the code will be like this:
```python
print(int(input())//3)
```

Yep that's it. That's the solution.

## Wrap Up
The final code will be like this:
```python
print(int(input())//3)
```

### Solved!