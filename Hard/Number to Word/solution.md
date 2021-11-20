# Solution

## Understanding
Given number in a word form, the challenge is to convert it to its numerical form. So, I have to make dictionaries and some condition to translate the numbers.

## Try

### Accepting The Inputs
The letters in the word is randomized wether it is in lowercase or uppercase, so I turn it into all lowercase and split it into an array to make it flexible and easy for further use.
```python
word = input().lower().split(' ')
```
### Do the Logical
First, create a dictionaries of possible words.

**Natural Number**
```python
A = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
    'eight', 'nine']
```
I put the words in an array is because it can be called using its index.\
For example if I call `A[3]`, `'three'` will comes up as it is at the `3` index. So if I get the index of `'three'` from `A` it would give me `3`.
```python
A.index('three')
>>> 3
```

**-teen Number** (idk what it is called)
```python
B = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen']
```
Again I put the words in an array. So if I get the index of it and add `10` it would give me the right number.
```python
B.index('fourteen') + 10
>>> 14
```

Like the `A` and `B`, I put the **tens** (idk what it is called too) into an array.
```python
C = ['zero', 'ten', 'twenty', 'thirty', 'fourty', 'fifty',
    'sixty', 'seventy', 'eighty', 'ninety']
```
With that if I get the index of it and multiple it by `10`, I got the right number.
```python
B.index('eighty') * 10
>>> 80
```
**Hundred, Thousand, Million, Billion, Trillion**
```python
D = {'hundred': 2, 'thousand': 3, 'million': 6,
    'billion': 9, 'trillion': 12}
```
The reason I put it in dictionary, so It can be easily called by using the `key`, and if I power `10` to the `value` of it, I got the right number.
```python
10 ** D['billion']
>>> 1000000000         # nine 0s, no need to point your finger
```

With the dictionaries of possible words set, Now I process the given input array one by one using `while` loop, and remove the processed word from the array. So, the loop will end if there is no word left in the array.
```python
while word:

    #the logic goes here

    word.remove(word[0])
```

The possible word that appear first is either `A`, `B`, or `C`, not `D`. So I make the condition for it and make nested condition inside it to process the word based on which dictionary the word in.
```python
base = 0
temp = 0

while word:
    if not word[0] in D.keys():
        if word[0] in A:
            temp += A.index(x[0])
        elif word[0] in B:
            temp += 10 + B.index(x[0])
        elif word[0] in C:
            temp += 10 * C.index(x[0])

    else:
        temp *= (10**D[x[0]])

        if D[x[0]] > 2:
            base += temp
            temp = 0

    x.remove(x[0])

result = base + temp
```
I create 2 variables `base` and `temp` for the counter.
Here's how it works.
```python
# I printed everything

base = 0
temp = 0

while word:
    if not word[0] in D.keys():
        print(f'[*]{repr(x[0])} is not in D')
        if word[0] in A:
            print(f'[*]{repr(x[0])} is in A. +{A.index(x[0])} to temp')
            temp += A.index(x[0])
        elif word[0] in B:
            print(f'[*]{repr(x[0])} is in B. +{10 + B.index(x[0])} to temp')
            temp += 10 + B.index(x[0])
        elif word[0] in C:
            print(f'[*]{repr(x[0])} is in C. +{10 * C.index(x[0])} to temp')
            temp += 10 * C.index(x[0])

    else:
        print(f'[*]{repr(x[0])} is in D. multiply the temp by {(10**D[x[0]])}')
        temp *= (10**D[x[0]])

        if D[x[0]] > 2:
            print(f'[*]{repr(x[0])} is thousand or above. +temp to base')
            base += temp
            print(f'[*]reset the temp to 0')
            temp = 0
    print(f'[*]removed {repr(x[0])} from the array')
    x.remove(x[0])

    print('[*]Current:')
    print(f'\tbase: {res}')
    print(f'\ttemp: {base}')
    print(f'\tarray: {x}')
    print()

result = base + temp
print(result)
```
And this is the output
```
[*]'four' is not in D
[*]'four' is in A. +4 to temp
[*]removed 'four' from the array
[*]Current:
    base: 0
    temp: 4
    array: ['thousand', 'two', 'hundred', 'sixty', 'nine']

[*]'thousand' is in D. multiply the temp by 1000
[*]'thousand' is thousand or above. +temp to base
[*]reset the temp to 0
[*]removed 'thousand' from the array
[*]Current:
    base: 4000
    temp: 0
    array: ['two', 'hundred', 'sixty', 'nine']

[*]'two' is not in D
[*]'two' is in A. +2 to temp
[*]removed 'two' from the array
[*]Current:
    base: 4000
    temp: 2
    array: ['hundred', 'sixty', 'nine']

[*]'hundred' is in D. multiply the temp by 100
[*]removed 'hundred' from the array
[*]Current:
    base: 4000
    temp: 200
    array: ['sixty', 'nine']

[*]'sixty' is not in D
[*]'sixty' is in C. +60 to temp
[*]removed 'sixty' from the array
[*]Current:
    base: 4000
    temp: 260
    array: ['nine']

[*]'nine' is not in D
[*]'nine' is in A. +9 to temp
[*]removed 'nine' from the array
[*]Current:
    base: 4000
    temp: 269
    array: []

4269
```

### Done! :smile:

## Wrap Up
The final code will be like this:
```python
A = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
    'eight', 'nine']
B = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
    'sixteen', 'seventeen', 'eighteen', 'nineteen']
C = ['dummy1', 'dummy2', 'twenty', 'thirty', 'fourty', 'fifty',
    'sixty', 'seventy', 'eighty', 'ninety']
D = {'hundred': 2, 'thousand': 3, 'million': 6,
    'billion': 9, 'trillion': 12}

def word_to_number(x):
    res = 0
    base = 0

    while x:
        if not x[0] in D.keys():
            if x[0] in A:
                base += A.index(x[0])
            elif x[0] in B:
                base += 10 + B.index(x[0])
            elif x[0] in C:
                base += 10 * C.index(x[0])

        else:
            base *= (10**D[x[0]])

            if D[x[0]] > 2:
                res += base
                base = 0

        x.remove(x[0])

    return base + res


word = input().lower().split(' ')

print(word_to_number(word))
```

### Solved!
