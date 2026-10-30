palabra= input("Escribe una palabra:")
vocales =0
for letra in palabra.lower():
    if letra in "aeiou":
        vocsles+=1

print("Tiene",vocales, "vocales")
