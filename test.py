import json
import requests
from io import StringIO
import sys
from requests.models import Response

def getHosts():
    f = open("servers.txt", "r").readlines() #we open the server.txt file, {you must change the name servers.txt to the path of your file servers.txt} 
    for x in f: #we loop inside the servers.txt file and collect endpoints
        headers = {
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        response=requests.get(url= "http://{}".format(x), headers=headers) # we get request the endpoints
        if response.status_code== 200: # we check that the endpont is reachable 
            J=json.loads(response.text)
            print("Application : {}, Version : {}, Success_Count : {}".format(J['Application'],J['Version'],J['Success_Count']))
        else:
            print("request bad")
            print(response.status_code)
            return {}

def redirect(): #here we redirect the results from the getHosts method to stdout and out.txt file
    getHosts()
    original_stdout = sys.stdout
    with open('out.txt', 'w') as f: #{you must change the name out.txt to the path of your file out.txt so for {example /root/out.txt}}
            sys.stdout = f
            getHosts()
            sys.stdout = original_stdout

def main(): # here we call the redirect method 
	redirect()
    
    

if __name__ == '__main__':
    main()  # the end result will get request the endpoints present in servers.txt as http request on the terminal and redirect it to the out.txt file