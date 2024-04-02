class Ficha:
    def __init__(self, x, y,angulo,editando,nombre,vida):
        self.x=x
        self.y=y
        self.angulo=angulo
        self.editando=editando
        self.nombre=nombre
        self.vida=vida
    def serializar(self,obj):
        if isinstance(obj, Ficha):
            return {'x': obj.x, 
            'y':obj.y,
            'angulo':obj.angulo,
            'editando':obj.editando,
            'nombre':obj.nombre,
            'vida':obj.vida
            }
        else:
            raise TypeError("Object of type 'MiObjeto' is not JSON serializable")


class Fijo(Ficha):
    def __init__(self,tipo,*args):
        super().__init__(*args)
        self.tipo=tipo

class Jugador(Ficha):
    def __init__(self,energia,punteria,municiones,minas,lamparas, animacion,*args):
        super().__init__(*args)
        self.energia=energia
        self.punteria=punteria
        self.municiones=municiones
        self.minas=minas
        self.lamparas=lamparas
        self.animacion=animacion

class JugadorAzul(Jugador):
    def __init__(self,*args):
        super().__init__(*args)

class JugadorRojo(Jugador):
    def __init__(self,*args):
        super().__init__(*args)

#pepe= JugadorAzul(100,100,15,5,5,True,0,0,0,True,"Pepe",5)

#print (pepe)
#print (pepe.__class__.__name__)
#for key, value in pepe.__dict__.items():
 #       print(f"{key}: {value}")


#regalo=Fijo("Pared",0,0,0,False,"Pared",5)
#for key, value in regalo.__dict__.items():
 #       print(f"{key}: {value}")
