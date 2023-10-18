import keyboard
import serial
import serial.tools.list_ports
import time
ports = serial.tools.list_ports.comports()
portsList = []

## cek port yang tersedia
for onePort in ports:
    portsList.append(str(onePort))
    print(str(onePort))
    
## pilih port
val = input("Select Port: COM")
for x in range(0,len(portsList)):
    if portsList[x].startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(portVar)

# Konfigurasi koneksi Serial
serialInst = serial.Serial(port=portVar, baudrate=9600)

try:
    while True:
        if serialInst.in_waiting:
            packet = serialInst.readline()
            print(packet.decode('utf').rstrip('\n'))
        
        if keyboard.is_pressed('h'):  # Cek apakah tombol "h" ditekan
            print("Tombol 'h' ditekan, mengirim perintah ke Arduino...")
            serialInst.write('H'.encode())  # Kirim perintah 'H' ke Arduino
            time.sleep(0.5)  #biar ga spamming
            
        elif keyboard.is_pressed('l'):  # Cek apakah tombol "l" ditekan
            print("Tombol 'l' ditekan, mengirim perintah ke Arduino...")
            serialInst.write('L'.encode())  # Kirim perintah 'L' ke Arduino
            time.sleep(0.5)  #biar ga spamming
        else:
            # 
            pass
except KeyboardInterrupt:
    serialInst.close()
  