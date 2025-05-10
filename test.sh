#!/bin/bash
# Super basic hacky test script
echo "Expected output:
<p>Hello, World!</p>
Logout successful
Login required
Not logged in. I dont know you!
Invalid username or password
Login success
Logged in as bob
<p>Secret area!</p>
Logout successful
"
echo "Test time!:"
# set -x
curl localhost:5000/
curl -b cookie.txt -c cookie.txt localhost:5000/auth/logout
curl -b cookie.txt -c cookie.txt localhost:5000/protected
curl -b cookie.txt -c cookie.txt localhost:5000/auth/login
curl -b cookie.txt -c cookie.txt localhost:5000/auth/login -d "username=a&password=a"
curl -b cookie.txt -c cookie.txt localhost:5000/auth/login -d "username=bob&password=secret"
curl -b cookie.txt -c cookie.txt localhost:5000/auth/login
curl -b cookie.txt -c cookie.txt localhost:5000/protected
curl -b cookie.txt -c cookie.txt localhost:5000/auth/logout



