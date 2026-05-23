
entrada = input("Dame cualquier numero que quieras: \n")
try:
    numero = float(entrada)
    
    while(input("Quieres sumarle 1 responde y para aceptar o escribe cualquier otra cosa para rechazar ").lower()=="y"):
        numero += 1
    print(f"Este es tu resultado: {numero}")

except ValueError:
    print("Por favor ingrese un valor correcto")