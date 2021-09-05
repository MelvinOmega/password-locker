class User:
    '''
    Generates user details.
    '''

    user_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        This is for saving a new user to the user_list.
        '''
        User.user_list.append(self)




