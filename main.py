import pywhatkit


phone_number = input("Numero de celular a enviar el mensaje:")


pywhatkit.sendwhatmsg("phone_number", "Test bot de mensajes", 10,30,2,True,2)




