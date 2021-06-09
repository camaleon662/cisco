file=open("devices.txt","a")
while True:
    newItem=input("Introduce un nuevo dispositivo: ")
    if newItem == "exit":
       print("All done!")
       break
    file.write(newItem + "\n")
file.close()
