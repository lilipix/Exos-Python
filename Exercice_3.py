# Écrivez un programme Python pour obtenir la série de Fibonacci entre 0 et 50.

# Remarque : La Suite de Fibonacci est la série de nombres :
# 0, 1, 1, 2, 3, 5, 8, 13, 21, ....
# Chaque nombre suivant est trouvé en additionnant les deux nombres qui le précèdent.


# 1                                                                                                             
# 1                                                                                                             
# 2                                                                                                             
# 3                                                                                                             
# 5                                                                                                             
# 8                                                                                                             
# 13                                                                                                            
# 21                                                                                                            
# 34

number_one = 0
number_two = 1
number_two_bis = 0
number_one_bis = 0
print(number_one)
print(number_two)
sum = 0
for i in range(50):
  number_one_bis += 1
  number_two_bis += 1
  number_one = number_one_bis
  number_two= number_two_bis
  sum = number_one + number_two
  print(number_one, number_two, sum)
  
 
  
