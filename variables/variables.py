#Definiendo una variable con snake_case
nombre_completo_de_tu_tio_master= "Lucas"

#concatenar con f-string (funciona incluyendo mas tipos de datos sin el format)
bienvenida= f"Hola {nombre_completo_de_tu_tio_master} ¿Como estas?"

#concatenar con +
bienvenida= f"Hola " +nombre_completo_de_tu_tio_master+ "¿Como estas?"

del nombre_completo_de_tu_tio_master #Eliminar datos

print(bienvenida)

#Operadores de pertenencia (in / not in)

print("Lucas" in bienvenida) #false

print("Lucas" not in bienvenida) #false
