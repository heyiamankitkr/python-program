from abc import ABC,abstractmethod #import from module
class animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class dog(animal):
    def make_sound(self):
        print("bark")
class cow(animal):
    def make_sound(self):
        print("moo")
d1=dog()
c1=cow()
d1.make_sound()
c1.make_sound()
