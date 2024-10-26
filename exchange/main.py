#pip install requests , use for send request get,post,put,delete
#also we can use urllib but requests is easier than urllib
from datetime import datetime


import requests

#json package use for json data , convert string to json and json to string by loads and dumps
import json
#add base url and api_key to config file
from config import url,rules

from mail import send_smtp_mail



#get data from fixer api and change json string to dictionary object and return it
def get_response(url:str):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None

#get filename like timestamp and rates and convert rates to json string and then write to new file
def archive(filename:str, rates):
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))



def send_email(rates):
    subject = f'{datetime.now()} - crypto'

    if rules['email']['preferred'] is not None:
        print('111111111111111')
        tmp = dict()
        for exe in rules['email']['preferred']:
            tmp[exe] = rates[exe]
        rates= tmp

    body = json.dumps(rates)
    send_smtp_mail(subject, body)



if __name__ == '__main__':
    res = get_response(url)
    archive(res['timestamp'],res['rates'])
    send_email(res['rates'])
