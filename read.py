import string

# Función para descifrar usando el cifrado César con un corrimiento específico
def cesar_decrypt(text, shift):
    decrypted_text = []
    for char in text:
        if char.isalpha():
            shift_amount = 65 if char.isupper() else 97
            decrypted_text.append(chr((ord(char) - shift_amount - shift) % 26 + shift_amount))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)
# Función para evaluar cuántas palabras de un texto son reconocibles en un diccionario
def count_spanish_words(text, dictionary):
    words = text.split()
    count = sum(1 for word in words if word.lower() in dictionary)
    return count

# Función para probar todos los corrimientos posibles
def brute_force_decrypt(text, dictionary):
    probable_text = ""
    max_word_count = 0
    probable_shift = 0
    
    for shift in range(26):
        decrypted_text = cesar_decrypt(text, shift)
        word_count = count_spanish_words(decrypted_text, dictionary)
        if word_count > max_word_count:
            max_word_count = word_count
            probable_text = decrypted_text
            probable_shift = shift
        print(f"Shift {shift}: {decrypted_text}")
    
    return probable_shift, probable_text

# Función principal para manejar el descifrado
def main():
    # Texto cifrado proporcionado
    encrypted_text = "Kzqxbw tijwzibwzqw" 
    # Diccionario simple de palabras en español
    spanish_words = set([
        "cripto", "laboratorio", "el", "la", "los", "las", "de", "y", "a", "en", "es", "un", 
        "una", "por", "con", "no", "una", "sus", "al", "lo", "como", "más", "o", "pero", 
        "sus", "le", "ha", "me", "si", "sin", "sobre", "este", "ya", "entre", "cuando", 
        "todo", "también", "son", "ser", "hay", "este", "mi", "mis", "tu", "que", "quien", "cual"
    ])
    print("Probando todas las combinaciones posibles...\n")
    probable_shift, probable_text = brute_force_decrypt(encrypted_text, spanish_words)
    # Mostrar el mensaje más probable en verde
    print(f"\n\033[92mEl mensaje más probable es: '{probable_text}' con un corrimiento de {probable_shift}\033[0m")
if __name__ == "__main__":
    main()
