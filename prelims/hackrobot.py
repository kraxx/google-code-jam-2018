def calcDamage(program):
	dmg = 0
	atk = 1
	for cmd in program:
		if cmd == 'S':
			dmg += atk
		else:
			atk *= 2
	return dmg

def hackRobot(idx, program):

	idx = len(program) - 1
	while idx > 0:
		if program[idx] == 'S' and program[idx - 1] == 'C':
			program[idx], program[idx - 1] = program[idx - 1], program[idx]
			program = "".join(program)
			return program, True
		idx -= 1
	return program, False

def saveTheUniverse(num, shield, program):

	swaps = 0
	lastIdx = len(program) - 1
	while calcDamage(program) > shield:
		program, changed = hackRobot(lastIdx, list(program))
		if changed == False:
			print("Case #" + str(num) + ": IMPOSSIBLE")
			return
		else:
			swaps += 1
	print("Case #" + str(num) + ": " + str(swaps))
	return


# if __name__ == "__main__":
numTests = int(input())
for x in range(numTests):
	arr = input().split()
	saveTheUniverse((x + 1), int(arr[0]), arr[1])