import pdb
dev_flag = 'Y'


def trace():
	global dev_flag
	if dev_flag == 'Y':
		pdb.set_trace()

def sum_till_n(list_n):
	i = 0
	result = []
	trace()
	for num in list_n:
		i=0
		for j in range(1,num+1):
			i = i + j
		result.append(i)
	return result



if __name__ == '__main__':
	print sum_till_n([2,3,1])
	trace()
	print 9*9
# Desired output [3,6,1]

