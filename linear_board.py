from settings import BOARD_LENGTH

class LinearBoard():
    """
    Clase que representa un tablero de una sola columna
    x un jugador
    o otro jugador
    none un espacio vacio
    """

    def __init__(self):
        """
        Una lista de None
        """
        self._column = [None for i in range(BOARD_LENGTH)]

    def add(self, char):
        """
        Juega en la primera posición disponible
        """
        # Siempre y cuando no este lleno
        if self.is_full():
            # Buscamos la primera posicion libre (None) 
            i = self._column.index(None) # Al poner el index nos va a buscar el primer None ya que es lo que le pedimos
            # Lo sustituimos por char
            self._column[i] = char # Acabamos de sustituir el none por char

    def is_full(self):
        return self._column[-1] != None

    def is_victory(self, char):
        return False
    
    def is_tie(self, char1, char2):
        """
        No hay victoria ni de char1 ni de char2
        """
        return (self.is_victory("x") == False and self.is_victory("o") == False)