from faker import Faker

fake=Faker()


class DataGeneration(object):
	"""docstring for DataGeneration"""
	def __init__(self, users, events):
		
		self.users = users
		self.events = events


	def generate_users(self):
		users=[]

		for i in range(0,self.users):
			i = fake.profile()
			
			users.append(i)

		print(len(users))




