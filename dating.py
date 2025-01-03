from datetime import datetime
import uuid

class User:
    def __init__(self, name, age, gender, bio, interests):
        self.id = str(uuid.uuid4())
        self.name = name
        self.age = age
        self.gender = gender
        self.bio = bio
        self.interests = interests
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.liked_users = []
        self.matches = []

class DatingApp:
    def __init__(self):
        self.users = {}
    
    def register_user(self, name, age, gender, bio, interests):
        user = User(name, age, gender, bio, interests)
        self.users[user.id] = user
        return user.id

    def get_potential_matches(self, user_id):
        user = self.users.get(user_id)
        if not user:
            return []

        # Basic matching logic - exclude already liked users and self
        potential_matches = [
            u for u in self.users.values()
            if u.id != user_id 
            and u.id not in user.liked_users
        ]
        return potential_matches

    def like_user(self, user_id, liked_user_id):
        user = self.users.get(user_id)
        liked_user = self.users.get(liked_user_id)

        if not user or not liked_user:
            return False

        user.liked_users.append(liked_user_id)

        # Check if this creates a match
        if user_id in liked_user.liked_users:
            user.matches.append(liked_user_id)
            liked_user.matches.append(user_id)
            return True
        return False


# Example usage:
def main():
    app = DatingApp()

    # Register some users
    alice_id = app.register_user("Alice", 25, "female", "I love hiking and yoga", ["hiking", "yoga"])
    bob_id = app.register_user("Bob", 30, "male", "I enjoy reading and playing the guitar", ["reading", "guitar"])

    # Get potential matches for Alice
    matches = app.get_potential_matches(alice_id)

    # Alice likes Bob
    if app.like_user(alice_id, bob_id):
        print("It's a match!")
    else:
        print("No match yet!")

if __name__ == "__main__":
    main()

