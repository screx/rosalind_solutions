def read_fasta(fa):
	seqs = {}
	line = fa.readline()
	name = line[1:].replace("\n", "")
	while line:
		if line[0] == ">":
			name = line[1:].replace("\n", "")
			line = fa.readline()
		if name in seqs:
			seqs[name] += line.replace("\n", "")
		else:
			seqs[name] = line.replace("\n", "")
		line = fa.readline()
	return seqs	

def gc(dna):
	dna = dna.upper()
	total = len(dna)
	gc = 0
	for i in dna:
		if i == "G" or i == "C":
			gc += 1
	return float(gc)/float(total)

def max_gc(fa):
	f = open(fa, "r")
	seqs = read_fasta(f)
	f.close()
	vals = {}
	for i in seqs:
		vals[i] = gc(seqs[i])
	val = ""
	max_gc = 0
	for i in vals:
		if vals[i] >= max_gc:
			max_gc = vals[i]
			val = i
	print val
	print max_gc
		

