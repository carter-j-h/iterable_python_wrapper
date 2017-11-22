import csv
from faker import Faker
import json
import requests
import time

# import class from other file
from iterable_wrapper import IterableAPI

# Iterable Instance Credentials 
API_KEY = "94c3333a8e224b32b93a40788d1927cc"


class DataGeneration(IterableAPI):
	"""docstring for DataGeneration"""
	def __init__(self, users=0, events=0):
		
		IterableAPI.__init__(self, api_key=API_KEY)
		self.users = users
		self.events = events


	def generate_users(self):
		# initiate Faker
		fake=Faker()

		for i in range(0,self.users):
			i = fake.profile()

			email = str(i["mail"])

			i.pop("mail")
			i.pop("current_location")

		return self.update_user(email=email, data_fields=i, user_id=None, merge_nested_objects=None)

	def generate_events(self):

		fake=Faker()

		for i in range(0, self.events):

	


data = DataGeneration(users=1, events=0)

print(data.generate_users())






