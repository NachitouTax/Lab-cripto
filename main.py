def cifrado_cesar(texto, corrimiento):
    resultado = ""
    
    # Recorre cada carácter en el texto
    for i in range(len(texto)):
        char = texto[i]

        # Cifra las letras mayúsculas
        if char.isupper():
            resultado += chr((ord(char) + corrimiento - 65) % 26 + 65)

        # Cifra las letras minúsculas
        elif char.islower():
            resultado += chr((ord(char) + corrimiento - 97) % 26 + 97)

        # Deja los caracteres no alfabéticos sin cambiar
        else:
            resultado += char

    return resultado

# Ejemplo de uso:
texto = input("Ingresa el texto a cifrar: ")
corrimiento = int(input("Ingresa el corrimiento: "))

texto_cifrado = cifrado_cesar(texto, corrimiento)
print("Texto cifrado:", texto_cifrado)
