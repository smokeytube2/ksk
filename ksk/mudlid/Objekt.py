from mudlid.KinemaatikaMudel import KinemaatikaMudel

from abc import abstractmethod

class Objekt(KinemaatikaMudel):
    def __init__(self, ekraan, esialgne_kiirus, nurk, gravitatsioon, dt, suurus, värv) -> None:
        super().__init__(esialgne_kiirus, nurk, gravitatsioon, dt)
        self.esialgne_kiirus = esialgne_kiirus
        self.nurk = nurk
        self.suurus = suurus
        self.ekraan = ekraan
        self.värv = värv
        self.tüüp = None
        
    @abstractmethod
    def _joonista_(self) -> None:
        """
        Kaitstud funktsioon joonistab objekti ekraanile. Lapse klass peab määrama.
        """
        pass
    
    def __uuenda__(self) -> None:
        """
        Privaatfunktsioon uuenda objektiandmeid lapsevanema klassi kaudu.
        """
        super().uuenda()
    
    def protsess(self) -> None:
        self._joonista_()
        self.__uuenda__()

    @property
    def objekti_andmed_võtja(self) -> dict:
        """
        Tagastab objekti andmed. Seda kutsutakse simulatsiooni 
        lõpus, et näidata kasutajale kulunud aega ja läbitud vahemaad.
        """
        return {
            "tüüp": self.tüüp,
            "suurus": self.suurus,
            "värv": self.värv,
            "positsioon": (self.positsioon_x, self.positsioon_y),
            "gravitatsioon": self.gravitatsioon,
            "esialgne_kiirus": self.esialgne_kiirus,
            "nurk": self.nurk,
            "aeg": self.aeg,
            "dt": self.dt
        }
