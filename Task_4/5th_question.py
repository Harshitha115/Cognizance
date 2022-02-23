rows = int(input("Enter no.of Rows = "))
for p in range(rows - 1, -1, -1):
  for r in range(0, p):
        print(end = ' ')
  for h in range(p, rows):
        print('*', end = ' ')
  print()
