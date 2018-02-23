def count_dna(dna):
	dna = dna.upper()
	frequency = {}
	for i in dna:
		if i in frequency:
			frequency[i] += 1
		else:
			frequency[i] =1
	return "{A} {C} {G} {T}".format(frequency["A"], frequency["C"], frequency["G"], frequency["T"])
