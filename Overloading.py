class Vektör:
    def __init__(self,vx,vy):
        self.x=vx
        self.y=vy

    def __str__(self):
        return "vektör (%d %d)"%(self.x,self.y)

    def __add__(self,yeni):
        return Vektör(self.x+yeni.x,self.y+yeni.y)
