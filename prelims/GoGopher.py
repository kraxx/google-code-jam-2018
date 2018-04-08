def goGopher(limit):

	plot = [[False for _ in range(limit)] for _ in range(3)]
	leftCol = 0
	filledCol = 0
	while leftCol < limit - 2: # Keep filling leftmost columns
		print(2, leftCol + 2)
		res = list(map(int, input().split(" ")))
		if res[0] == 0: # End of test
			return True
		elif res[0] == -1:
			return False

		resRow, resCol = res[0] - 1, res[1] - 1
		if plot[resRow][resCol] == False: # Was empty plot, commence checks

			if resCol == leftCol: # LeftCol checks
				filledCol += 1
				if filledCol == 3:
					while filledCol == 3 and leftCol < limit - 2: # Increment leftCol if filled
						filledCol = 0
						leftCol += 1
						for x in range(3):
							if plot[x][leftCol] == True:
								filledCol += 1
					continue

			plot[resRow][resCol] = True

	while True:
		print(2, limit - 1)
		res = list(map(int, input().split(" ")))
		if res[0] == 0: # End of test
			return True
		elif res[0] == -1:
			return False

# Main
numTests = int(input())
for _ in range(numTests):
	area = int(input())
	if area > 9000: # lol
		exit()
	limit = (area // 3) + (0 if area % 3 == 0 else 1)
	if goGopher(limit) == False:
		exit()