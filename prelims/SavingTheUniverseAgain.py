def calcDamage(program):
	dmg = 0
	atk = 1
	finAtk = 1
	for cmd in program:
		if cmd == 'S':
			dmg += atk
			finAtk = atk
		else:
			atk *= 2
	return dmg, finAtk

def hackRobot(lenProg, idx, atk, dmg, program):
	while idx > 0:
		if program[idx] == 'S' and program[idx - 1] == 'C':
			program[idx], program[idx - 1] = program[idx - 1], program[idx]
			if idx + 1 < lenProg and program[idx +	 1] == 'S':
				idx += 1
				dmg -= atk // 2
			else:
				idx -= 1
				atk //= 2
				dmg -= atk
			return program, idx, atk, dmg, True
		idx -= 1
	return program, idx, atk, dmg, False

def saveTheUniverse(num, shield, program):
	swaps = 0
	dmg, atk = calcDamage(program)
	listProg = list(program)
	lenProg = len(program)
	lastIdx = lenProg - 1
	while dmg > shield:
		program, lastIdx, atk, dmg, changed = hackRobot(lenProg, lastIdx, atk, dmg, listProg)
		if changed == False:
			print("Case #" + str(num) + ": IMPOSSIBLE")
			return
		else:
			swaps += 1
	print("Case #" + str(num) + ": " + str(swaps))
	return

# Main
numTests = int(input())
for x in range(numTests):
	arr = input().split()
	saveTheUniverse((x + 1), int(arr[0]), arr[1])