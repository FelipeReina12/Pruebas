#-------------Clase Padre----------------------------------------
class Deportista:
    def __init__(self,nombre: str, documento: int,edad: int):
        self.__nombre =  nombre
        self.__documento =  documento
        self.__edad =  edad

    #---------------------Getters-------------------------------
    def getNombre(self):
        return self.__nombre

    def getDocumento(self):
        return self.__documento

    def getEdad(self):
        return self.__edad

    #---------------------Setters-------------------------------
    def setNombre(self, nombre: str):
        self.__nombre = nombre

    def setDocumento(self, documento: int):
        self.__documento = documento

    def setEdad(self, edad: int):
        self.__edad = edad

#-----------------------Clase Hijo--------------------------------
class DeportistaFutbol(Deportista):
    def __init__(self, nombre: str, documento: \
        int, edad: int, golesAnotados: int, \
            nombreEquipo: str):
        super().__init__(nombre, documento, edad)
        self.__golesAnotados = golesAnotados
        self.__nombreEquipo = nombreEquipo

    #---------------------Getters Hijo-------------------------------
    def getgolesAnotados(self):
        return self.__golesAnotados
    
    def getnombreEquipo(self):
        return self.__nombreEquipo
    
    #---------------------Setters Hijo-------------------------------
    def setGolesAnotados(self, golesAnotados):
        self.__golesAnotados = golesAnotados

    def setNombreEquipo(self, nombeEquipo):
        self.__nombreEquipo = nombeEquipo

class DeportistaTennis(Deportista):
    def __init__(self, nombre: str, documento: \
        int, edad: int, setsGanados: int, \
            setsPerdidos: int):
        super().__init__(nombre, documento, edad)
        self.__setsGanados = setsGanados
        self.__setsPerdidos = setsPerdidos

    #---------------------Getters Hijo-------------------------------
    def getSetsGanados(self):
        return self.__setsGanados
    
    def getSetsPerdidos(self):
        return self.__setsPerdidos
    
    #---------------------Setters Hijo-------------------------------
    def setSetsGanados(self, setsGanados):
        self.__setsGanados = setsGanados

    def setSetsPerdidos(self, setsPerdidos):
        self.__setsPerdidos = setsPerdidos

def main():
    Futbolista = DeportistaFutbol('Falcao', 2073245, 36, 35,'Seleccion Colombia')
    Tennista = DeportistaTennis('nole',45204, 40, 15, 2)
    print(f'Deportista: {Futbolista.getNombre()}\n\
          Documento: {Futbolista.getDocumento()}\n\
          Edad: {Futbolista.getEdad()}\n\
          Cantidad de goles: {Futbolista.getgolesAnotados()}\n\
          Nombre del equipo: {Futbolista.getnombreEquipo()}')
    print(f'Deportista: {Tennista.getNombre()}\n\
          Documento: {Tennista.getDocumento()}\n\
          Edad: {Tennista.getEdad()}\n\
          Cantidad de goles: {Tennista.getSetsGanados()}\n\
          Nombre del equipo: {Tennista.getSetsPerdidos()}')


if __name__ == '__main__':
    main()