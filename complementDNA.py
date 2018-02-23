def reverse(dna):
	dna_rev = ""
	i = len(dna) - 1
	while i >= 0:
		dna_rev += dna[i]
		i-=1
	return dna_rev

def complement(dna):
	complement = ""
	for i in dna:
		if i == "A":
			complement += "T"
		if i == "T":
			complement += "A"
		if i == "C":
			complement += "G"
		if i == "G":
			complement += "C"
	return complement

def reverse_complement(dna):
	return reverse(complement(dna))


