import requests
import hashlib
import  getpass

RED = '\033[91m'
GREEN = '\033[92m'
ENDC = '\033[0m'

def request_api_data(hached):
    url = 'https://api.pwnedpasswords.com/range/' + hached
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Eroor fetching: {res.status_code}, check the api and try again')
    return res

def get_leaks_count(hashes, hashed_to_check):
    hash = (line.split(':') for line in (hashes.text.splitlines()))
    for h, count in hash:
        if (h == hashed_to_check):
            return int(count)
    return 0
    

def pwned_api_checker(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    fist_part, second_pat = sha1password[:5], sha1password[5:]
    respond = request_api_data(fist_part)
    count = get_leaks_count(respond, second_pat)
    if count :
     print(f"{RED}Weak password({password}): This password has been found {count} times in data breaches. Change it immediately!{ENDC}")
    else:
        print(f"{GREEN}Strong password({password}): This password has not been found in any known data breaches. Keep up the good work!{ENDC}")

def main():
    while (True):
        user_input = getpass.getpass("Enter the password to check (type EXIT to quit): ")
        if user_input.upper() == 'EXIT':
            break
        if not user_input.strip(): 
            print("No password entered. Please try again.")
            continue
        pwned_api_checker(user_input)
    return 0

if __name__ == '__main__':
    main()
