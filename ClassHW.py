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
#         self.people_greeted = []
#     def greeting(self, other_person):
#         print(f"Hello {other_person.name}, I am {self.name}!")
#         self.greeting_count += 1
#         if other_person.name not in self.people_greeted:
#             self.people_greeted.append(other_person.name)
#     def num_unique_people_greeted(self):
#         print(len(self.people_greeted))
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
# dee_ann = Person("Dee-Ann", "dee@aol.com", "713-405-5678")
# sonny.add_friend("Jordan")
# sonny.num_friends()
# print(sonny)
# sonny.num_unique_people_greeted()
# sonny.greeting(jordan)
# sonny.num_unique_people_greeted()
# sonny.greeting(jordan)
# sonny.num_unique_people_greeted()
# sonny.greeting(dee_ann)
# sonny.num_unique_people_greeted()