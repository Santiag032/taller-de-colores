class DR:
 #ATRIBUTOS
    altura:float=(1,70)
    Peso:float=(87)
    edad:int=(67)
    IQ:int=(120)
    Nombre:str=("Juan")

    #METODOS

    def gafas(self):
        print("Se ha puesto las gafas")
         
    def bata(self):
        print("Se ha puesto la bata de laboratorio")

    def pocion(self):
        print("Ha preparado una medicina")

    def pensar(self):
        print("A pensado en una nueva medicina")

    def escribir(self):
        print("Ha escrito la reseta de una nueva medicina")


d1=DR()
d1.gafas()
d1.bata()
d1.pensar()
d1.escribir()
d1.pocion()

