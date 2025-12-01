# Écrire un programme Python pour compter le nombre de nombres pairs et impairs dans une série de nombres

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)


# Nombre de nombres pairs : 4                                                                                    
# Nombre de nombres impairs : 5
peer = 0
odd = 0

for n in numbers:
  if n % 2 == 0:
    peer += 1
  else:
    odd += 1
  
print(f"Nombre de nombres pairs : {peer}")
print(f"Nombre de nombres impairs : {odd}")

