inp=input("Enter a word")
alphabet=set("abcdefghijklmnopqrstuvwxyz")
inp_set=set(inp)

intersection=(alphabet&inp_set)
print (intersection)

if len(intersection)==26:
    print ("thats a panagram")
else:
    print ("thats not a panagram")