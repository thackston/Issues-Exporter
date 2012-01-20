import requests
import csv
import json
import getpass

user = raw_input("What is your Github username? ")
password = getpass.getpass(prompt = "What is your password? ")
org = raw_input("What organization are you querying? ")
repo = raw_input("And which repo? ")
base_url = 'https://api.github.com/repos/'
creds = (user, password)
headers = {'content-type': 'application/vnd.github.v3.full+json'}



def get_issues():
    whole_url = base_url + org + '/' + repo + '/issues?per_page=1000'
    print whole_url
    issues = requests.get('%s'% whole_url, auth = creds, headers = headers) 
    return issues.content


data = json.loads(issues)

titles = [
        'id',
        'title',
        'body',
        'state',
        'creator',
        'labels',
        'created_at',
        'updated_at',
        'closed_at',
    ]

target = csv.writer(open('test.csv','wb+'))

target.writerow(titles)
    


for item in data:
    label = []
    for l in item['labels']:
        label.append(l['name'])
        
    issue = [
            item['number'],
            item['title'].encode('utf8'),
            item['body'].encode('utf8'),
            item['state'], 
            item['user']['login'],
            ", ".join(label) ,
            item['created_at'],
            item['updated_at'],
            item['closed_at']
             
           
        ]
    target.writerow(issue)



    
    

