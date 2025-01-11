class User:

    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.follower = 0
        self.following = 0
    def follow(self, user_id):
        user_id.follower += 1
        self.following +=1

user_1 = User("001", "Angela")
user_2 = User("001", "Angela")

print(user_1.follower)
user_1.follow(user_2)
print(user_1.user_id)
print(user_1.follower)
print("I'm just testing this bitches")