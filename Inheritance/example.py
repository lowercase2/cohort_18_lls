class Fish():
    def __init__(self, first_name, last_name="Fish", skeleton="bone",eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming")

    def swim_backwards(self):
        print("The fish can swim backwards")


class Trout(Fish):
    def __init__(self, water = "freshwater"):
        super().__init__(self)
        self.water = water

    def swim(self):
        super().swim()
        print("Hey the trout is swimming")


# bubbles = Trout()
# bubbles.first_name = "bubbles"
# print(bubbles.first_name)
# print(bubbles.last_name)
# print(bubbles.water)
# bubbles.swim()
# class Animal:
#     pass

nemo = Trout("nemo")
# print(nemo.first_name + " " + nemo.last_name)
# print(nemo.skeleton)
# print(nemo.eyelids)
# nemo.swim()
# nemo.swim_backwards()

# print(type(nemo))
# print(isinstance(nemo, Fish))
# print(isinstance(nemo, Trout))
# print(issubclass(Animal, Fish))

class Clownfish(Fish):

    def live_with_anemone(self):
        print("They live with anemone")

terry = Clownfish("Terry")
# print(terry.first_name + " " + terry.last_name)
# terry.live_with_anemone()

class Shark(Fish):
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim_backwards(self):
        print("Sharks cannot swim backwards, they sink backwards")

# bull = Shark("bull")
# print(bull.first_name + " " + bull.last_name)
# bull.swim()
# bull.swim_backwards()
# print(bull.skeleton)
# print(bull.eyelids)

class Coral:
    def __init__(self, first_name= "barrier", last_name="coral"):
        self.first_name = first_name
        self.last_name = last_name

    def community(self):
        print("coral live in a community")

class Anemone(Coral):
    def __init__(self, last_name="Anemone"):
        self.last_name = last_name
        super().__init__(self)


    def protect_clownfish(self):
        print("The anemone protect clownfish")


class Coralreef(Anemone):

    def __init__(self, age = 100):
        self.age = age
        super().__init__()
    
new = Coralreef()
new.community()
new.protect_clownfish()
print(new.age)
print(new.first_name)
print(new.last_name)

print(dir(new))
print(dir(Coralreef))