import sys
import time
import random 
sys.setrecursionlimit(10000)

def selection(l):
    st = time.time()
    for i in range(0, len(l)):
        for in_eac in range(i, len(l)):
            if l[i] > l[in_eac]:
                (l[i], l[in_eac]) = (l[in_eac], l[i])
    #print(l)
    print(time.time() - st )

def insertion(l):
    st = time.time()
    for i in range(0, len(l)-1):
        for in_eac in range(i+1, 0, -1):
            if l[in_eac] < l[in_eac-1]:
                (l[in_eac], l[in_eac-1]) = (l[in_eac-1], l[in_eac])
            else:
                break
    #print(l)                
    print(time.time() - st )

def mergecall(l):
	st = time.time()
	l = mergesort(l,0,len(l))
	#print(l)
	print(time.time() - st )

def mergesort(l, left, right):
	if (right - left) <= 1:
		return (l[left:right])
	if (right - left) > 1:
		mid = (left + right) // 2 
		a = mergesort(l, left, mid)
		b = mergesort(l, mid, right)
	return (merge(a,b))
	
def merge(l, r):
	x = []
	
	i = 0
	j = 0
	
	while(len(x) < len(l) + len(r)):
		if i == len(l):
			x = x + r[j:]
			break
		elif j == len(r):
			x = x + l[i:]
			break
		elif l[i] <= r[j]:
			x.append(l[i])
			i += 1
		elif r[j] <= l[i]:
			x.append(r[j])
			j += 1

	return x

def quickcall(a):
	st = time.time()
	for i in range(0, (len(a)//2)):
		j = random.randrange(0, len(a), 1)
		k = random.randrange(0, len(a), 1)
		(a[j], a[k]) = (a[k], a[j])
		
	quick(a, 0, len(a))	
	print(time.time() - st)
		
def quick(a, left, right):

	if (right - left) <= 1:
		return a 

	yellow = left + 1
	for green in range(left+1, right):
		if a[green] <= a[left]:
			(a[green], a[yellow]) = (a[yellow], a[green])
			yellow += 1
	
	(a[left], a[yellow-1]) = (a[yellow-1], a[left])
	
	quick(a, left, yellow-1)
	quick(a, yellow, right)
	

