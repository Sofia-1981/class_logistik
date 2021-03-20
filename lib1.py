class AVTO():
    def __init__(self, marka, gruzopod, free=True):
        self.marka=marka
        self.gruzopod=gruzopod
        self.free=free

    def tonna(self, tonn):
        if self.gruzopod<= tonn:
            return True
        else:
            return False

    def frees(self):
        if self.free:
            return True
        else:
            return False


class GARAZH ():
    garaze={ }
    def __init__(self, name, number_place):
        self.name=name
        self.number_place=number_place

    def add_to_garaze (self,name, avto):
        self.garaze[name]=avto

    def chek_free(self):
        for name,car in self.garaze.items():
            if car.free:
                print(name, 'свободен')
            else:
                print(name, "не свободен")






