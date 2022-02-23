
H=[]
M=int(input("Enter the num of records to be stored:"))

for i in range (M):
     R=input("Enter the record (Roll no, Name, Marks):")
     S=R.split()
     P=list(S)
     H.append(P)
print("Roll no", "Name", "Marks", sep='   ')
for i in H:
    print(i[0], i[1], i[2], sep='        ')
J = H[1]
print(J[0], J[1], J[2], sep='   ')

