import os
import inspect
import hashlib

def attack_one(guess):
    stack = inspect.stack()
    for frame_info in stack:
        # print("\nframe info: ", frame_info)
        locals_dict = frame_info.frame.f_locals
        # print("\nlocals dict: ", locals_dict)
        if 'secret' in locals_dict:
            if guess(locals_dict['secret']):
                print('\n*****attack one: secret found*****\n')
                return locals_dict['secret']

def attack_two():
    stack = inspect.stack()
    for frame_info in stack:
        # print("\nframe info: ", frame_info)
        locals_dict = frame_info.frame.f_locals
        # print("\nlocals dict: ", locals_dict)
        if 'secret' in locals_dict:
            return locals_dict['secret']
        
def set_urandom_override(value):
    def urandom_override(size):
        return value[:size]
    os.urandom = urandom_override

def attack_three():
    # secret is chosen after this function guesses
    overridden_secret = b'secretpwd'
    set_urandom_override(overridden_secret)
    secret = os.urandom(256)
    print("attack 3 secret: ", secret)
    return secret
    
class SecretStore:
    def __init__(self, secret):
        self.secret = secret

    def get_secret(self):
        return self.secret
    
def attack_four():
   pass
