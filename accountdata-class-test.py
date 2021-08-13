class accountdata(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password


user1 = accountdata("element", "1234password")
user2 = accountdata("funnyguys", "24343password")

print(user1.username)
print(user2.password)





class accountdata(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password


user1 = accountdata("element", "1234password")
user2 = accountdata("funnyguys", "24343password")

uid = input('enter')
if uid in user1.username:
	print('already found')
else:
	print('will add')
	
	
	Above will check to see if info is in userdata
