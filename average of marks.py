marks={}
for i in range(5):
    m=int(input("enter marks"))
    marks["sub"+str(i+1)]=m
print(marks)
tot=0
sublist=" "
for item in marks.items():
    sublist+=item[0]+","
    tot=tot=item[1]
print("list of subs",sublist)
print("tot=",tot)
print("no of sub=",len(marks))
print("avg=",tot/len(marks))
