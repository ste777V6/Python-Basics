for x in range(4):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

