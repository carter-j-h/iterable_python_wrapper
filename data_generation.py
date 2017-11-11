from faker import Faker

fake=Faker()


class DataGeneration(object):
	"""docstring for DataGeneration"""
	def __init__(self, users=0, events=0):
		

		self.users = users
		self.events = events


	def generate_users(self):
		container = []

		for i in range(0,self.users):
			i = fake.profile()

			email = i["mail"]

			i.pop("mail")

			person = {}

			person["email"]= email
			person["dataFields"]= i
			
			
			container.append(person)

		print(container, "\nYou have "+str(len(container)) + " users generated")


data = DataGeneration(users=10, events=0)

data.generate_users()




