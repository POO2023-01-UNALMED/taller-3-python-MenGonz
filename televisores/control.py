class Control:
    __tv = 0

    #métodos igualiticos
    def turnOn(self):
        self.__tv.turnOn()
    def turnOff(self):
        self.__tv.turnOff()
    def canalUp(self):
        self.__tv.canalUp()
    def canalDown(self):
        self.__tv.canalDown()
    def volumenUp(self):
        self.__tv.volumenUp()
    def volumenDown(self):
        self.__tv.volumenDown()
    def setCanal(self, canal):
        self.__tv.setCanal(canal)
    #métodos propios
    def enlazar(self,tv):
        self.__tv = tv
        tv.setControl(self)
    
    #métodos de clase
    @classmethod    
    def getTv(cls):
        return cls.__tv
    @classmethod
    def setTv(cls,tv):
        cls.__tv = tv
