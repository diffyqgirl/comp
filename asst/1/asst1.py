import collections
import string

def swap_chars(s):
	ctr = collections.Counter()
	for c in s.lower():
		if (string.ascii_letters.find(c) != -1):
			ctr.update(c)
	most_common = ctr.most_common(1)[0][0]
	least_common = ctr.most_common()[-1][0]
	new = ""
	for c in s:
		if (c == most_common):
			new += least_common
		elif (c == least_common):
			new  += most_common
		elif (c == most_common.upper()):
			new += least_common.upper()
		elif (c == least_common.upper()):
			new += most_common.upper()
		else:
			new += c
	return new

def get_key(x):
	return x[0]

def sort_cat(_n_, *args):
	lengths = []
	for arg in args:
		lengths.append((len(arg), arg))
	lengths.sort(reverse = True, key=get_key)
	new = ""
	for i in xrange(_n_):
		new += lengths[i][1]
	return new


s = 'I\'m just a chi-town coder with a nice flow.'
print swap_chars(s)
print sort_cat(2, "cats", "umbrellas", "dogs", "piggies")
states = {} #key is abbreviation, value is state
codes = {} #key is state, value is abbreviation
with open("states.txt") as my_file:
	for line in my_file:
		states[line[-3:-1]] = line[0:-4]
		codes[line[0:-4]] = line[-3:-1]

def bluesclues(abbrev):
	return states[abbrev]

print bluesclues("VA")

def bluesbooze(state):
	return codes[state]

print bluesbooze("Virginia")


