import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")

# Initialize the default app
firebase_admin.initialize_app(cred, options={
    'databaseURL': 'https://safeandsmartdb-default-rtdb.firebaseio.com/'
})

class User:
    def __init__(self, user_id, name, phone):
        self.user_id = user_id
        self.name = name
        self.phone = phone

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone
        }

    @staticmethod
    def from_dict(user_id, data):
        name = data.get('name')
        phone = data.get('phone')
        return User(user_id, name, phone)

    def save(self):
        ref = db.reference('SafeAndSmart/Users')
        user_ref = ref.child(self.user_id)
        user_ref.set(self.to_dict())

    @staticmethod
    def load(user_id):
        ref = db.reference('SafeAndSmart/Users')
        user_ref = ref.child(user_id)
        data = user_ref.get()
        if data:
            return User.from_dict(user_id, data)
        else:
            return None

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_phone(self):
        return self.phone

    def set_phone(self, phone):
        self.phone = phone

    def update_field(self, field_name, new_data):
        if field_name == 'name':
            self.set_name(new_data)
        elif field_name == 'phone':
            self.set_phone(new_data)
        else:
            print(f"Field '{field_name}' does not exist.")

# # Example usage
# user1 = User('User1', 'Dvir', '0527025480')
# user2 = User('User2', 'Dvir', '05270254802342')
# user3 = User('User3', 'Dvir', '05270254801')
# user4 = User('User4', 'Dvir', '0527025480222')
# user5 = User('User5', 'Dvir', '0527025480444')

# # Save user1 to the database
# user1.save()
# user2.save()
# user3.save()
# user4.save()
# user5.save()

# # Load user1 from the database
# loaded_user1 = User.load('User1')
# loaded_user2 = User.load('User2')
# loaded_user3 = User.load('User3')
# loaded_user4 = User.load('User4')
# loaded_user5 = User.load('User5')

# # Access and modify user1's name and phone
# print(loaded_user1.get_name())  # Output: 'Dvir'
# print(loaded_user1.get_phone())  # Output: '0527025480'

# # Update only the 'name' field
# loaded_user1.update_field('name', 'John')

# # Save the updated user1 to the database
# loaded_user1.save()

# # Load the updated user1 from the database
# updated_user1 = User.load('User1')

# # Access and print the updated name
# print(updated_user1.get_name())  # Output: 'John'


# ####################

# # Update only the 'name' field
# loaded_user2.update_field('name', 'shaul')

# # Save the updated user1 to the database
# loaded_user2.save()

# # Load the updated user1 from the database
# updated_user2 = User.load('User2')

# # Access and print the updated name
# print(updated_user2.get_name())  # Output: 'John'



