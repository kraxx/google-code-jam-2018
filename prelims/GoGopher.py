def goGopher(limit):

	plot = [[False for _ in range(limit + 3)] for _ in range(4)]
	row, col = 1, 1
	leftCol = 0
	curRow = True # True == Top, False == Bottom
	filledCol = 0
	while leftCol < limit: # Keep filling leftmost columns
		print(row + 1, col + 1)
		res = list(map(int, input().split(" ")))
		if res[0] == 0 or res[0] == -1: # End of test
			return
		resRow, resCol = res[0] - 1, res[1] - 1
		if plot[resRow][resCol] == False: # Was empty plot, commence checks
			
			if resCol == leftCol: # LeftCol checks
				filledCol += 1
				if filledCol == 4:
					while filledCol == 4 and leftCol < limit: # Increment leftCol if filled
						filledCol = 0
						leftCol += 1
						for x in range(4):
							if plot[x][leftCol] == True:
								filledCol += 1
					curRow = True
					row, col = 1 if curRow == True else 2, leftCol + 1
					continue

			plot[resRow][resCol] = True
			if curRow == True:
				if plot[curRow][leftCol] == True:
					curRow = False

		row, col = 1 if curRow == True else 2, leftCol + 1

	filledRow = 0	
	for x in range(limit, limit + 3):
		if plot[0][x] == True:
			filledRow += 1
	if filledRow == 3:
		curRow = False

	if curRow == True:
		while filledRow < 3:
			print(2, limit + 2)
			res = list(map(int, input().split(" ")))
			if res[0] == 0 or res[0] == -1: # End of test
				return
			resRow, resCol = res[0] - 1, res[1] - 1
			if resRow == 0 and plot[resRow][resCol] == False:
				plot[resRow][resCol] = True
				filledRow += 1

	while True:
		print(3, limit + 2)
		res = list(map(int, input().split(" ")))
		if res[0] == 0 or res[0] == -1: # End of test
			return


	# while True:
	# 	print(row + 1, col + 1)
	# 	res = list(map(int, input().split(" ")))
	# 	if res[0] == 0 or res[0] == -1: # End of test
	# 		return
	# 	resRow, resCol = res[0] - 1, res[1] - 1
	# 	if plot[resRow][resCol] == False: # Was empty plot, commence checks

	# 		plot[resRow][resCol] = True
	# 		# filledBox += 1
	# 		if curRow == True and resRow == 0:
	# 			filledRow += 1
	# 			if filledRow == 4:
	# 				curRow = False

	# 	row, col = 1 if curRow == True else 2, leftCol + 1


# Main
numTests = int(input())
for _ in range(numTests):
	area = int(input())
	if area == 200:
		goGopher(47)
	else:
		goGopher(2)