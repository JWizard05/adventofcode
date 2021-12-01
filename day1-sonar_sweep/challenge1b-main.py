
from data import sonarScans

incCount = 0

for i in range(len(sonarScans) - 3):
	threeWindow = sonarScans[i] + sonarScans[i + 1] + sonarScans[i + 2]
	threeWindowNext = threeWindow - sonarScans[i] + sonarScans[i + 3]
	if threeWindow < threeWindowNext:
		incCount += 1

print(incCount)
