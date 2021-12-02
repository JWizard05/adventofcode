
inputFile = open("challenge2-data.txt", "r")

directionsList = []
for line in inputFile:
	stripped_line = line.strip()
	line_list = stripped_line.split()
	directionsList.append(line_list)

inputFile.close()

horizontalVal = 0
depthVal = 0
aimVal = 0

for i in range(len(directionsList)):
	if directionsList[i][0] == "forward":
		horizontalVal += int(directionsList[i][1])
		depthVal += (aimVal * int(directionsList[i][1]))
	elif directionsList[i][0] == "up":
		aimVal -= int(directionsList[i][1])
	elif directionsList[i][0] == "down":
		aimVal += int(directionsList[i][1])

print(horizontalVal * depthVal)
