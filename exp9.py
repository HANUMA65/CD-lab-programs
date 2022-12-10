
gram = {
	"S":["CC"],
	"C":["aC","d"]
}
start = "S"
terms = ["a","d","$"]

non_terms = []
for i in gram:
	non_terms.append(i)
gram["S'"]= [start]


new_row = {}
for i in terms+non_terms:
	new_row[i]=""


non_terms += ["S'"]
# each row in state table will be dictionary {nonterms ,term,$}
stateTable = []
# I = [(terminal, closure)]
# I = [("S","A.A")]

def Closure(term, I):
	if term in non_terms:
		for i in gram[term]:
			I+=[(term,"."+i)]
	I = list(set(I))
	for i in I:
		# print("." != i[1][-1],i[1][i[1].index(".")+1])
		if "." != i[1][-1] and i[1][i[1].index(".")+1] in non_terms and i[1][i[1].index(".")+1] != term:
			I += Closure(i[1][i[1].index(".")+1], [])
	return I
