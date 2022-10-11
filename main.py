words = input().split(" ")
ans = []
for i in range(0, len(words)):
	if (words[i].find("a") == -1 or words[i].find("r") == -1 or words[i].find("e") == -1):
		continue
	if ("are" in words[i]):
		ans.append(words[i])
		continue
	copy = words[i]
	find = False
	aindex = -1
	rindex = -1
	eindex = -1
	for j in range(0, words[i].count("a")):
		aindex = copy.find("a")
		copy = copy[:aindex] + copy[aindex + 1:]
		for k in range(0, words[i].count("r")):
			rindex = copy.find("r")
			copy = copy[:rindex] + copy[rindex + 1:]
			for i1 in range(0, words[i].count("e")):
				eindex = copy.find("e")
				copy = copy[:eindex] + copy[eindex + 1:]
				if (aindex <= rindex and rindex <= eindex):
					ans.append(words[i])
					find = True
					break
				if (find == True):
					break
			if (find == True):
				break
		if (find == True):
			break
print(ans)