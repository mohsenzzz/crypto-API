from gc import enable

BASE_URL = 'http://data.fixer.io/api/latest?access_key='
API_KEY = '19d608b57c5fc4981920b0b510b02b11'

url = BASE_URL+API_KEY

rules ={
    'email':{
        'enable': False,
        'preferred': {
            'BTC':['BTC',"USD",'IRR',"ETC",'CAD','AED']
        }
    },
    'sms':{
        'enable':True,
        'preferred': {
            'BTC':{'min':1.6113625e-05, 'max':1.6113629e-05},
            'USD':{'min':1.079969,'max':1.079971}
        }
    }
}