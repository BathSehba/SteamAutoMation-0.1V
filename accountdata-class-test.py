class accountdata(object):
	def __init__(self, username, password):
		self.username = username
		self.password = password


user1 = accountdata("element", "1234password")
user2 = accountdata("funnyguys", "24343password")

print(user1.username)
print(user2.password)
