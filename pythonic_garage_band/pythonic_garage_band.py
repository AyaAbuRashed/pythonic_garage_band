from abc import abstractmethod
class Band():

 band_array = []
 def __init__(self,name):
        self.name = name
        Band.band_array.append(self)

 member_arr = []
 def add_members(self,member_name):
        self.member_name = member_name
        Band.member_arr.append(self.member_name)

 def play_solos(self):
        solos = ''
        for i in Band.member_arr:
            solos+= f'{i.play_solos()}\n'
        return solos
    
 @classmethod
 def to_list(cls):
        return (cls.member_arr)

 def __repr__(self):
        return (f"{self.name}")
    
 def __str__(self):
        return (f"{self.name}")

class Musician():


    def __init__(self,name):
        self.name = name

    @abstractmethod
    def __str__(self):
        return f"Hello Musician {self.name}"

    @abstractmethod
    def __repr__(self):
        return f" '{self.name}' "

    def play_solo(self):
        return f'Welcome Musician {self.name} you can Play solo'

class Guitarist(Musician):

    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return 'guitar'

class Bassist(Musician):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return 'bass'

class Drummer(Musician):
    def __init__(self,name):
        super().__init__(name)

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return 'drums'

if __name__ == "__main__":
  Aya = Guitarist('Aya')
  print(Aya.name)
  BTS = Band('BTS')
  BTS.add_members('SUGA')
  BTS.add_members('JINNE')
  print(BTS.__repr__())

 