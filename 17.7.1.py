for i in range (1,10):
   print()
   if i % 2 == 0:
      continue
   for j in range (1,10):
      if j % 2 == 0:
         continue
      multipl = i * j
      print(multipl)