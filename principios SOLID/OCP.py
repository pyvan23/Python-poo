class Notificador:
    def __init__(self,usuario,mensaje) -> None:
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
        raise NotImplementedError
    
class NotificadorEmail(Notificador):
    def notificar(self):
        print(f'Enviando el email a {self.usuario.email}')
        
class NotificadorSMS(Notificador):
    def notificar(self):
        print(f'Enviando el mensaje {self.usuario.sms}')        
    
class NotificadorWhatsApp(Notificador):
    def notificar(self):
        print(f'Enviando el Whats APP {self.usuario.whatsApp}')        
    
        