
class Person:

    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if user_id >= len(self.name):
            return "No user found"
        else:
            return self.name[user_id]
        
# person = Person()
# print(person.set_name("John"))
# print(person.set_name("Jake"))
# print(person.set_name("Jared"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Robert"))
# print(person.set_name("Jimy"))
# print(person.set_name("Jmmy"))
# print(person.set_name("immy"))
# print(person.set_name("Jim"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Jimmy"))
# print(person.set_name("Reubem"))
# print(person.set_name("Jimmy"))
# print(person.get_name(0))
# print(person.get_name(1))
# print(person.get_name(2))
# print(person.get_name(3))
# print(person.get_name(4))
# print(person.get_name(5))
# print(person.get_name(6))
# print(person.get_name(7))

