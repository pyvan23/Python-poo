#Las subClases debe poder hacer todo lo que hace la super clase


class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        return 'Volando...'
    
class AveNoVoladora(Ave):
    def volar(self):
        pass
    
class AveNadadora(Ave):
    def volar(self):
        pass