A = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven',
	'eight', 'nine']
B = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
	'sixteen', 'seventeen', 'eighteen', 'nineteen']
C = ['zero', 'ten', 'twenty', 'thirty', 'forty', 'fifty',
	'sixty', 'seventy', 'eighty', 'ninety']
D = {'hundred': 2, 'thousand': 3, 'million': 6,
	'billion': 9, 'trillion': 12, 'quadrallion': 15,
	'quintallion': 18}

def read(s):
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

	def word_to_number(x):
		x = x.lower().split()
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
		
	try:
		int(s)
		return number_to_word(s)
	except:
		return word_to_number(s)