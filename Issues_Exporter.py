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
    response = requests.get('%s'% whole_url, auth = creds, headers = headers) 
    return response.content

issues = json.loads(get_issues())

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

csv_file = csv.writer(open('test.csv','wb+'))

csv_file.writerow(titles)
    
for issue in issues:
    label = []
    for l in issue['labels']:
        label.append(l['name'])
   
    row = [
            issue['number'],
            issue['title'].encode('utf8'),
            issue['body'].encode('utf8'),
            issue['state'], 
            issue['user']['login'],
            ", ".join(label) ,
            issue['created_at'],
            issue['updated_at'],
            issue['closed_at']
             
           
        ]

    csv_file.writerow(row)



    
    

