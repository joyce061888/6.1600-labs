import os

def attack_one(guess):
    secret = os.urandom(256)
    while not guess(secret):
        secret = os.urandom(256)
    return secret

def attack_two():
    return b''

def attack_three():
    return b''

def attack_four():
    return b''
