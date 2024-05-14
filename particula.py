from algoritmos import distancia_euclidiana



class Particula:
    id_actual = 0

    def __init__(self, origen_x, origen_y, destino_x, destino_y, velocidad, red, blue, green, id=None, distancia=None):
        if id is None:
            self.__id = Particula.id_actual
            Particula.id_actual += 1
        else:
            self.__id = id
            Particula.id_actual += 1
        self.__origen_x = origen_x
        self.__origen_y = origen_y
        self.__destino_x = destino_x
        self.__destino_y = destino_y
        self.__velocidad = velocidad
        self.__red = red
        self.__blue = blue
        self.__green = green
        self.__distancia = distancia if distancia is not None else distancia_euclidiana(origen_x, origen_y, destino_x, destino_y)


    def __str__(self):
        return (
                "Id : " + str(self.__id) + "\n" +
                "Origen x: " + str(self.__origen_x) + "\n" +
                "Origen y: " + str(self.__origen_y) + "\n" +
                "Destino x: " + str(self.__destino_x) + "\n" +
                "Destino y: " + str(self.__destino_y) + "\n" +
                "Velocidad: " + str(self.__velocidad) + "\n" +
                "Red: " + str(self.__red) + "\n" +
                "Blue: " + str(self.__blue) + "\n" +
                "Green: " + str(self.__green) + "\n" +
                "Distancia: " + str(self.__distancia) + "\n"
                )
        
    def to_dict(self):
        return{
            "id": self.__id,
            "origen_x": self.__origen_x, 
            "origen_y": self.__origen_y,
            "destino_x": self.__destino_x,
            "destino_y": self.__destino_y,
            "velocidad": self.__velocidad,
            "red": self.__red,
            "blue": self.__blue,
            "green": self.__green,
        }
    
    @property
    def id(self):
         return self.__id
    @property
    def origen_x(self):
         return self.__origen_x
    @property
    def origen_y(self):
         return self.__origen_y
    @property
    def destino_x(self):
         return self.__destino_x
    @property
    def destino_y(self):
         return self.__destino_y
    @property
    def velocidad(self):
         return self.__velocidad
    @property
    def red(self):
         return self.__red
    @property
    def blue(self):
        return self.__blue
    @property
    def green(self):
        return self.__green
    @property
    def distancia(self): 
         return self.__distancia