def ham(dna1, dna2):
	l = len(dna1)
	distance = 0
	for i in range(l):
		if dna1[i] != dna2[i]:
			distance += 1
	return distance

def solution(txt):
	f = open(txt)
	dna1 = f.readline()
	dna2 = f.readline()
	f.close()
	return ham(dna1, dna2)
