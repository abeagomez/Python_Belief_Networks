"""
The MIT License (MIT)

Copyright (c) 2016 Amalia Gómez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
__author__ = "Amalia Gomez"
__copyright__ = "Copyright 2016"
__license__ = "MIT"
__version__ = "1.0"
__email__ = "abeagomez@gmail.com"
__status__ = "Production"

import math

class VectorModel():
	"""
	terms -> Dictionary: terms -> (doc -> times term appears in doc)
	N -> total number of documents in the system
	"""
	def __init__(self, terms, N):
		self.N = N
		self.Dictionary = terms
	
	"""
	Number of documents in which the index term ki appears
	"""
	def Ni (self, Ki):
		return len(self.Dictionary[Ki])

	"""
	Row frequency of term ki in the document dj (the number of times the term
	ki is mentioned in the text of the document dj)
	"""
	def Freq(self, Ki, Dj):
		if Ki in self.Dictionary and Dj in self.Dictionary[Ki]:
			return self.Dictionary[Ki][Dj]
		return 0

	"""
	Normalized frequency of the term ki in the document dj
	"""
	def F(self, Ki, Dj):
		max_term, max_freq = self.MaxL(Dj)
		if max_freq is 0:
			return 0
		return float(self.Freq(Ki, Dj))/ float(max_freq)

	"""
	maximum over all terms which are mentioned in the text of the document dj
	"""
	def MaxL(self, Dj):
		term, freq = "", 0
		for i in self.Dictionary:
			if Dj in self.Dictionary[i] and self.Dictionary[i][Dj] > freq:
				term, freq = i, self.Dictionary[i][Dj]
		return (term, freq)

	"""
	Inverse document frequency for ki,
	"""
	def idf(self, Ki):
		return math.log(float(self.N) / float(self.Ni(Ki)))

	"""
	Weight of term ki in the document Dj
	"""
	def W(self, Ki, Dj):
		return self.F(Ki, Dj) * self.idf(Ki)

	"""
	Weight of term ki in the query q
	"""
	def Wq(self, Ki, q):
		return (0.5 + (0.5*float(q.count(Ki)) / float(self.max_Fq(q)) )) * self.idf(Ki) 

	"""
	max-frequency term in the query q
	"""
	def max_Fq(self, q):
		return max([q.count(w) for w in set(q)])

	"""
	Degree of similarity of the document dj with the query q
	"""
	def similarity(self, dj, q):
		Wkij = sum([self.Wq(ki, dj) for ki in self.Dictionary])
		Wkiq = sum([self.Wq(ki, q) for ki in self.Dictionary])
		return (Wkij*Wkiq) / (math.sqrt(Wkij**2) * math.sqrt(Wkiq**2))

	def modDj(self, Dj):
		pass

	def F2(self, Ki, Dj):
		return Freq(self, Ki, Dj)/modDj(self, Dj)
