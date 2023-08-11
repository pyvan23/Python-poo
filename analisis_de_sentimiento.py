import openai
import os

#api_key = os.environ.get("")
#openai.api_key = api_key

system_rol = '''Hace de cuenta que sos un analizador de sentimiento.
                Yo te paso sentimientos y vos analizas el sentimiento de los mensajes
                y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
                SOLO RESPUESTAS NUMERICAS. donde -1 es negatividad maxima, 0 es neutral y 
                1 es positividad maxima(Podes responder con ints o floats solamente)'''
                
mensajes = [{"role":"system", "content":system_rol}]

class AnalizadorDeSentimiento:
    
    def analizar_sentimiento(self,polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m" + "Negativo"
        elif polaridad > -0.3 and polaridad < 0:
            return "\x1b[1;31m" + "Algo Negativo"
        elif polaridad >= -0.1 and polaridad <= 0.1: 
            return "\x1b[1;33m" + "Neutral"
        elif polaridad >= -0.1 and polaridad <= 0.4: 
            return "\x1b[1;32m" + "Algo positivo"
        elif polaridad >= 0.4 and polaridad <= 0.9: 
            return "\x1b[1;32m" + "Positivo"
        elif  polaridad > 0.9: 
            return "\x1b[1;32m" + "Muy positivo"
        else:
            return "\x1b[1;32m" + "Muy Negativo"
        



analizador = AnalizadorDeSentimiento()

while True:
    user_prompt = input("\x1b[1;33m" + "\nCuentame Algo: "+ "\x1b[1;37m")
    mensajes.append({"role":"user","content":user_prompt})
    
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )
    
    respuesta = completion.choice[0].message["content"]
    mensajes.append({"role":"assistans","content":respuesta})
    
    sentimiento = analizador.analizar_sentimiento(float(respuesta))
    print(sentimiento)