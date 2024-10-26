#pip install requests , use for send request get,post,put,delete
#also we can use urllib but requests is easier than urllib
from time import strftime

import requests
#pip install khayyam, use for get jalalidate and convert datetime to jalalidate
from khayyam import JalaliDatetime
from datetime import datetime

#json package use for json data , convert string to json and json to string by loads and dumps
import json
#add base url and api_key to config file
from config import url,rules

from mail import send_smtp_mail
from sms import send_notification



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
    now = datetime.now()
    jalaliDate = JalaliDatetime(now),strftime('%Y-%B-%d %A %H:%M')
    subject = f'{jalaliDate} - crypto'

    if rules['email']['preferred'] is not None:

        tmp = dict()
        for exe in rules['email']['preferred']:
            tmp[exe] = rates[exe]
        rates= tmp

    body = json.dumps(rates)
    send_smtp_mail(subject, body)

def send_sms(rates):
    preferred = rules['sms']['preferred']
    msg = None
    now = datetime.now()
    jalaliDate = JalaliDatetime(now), strftime('%Y-%B-%d %A %H:%M')
    for exe in preferred.keys():
        if rates[exe] <= preferred[exe]['min'] :
            msg = f'{exe} reached min: {rates[exe]} \n'
        if rates[exe] >= preferred[exe]['max']:
            msg = f'{exe} reached max: {rates[exe]} \n'
    print("msg is :" + msg)
    if msg is not None:
        msg += jalaliDate
        send_notification(msg)

if __name__ == '__main__':
    res = get_response(url)
    archive(res['timestamp'],res['rates'])
    if rules['email']['enable']:
        send_email(res['rates'])
    if rules['sms']['enable']:
        send_sms(res['rates'])

