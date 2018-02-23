def DNAtoRNA(dna):
	l = len(dna)
	dna = dna.upper()
	rna = ""
	for i in range(l):
		if dna[i] == "T":
			rna += "U"
		else: 
			rna += dna[i]
	return rna
