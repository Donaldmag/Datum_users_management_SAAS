from data.users import USERS

# Find user id for POST new user
def find_proper_user_id(user):
    user.id = 1 if len(USERS) == 0 else USERS[-1].id + 1
    return user