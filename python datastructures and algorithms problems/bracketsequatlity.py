def balancedCheck(s):

	if len(s)%2 !=0:
		return False

	openings =set('{[(')
	matches = set([('[', ']') , ( '{' , '}' ), ( '(', ')' ) ])
	stack = []

	for paren in s:
		if paren in openings:
			stack.append(paren)
		else:
			if len(stack) == 0:
				return False

			last_open = stack.pop()

			if (last_open, paren) not in matches:
				return False

	return len(stack) == 0


a = balancedCheck('[{(})]')
print(a)