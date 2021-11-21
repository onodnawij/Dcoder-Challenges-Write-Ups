# Solution

## Understanding
This is just reverse version of [this challenge](https://github.com/onodnawij/Dcoder-Challenges-Write-Ups/blob/master/Hard/Number%20to%20Word/)

## Try

### Accept the inputs:
```python
num = input()
```

### Do the Logical
I will use my dictionary in [this](https://github.com/onodnawij/Dcoder-Challenges-Write-Ups/blob/master/Hard/Number%20to%20Word/solution.md#do-the-logical)

For explaination about the my code, I print everything what my code does.\
Please take a look at the output of this code:
```python
A = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
	'eight', 'nine']
B = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
	'sixteen', 'seventeen', 'eighteen', 'nineteen']
C = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
	'sixty', 'seventy', 'eighty', 'ninety']
D = {'hundred': 2, 'thousand': 3, 'million': 6,
	'billion': 9, 'trillion': 12, 'quadrallion': 15,
	'quintallion': 18}

def number_to_word(x):
	if len(x) == 1:
		print(f'[*]got 1 digit. Return {x} => {A[int(x)]}')
		return A[int(x)]

	print(f'[*]Got {len(x)} digits. Detecting number levels.')
	levels = []
	while len(x) > 3:
		levels.append(x[-3:])
		x = x[:-3]
	levels.append(x)
	print(f'[*]The number levels is:')
	print(f'   {levels[::-1]}')
	print(f'[*]Processing it from the lowest level. So flipping it')
	print(f'   {levels}')
	thousands = [t for t in D.keys()]
   
	res = []
	print()
	print('[*]Processing the levels')
	for i in range(len(levels)):
		is_teens = False

		print(f'\t[*]{levels[i]} is {len(levels[i])} digits. add it to digits array.')
		if len(levels[i]) != 1:
			digits = [int(digit) for digit in levels[i]]
			if digits[-2] == 1:
				print(f'\t   {digits[-2]}{digits[-1]} detected as -teens number. set is_teens as True')
				is_teens = True
		else:
			digits = [int(levels[i])]
		print(f'\t[*]digits: {digits}')
		
		print(f'\t[*]Flip the digits for Processing it from the lowest level')
		digits = digits[::-1]
		print(f'\t[*]digits: {digits}')
		word = []

		print('\t[*]Collecting words from digits')
		print(f'\t\tis_teens is {is_teens}')
		for j in range(len(digits)):
			if j == 0:
				if is_teens:
					print(f'\t\t[*]{digits[j]} is {B[digits[j]]}')
					print(f'\t\t   add {B[digits[j]]} to collection')
					word.append(f'{B[digits[j]]}')
				elif digits[j]:
					print(f'\t\t[*]{digits[j]} is {A[digits[j]]}')
					print(f'\t\t   add {A[digits[j]]} to collection')
					word.append(f'{A[digits[j]]}')
				else:
					print(f'\t\t[*]{digits[j]} is zero')
					print(f'\t\t   Ignoring it.')
					pass
			elif j == 1:
				if digits[j] and not is_teens:
					print(f'\t\t[*]{digits[j]} is {C[digits[j]]}')
					print(f'\t\t   add {C[digits[j]]} to collection')
					word.append(f'{C[digits[j]]}')
				else:
					print(f'\t\t[*]{digits[j]} is zero')
					print(f'\t\t   Ignoring it.')
					pass
			else:
				if digits[j]:
					print(f'\t\t[*]{digits[j]} is {A[digits[j]]} with {thousands[0]} level.')
					print(f'\t\t   add {A[digits[j]]} {thousands[0]} to collection')
					word.append(f'{A[digits[j]]} {thousands[0]}')
				else:
					print(f'\t\t[*]{digits[j]} is zero')
					print(f'\t\t   Ignoring it.')
					pass

		print(f'\t[*]Words collected.')
		print(f'\t   {word}')
		print(f'\t[*]Flip it and append to results array.')
		print(f'\t   {word[::-1]}')
		res.append(' '.join(word[::-1]))
		try:
			if i != len(levels) -1:
				print('\t[*]Trying to add large number level to results')
				res.append(thousands[i+1])
				print(f'\t[*]The level is {thousands[i+1]}. Add it to results')
		except Exception as e:
			print(f'\t[!]Error. The level after {thousands[i]} is not in dictionary')
		print(f'\t[*]Current results is:')
		print(f'\t   {res}')
		print()

	print(f'[*]Done processing levels.')
	print(f'[*]Flip the results')
	res = res[::-1]
	while '' in res:
		print(f'[!]Detected blank word and unecessary thousands word')
		print(f'   {res[problem:problem+2]}')
		print(f'[!]Removing it.')
		problem = res.index('')
		res = res[:problem] + res[problem+2:]
	print(f'[*]Done!!')
	print(f'[*]Result is:')
	print(f'   {res}')
	print(f'[*]Join the results with space separator and returning it.')
	print()
	return ' '.join(res)

a = '123003114'
print(number_to_word(a))
```
The output:
```
[*]Got 9 digits. Detecting number levels.
[*]The number levels is:
   ['123', '003', '114']
[*]Processing it from the lowest level. So flipping it
   ['114', '003', '123']

[*]Processing the levels
	[*]114 is 3 digits. add it to digits array.
	   14 detected as -teens number. set is_teens as True
	[*]digits: [1, 1, 4]
	[*]Flip the digits for Processing it from the lowest level
	[*]digits: [4, 1, 1]
	[*]Collecting words from digits
		is_teens is True
		[*]4 is fourteen
		   add fourteen to collection
		[*]1 is zero
		   Ignoring it.
		[*]1 is one with hundred level.
		   add one hundred to collection
	[*]Words collected.
	   ['fourteen', 'one hundred']
	[*]Flip it and append to results array.
	   ['one hundred', 'fourteen']
	[*]Trying to add large number level to results
	[*]The level is thousand. Add it to results
	[*]Current results is:
	   ['one hundred fourteen', 'thousand']

	[*]003 is 3 digits. add it to digits array.
	[*]digits: [0, 0, 3]
	[*]Flip the digits for Processing it from the lowest level
	[*]digits: [3, 0, 0]
	[*]Collecting words from digits
		is_teens is False
		[*]3 is three
		   add three to collection
		[*]0 is zero
		   Ignoring it.
		[*]0 is zero
		   Ignoring it.
	[*]Words collected.
	   ['three']
	[*]Flip it and append to results array.
	   ['three']
	[*]Trying to add large number level to results
	[*]The level is million. Add it to results
	[*]Current results is:
	   ['one hundred fourteen', 'thousand', 'three', 'million']

	[*]123 is 3 digits. add it to digits array.
	[*]digits: [1, 2, 3]
	[*]Flip the digits for Processing it from the lowest level
	[*]digits: [3, 2, 1]
	[*]Collecting words from digits
		is_teens is False
		[*]3 is three
		   add three to collection
		[*]2 is twenty
		   add twenty to collection
		[*]1 is one with hundred level.
		   add one hundred to collection
	[*]Words collected.
	   ['three', 'twenty', 'one hundred']
	[*]Flip it and append to results array.
	   ['one hundred', 'twenty', 'three']
	[*]Current results is:
	   ['one hundred fourteen', 'thousand', 'three', 'million', 'one hundred twenty three']

[*]Done processing levels.
[*]Flip the results
[*]Done!!
[*]Result is:
   ['one hundred twenty three', 'million', 'three', 'thousand', 'one hundred fourteen']
[*]Join the results with space separator and returning it.

one hundred twenty three million three thousand one hundred fourteen

```

### Done!
Hope you understand what my code does :smile:

## Wrap Up
The code will be like this:
```python
A = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
	'eight', 'nine']
B = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
	'sixteen', 'seventeen', 'eighteen', 'nineteen']
C = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
	'sixty', 'seventy', 'eighty', 'ninety']
D = {'hundred': 2, 'thousand': 3, 'million': 6,
	'billion': 9, 'trillion': 12, 'quadrallion': 15,
	'quintallion': 18}

def number_to_word(x):
	if len(x) == 1:
		return A[int(x)]

	levels = []
	
	while len(x) > 3:
		levels.append(x[-3:])
		x = x[:-3]
	levels.append(x)

	thousands = [t for t in D.keys()]
	res = []

	for i in range(len(levels)):
		is_teens = False

		if len(levels[i]) != 1:
			digits = [int(digit) for digit in levels[i]]
			
			if digits[-2] == 1:
				is_teens = True

		else:
			digits = [int(levels[i])]

		digits = digits[::-1]
		word = []

		for j in range(len(digits)):
			if j == 0:
				if is_teens:
					word.append(f'{B[digits[j]]}')
				elif digits[j]:
					word.append(f'{A[digits[j]]}')
				else:
					pass
			elif j == 1:
				if digits[j] and not is_teens:
					word.append(f'{C[digits[j]]}')
				else:
					pass
			else:
				if digits[j]:
					word.append(f'{A[digits[j]]} {thousands[0]}')
				else:
					pass

		res.append(' '.join(word[::-1]))

		try:
			if i != len(levels) -1:
				res.append(thousands[i+1])
		
		except Exception as e:
			pass

	res = res[::-1]

	while '' in res:
		problem = res.index('')
		res = res[:problem] + res[problem+2:]

	return ' '.join(res)

N = input()
print(number_to_word(N))
```

### Solved!