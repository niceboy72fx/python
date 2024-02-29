
def re_range(start = 0 , end = 0 , step = 1):
		if end == 0:
					return [start]
		elif (start < end):
					return [start] + re_range(start + step, end, step) 
		else:
					return []
					
					
print(re_range(0,4,1))
