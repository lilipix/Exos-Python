# Écrivez un programme Python qui accepte une chaîne et calcule le nombre de chiffres et de lettres



# Saisissez une chaîne IPSSI2024
# Lettres 5                                                                                                                    
# Chiffres 4

numbers = ""
letters = ""
string = "IPSSI2024"
for s in string:
  if s.isdigit():
    numbers += s
  else:
    letters += s
print(f"Lettres {letters}")
print(f"Chiffres {numbers}")


