# HW start: 
# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year 
#     def print_info(self):
#         print(f"{self.year} {self.make} {self.model}")

# car = Vehicle("Nissan", "Leaf", "2015")
# car.print_info()

# class Person:
#     def __init__(self, name, email, phone):
#         self.name = name
#         self.email = email
#         self.phone = phone
#         self.friends = []
#         self.greeting_count = 0
#         self.unique_greetings = 0
#     def greeting(self, other_person):
#         print(f"Hello {other_person.name}, I am {self.name}!")
#         self.greeting_count += 1
#     def print_contact_info(self):
#         print(f"{self.name}\'s email: {self.email}\n{self.name}\'s phone number: {self.phone}")
#     def add_friend(self, friend_name):
#         self.friends.append(friend_name)
#         print(self.friends)
#     def num_friends(self):
#         print("Number of friends: ", len(self.friends))
#     def __str__(self):
#         return "Person: {} {} {}".format(self.name, self.email, self.phone)

# sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
# jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
# sonny.add_friend("Jordan")
# sonny.num_friends()
# print(sonny)