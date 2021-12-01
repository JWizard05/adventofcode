
from challenge1-data import sonarScans

incCount = 0

for i in range(len(sonarScans)):
	if sonarScans[i] > sonarScans[i - 1]:
		incCount += 1

print(incCount)
