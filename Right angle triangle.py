#Take input
print("half pyramid pattern of the stars(*): ")
n=int(input("enter the number of rows:"))
#outer loop to  handle number of rows
for i in range(n):
#inner loop to handle number of coulumns
  for j in range(i+1):
  #display result
    print("*",end="")
  print()

