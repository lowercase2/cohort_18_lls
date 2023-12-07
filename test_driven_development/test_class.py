import unittest
from model import Person


class my_test(unittest.TestCase):

    person = Person()
    user_name =[]
    user_id = []

    def test_0_set_name(self):
        print("**starting set name test**")

        for i in range(10):
            # Generating names
            name = "Name" + str(i)
            #store generated names in a list
            self.user_name.append(name)
            # Get user_id generated from set_name function
            user_id = self.person.set_name(name)
            # checking if obtained user id is not None or Null
            self.assertIsNotNone(user_id)
            # store user_id in our list
            self.user_id.append(user_id)
        print("User id length= ", len(self.user_name))
        print(self.user_id)
        print("User name length= ",len(self.user_name))
        print(self.user_name)

        print("**End of set_name test**")
        
    def test_1_get_name(self):
        print("**Starting get name tests**")

        length = len(self.user_id)
        print("User_name length= ", length)

        for i in range(15):
            if i < length:
                self.assertEqual(self.user_name[i], self.person.get_name(self.user_id[i]))
            else:
                print("Test for no user found")
                self.assertEqual("No user found in class", self.person.get_name(i))

        print("**Finish get_name test**")




