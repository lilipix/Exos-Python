# Écrivez un programme Python pour convertir les températures vers et depuis Celsius et Fahrenheit.

# temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")

# Saisissez la température que vous souhaitez convertir ? (par exemple, 45F, 102C etc.) : 104f                                     
# La température en Celsius est de 40 degrés.

temp = input("Input the temperature you like to convert? (e.g., 45F, 102C etc.) : ")
new_temp = ""
for t in temp:
  if t.isdigit():
    new_temp += t

if temp.endswith("F"):
  new_temp = (int(new_temp) -32) * 5/9
  print(f"La température en Celsius est de {new_temp}")
else:
  new_temp = (int(new_temp) * 9/5 ) + 32
  print(f"La température en Fareenheit est de {new_temp}")




