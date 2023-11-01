
class AttackTamper:
    def __init__(self, compress):
        # compress is set for the last extra credit part
        self.compress = compress
        self.bytes = 0

    def handle_data(self, data):
        # Your attack here.
        return data

def attack_decrypt(client_fn):
    # Your attack here.

    # instructs ssh client to send evil + secret to ssh server
    # (num of bytes sent to server, bytes received from server)
    (bytes_out, bytes_in) = client_fn("prefix string") 

    return "your guess of secret string"

# import logging

# logging.basicConfig()
# logging.getLogger("paramiko").setLevel(logging.DEBUG)

# def attack_decrypt(client_fn):
#     # Initialize the baseline "evil string."
#     base_evil = '{"city0":"A","city1":"A","city2":"A"}'
#     base_len_in_bytes = len(base_evil.encode())
#     secret = ""

#     while len(secret) < len(base_evil):
#         for char in range(256):
#             # add char to "evil string" 
#             evil_string = base_evil + chr(char)
#             # record the bytes sent and received for evil string with added char
#             bytes_out, bytes_in = client_fn(evil_string)

#             # get diff from the base len
#             diff = bytes_out - base_len_in_bytes

#             # if diff is not 1 it means the added char was part of the secret
#             if diff != 1:
#                 secret += chr(char)
#                 base_evil = base_evil + chr(char)
#                 break
        
#     print("secret: ", secret)
#     return secret



