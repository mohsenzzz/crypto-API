#pip install requests , use for send request get,post,put,delete
#also we can use urllib but requests is easier than urllib
import requests

#json package use for json data , convert string to json and json to string by loads and dumps
import json
#add base url and api_key to config file
from config import url


#get data from fixer api and change json string to dictionary object and return it
def get_response(url:str):
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None

#get filename like timestamp and rates and convert rates to json string and then write to new file
def archive(filename:str, rates):
    with open(f'archive/{filename}.json', 'r+w') as f:
        f.write(json.dumps(rates))




if __name__ == '__main__':
    res = get_response(url)
    archive(res['timestamp'],res['rates'])
