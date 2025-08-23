#For configure first time your credentials type this: aws configure 
import os
try:
    s = os.popen('aws ecr get-login-password')
    l = s.read()
    login = f"docker login --username AWS --password { l.strip() } 205467237791.dkr.ecr.us-west-2.amazonaws.com"
    res = os.popen(login)
    print(res.read())
except Exception as e:
    print(e)
