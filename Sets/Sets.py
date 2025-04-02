

sampllist=[1,2,1,3,2,3]
samplset=set(sampllist)

print (samplset)

if 3 in samplset:
    print ("yes")
else:
    print ("no")

samplset.add(4)
print (samplset)

samplset.add(3)
print (samplset)

samplset.remove(3)
print (samplset)