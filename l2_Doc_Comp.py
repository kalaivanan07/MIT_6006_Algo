import time
import math 

def doc_compare():

	f_a = input('file_a: ')
	f_b = input('file_b: ')

	start_time = time.time()
	
	'''
	print(f_a)
	print(f_b)
	'''
	
	dict_a = word_count(f_a)
	dict_b = word_count(f_b)

	'''
	print(dict_a)
	print(dict_b)
	'''
	
	dot_product = 0 	
	length_a    = 0	
	length_b    = 0	
	
	for eac in dict_b:
		length_b = length_b + dict_b[eac]*dict_b[eac]
	
	for eac in dict_a:
		length_a = length_a + dict_a[eac]*dict_a[eac]
		if eac in dict_b:
			print(eac)
			'''
			print(dict_a[eac] , ','  , dict_b[eac])
			'''
			dot_product = dot_product +  (dict_a[eac] * dict_b[eac])
	
	
	print(dot_product)			
	print(length_a)			
	print(length_b)			
	
	costheta = dot_product / (math.sqrt(length_a) * math.sqrt(length_b))
	
	print(costheta)
	print("--- %s seconds ---" % (time.time() - start_time))
	
def word_count(fname):

	fh = open(fname, 'r')
	words_count = {}

	while True:
		aLine = fh.readline()
		aLine = aLine.rstrip('\n')
		'''
		print(aLine.split(" "))
		'''
		if not aLine:
			break
		for eac in aLine.split(" "):
			if eac in words_count:
				words_count[eac] =  words_count[eac] + 1 
			else:
				words_count[eac] = 1
	
	return words_count 
