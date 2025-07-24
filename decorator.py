# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': False #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def rap_fun(user):
        if user.get('valid'):
            return fn(user)
        else:
            return print('no access')

    return rap_fun
  # code here

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
