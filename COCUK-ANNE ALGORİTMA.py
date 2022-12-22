class Anne:#ana class
    Aozellik=100
    def __init__(self):
        print("anne init yazdı")

    def Annemethod(self):
        print("Anne method yazdı")

    def setAnne(self,ozellik):
        Anne.Aozellik=ozellik

    def getAnne(self):
        print("Anne özellik:",Anne.Aozellik)

class Cocuk(Anne): #çocuk class
    def __init__(self):
        print("çocuk init yazdı")

    def Cocukmethod(self):
        print("Çocuk method yazdı")

    def Annemethod(self):
        print("Anne değil çocuk")


        
        
