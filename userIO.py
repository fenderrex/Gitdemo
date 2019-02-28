import time
from pymongo import MongoClient
client = MongoClient()
db = client.hackMerced2019


class IO:
	def __init__(self,io={"null":True}):
		self.expire=time.time()+259200
		self.io=io
	def __getItem__(self,key):
		return {"service Expire":self.time,"token":self.io[key]}
	def __str__(self):
		print(type(self.io.items())
		s=[]
		for k,v in self.io.items():
			s.append("{'%s':'%s'}"%(k,v))
		return s	
class InputsAndOutputs:
	def __init__(self):
		pass
	def __iter__(self):
		return self
	def next(self):
		result=db.find({ "token": { "$exists": True } })
		print(len(result))
		demo=IO(result)
