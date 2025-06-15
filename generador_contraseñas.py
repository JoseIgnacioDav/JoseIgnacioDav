import random
print("")
print("Bienvenido a este generador de contraseñas")
print("")
inicio = input("Ingresa 1 si quieres crear una contraseña , Ingresa cualquier otro caracter si quieres salir ->  ")
                                                                                             
if inicio == "1":
 print("")
 longitud_contraseña = input("Ingresa el numero de caracteres que necesita la contraseña, SOLO INGRESAR NUMEROS ->  ")
 validacion_longitud_contraseña = longitud_contraseña.isnumeric()
 if validacion_longitud_contraseña == True:
   longitud_contraseña_entero = int(longitud_contraseña)
   print(    ""                                                       )
 
   letras_y_numeros = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789" #creo una cadena de letras y numeros

   simbolos = "@!$%&*.,_/?<>|{}[]()#-;:"   #creo una cadena de simbolos 

   todos_los_caracteres = letras_y_numeros + simbolos # aqui concateno las dos cadenas en una sola 

   clave_generada = "" # igualo clave generada a un valor vacio, aqui va a entrar la clave luego que se genere

   # uso for para que elija un caracter al azar en funcion de la longitud de caracteres que le pase
   for _ in range(longitud_contraseña_entero): #utilizo el _ en el for por que no necesito un contador, me generaria errores, necesito que se repita las veces que indica la longitud de la clave
    caracter_al_azar = random.choice(todos_los_caracteres) #aqui el programa elige un valor al azar de la cadena con todos las letras y simbolos y lo igualo a la variable caracter al azar
    clave_generada = clave_generada + caracter_al_azar # ya aqui se genera el primer caracter y se suma al primer caracter + el segundo caracter y luego se suma el primer caracter + el segundo + el tercero +.... y se va a ejecutar por la cantidad de caracteres que pida la longitud
 
   print(f"tu clave generada es: {clave_generada}") # luego de salir del for ya nos da la clave que termino de concatenarse y lo concateno con un tu clave generada es
 else:print("debe contener numeros, saliste del programa") 
else: print("saliste del programa") 

 

 









