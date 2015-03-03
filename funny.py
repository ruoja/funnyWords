# Find the funnies words in given text.
 
#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, re
from pprint import pprint

text = open(sys.argv[1])
pattern = re.compile('[aeiouyäö]+', re.I)

def funny(x): return x * 2 ** x

def getKey(item):
	return item[1]

def listUniqueWords():
	wordSet = set()
	for line in text:
		for word in line.split():
			wordSet.add(word)
	return list(wordSet)

def countWeight(word):
	chains = [funny(match.end() - match.start()) for match in re.finditer(pattern, word)]
	return sum(chains,0)

words = listUniqueWords()
result = [(word, countWeight(word)) for word in words]
text.close()
pprint(sorted(result, key = getKey))
