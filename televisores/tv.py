class TV:

    __numTV = 0
    #constructor
    def __init__(self, cls, marca, estado):
        self.__marca = marca
        self.__estado = estado
        self.__canal = 1
        self.__precio = 500
        self.__volumen = 1
        self.__control = None
        cls.__numTV += 1


    #setters:
    def setMarca(self, marca):
        self.__marca = marca
    def setControl(self, control):
        self.__control = control
    def setPrecio(self, precio):
        self.__precio = precio
    def setVolumen(self,volumen):
        self.__volumen = volumen 
    def setCanal(self,canal):
        self.__canal = canal
    

    #getters:
    def getMarca(self):
        return self.__marca
    def getControl(self):
        return self.__control
    def getPrecio(self):
        return self.__precio
    def getVolumen(self):
        return self.__volumen
    def getCanal(self):
        return self.__canal
    def getEstado(self):
        return self.__estado  

    #métodos de estado
    def turnOn(self):
        self.__estado = True
    def turnOff(self):
        self.__estado = False

    #métodos de canal
    def canalUp(self):
        if (self.__canal + 1 <= 120) and (self.__estado == True):
            self.__canal += 1
    def canalDown(self):
        if (self.__canal - 1 >= 1) and (self.__estado == True):
            self.__canal -= 1

    #métodos de volumen
    def volumenUp(self):
        if (self.__volumen + 1 <= 7) and (self.__estado == True):
            self.__volumen += 1
    def volumenDown(self):
        if (self.__volumen - 1 >= 0) and (self.__estado == True):
            self.__volumen -= 1
    
    #métodos de clase
    @classmethod
    def getNumTV(cls):
        return cls.__numTV  
    
    @classmethod
    def setNumTV(cls,numTV):
        cls.__numTV = numTV