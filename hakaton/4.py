sequence_0 = (14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0)
sequence_1 = [14,10,35,45,'60',70,90,0,105,150,'70']
sequence_2 = [14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70',0.0]
sequence_3 = [14,10,35,45,'60',70,90,0,105,150,10.0,45.0,'70']
setarr = set(sequence_0)
for x in range(1):
  if len(sequence_0) == len(setarr):
      print("Все элементы уникальны")
  else:
        print("Есть одинаковые")
setarr = set(sequence_1)
for x in range(1):
  if len(sequence_1) == len(setarr):
      print("Все элементы уникальны")
  else:
        print("Есть одинаковые")
setarr = set(sequence_2)
for x in range(1):
  if len(sequence_2) == len(setarr):
      print("Все элементы уникальны")
  else:
        print("Есть одинаковые")
setarr = set(sequence_3)
for x in range(1):
  if len(sequence_3) == len(setarr):
      print("Все элементы уникальны")
  else:
        print("Есть одинаковые")
