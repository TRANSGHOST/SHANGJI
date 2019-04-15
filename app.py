squares=[]
for value in range(1,11):
	squares.append(value**2)                                               
print(squares)

for value in range(1,21):
	print(value)
squares=[value for value in range(1,1000001)]
#for value in squares:
#    print(value)

print(min(squares))
#max,sum
print(sum(squares))

nlist=[value for value in range(1,21,2)]
for value in nlist:
	print(value)

nlist=[value for value in range(3,31,3)]
for value in nlist:
	print(value)


nlist=[value**3 for value in range(1,11)]
for value in nlist:
	print(value)
