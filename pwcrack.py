import sys
import getopt
from binascii import hexlify
from hashlib import sha256
import base64
import uuid
import hashlib
import time


def main(argv):
    with open(sys.argv[2], 'r') as r:
        hash = r.readlines()
        hashGiven = hash[0]

    saltGiven = parse_salt_and_password(hashGiven)[0]


    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

        # c = 0
        wordList = []
        # t0= time.perf_counter()
        for passwordLines in lines:
            wordList.append(passwordLines.strip('\n'))

    for words in wordList:
        # c=c+1
        # print(c)

        salt = saltGiven
        salt = salt.encode('utf-8')
        hashed_pword = hash_pword(salt, words.strip())

        saltHash = salt.decode('utf-8') + '$' + hashed_pword

        
            
        if(saltHash.strip() == hashGiven.strip()):
            print("FOUND PASSWORD")
            print(words.strip())
            # t1 = time.perf_counter() - t0
            # guessesPerSecond = c/t1
            # print("Guesses Per Second: "+str(guessesPerSecond))
            exit()

        if(check_password(hashGiven.strip(), saltHash.strip())):
            print("CHECK PASSWORD "+str(check_password(hashGiven.strip(), saltHash.strip())))


        # c=c+1
            
        
    f.close()


def generate_salt(length, debug=True):
    import random

    return hexlify(random.randint(0, 2**length-1).to_bytes(length, byteorder='big'))
    return base64.urlsafe_b64encode(uuid.uuid4().bytes)

def hash_pword(salt, pword):
    assert(salt is not None and pword is not None)
    hasher = sha256()
    hasher.update(salt)
    hasher.update(pword.encode('utf-8'))
    return hasher.hexdigest()
    return hashlib.sha512()

def parse_salt_and_password(originalHash):
    return originalHash.split('$')

def check_password(originalHash, password): 

    newOrigional = originalHash.split('$')
    newPassword = password.split('$')

    if newOrigional[1] == newPassword[1] and newOrigional[0 == newPassword[0]]:
        return True
    return False
            

if __name__ == "__main__":
    main(sys.argv[1:])


