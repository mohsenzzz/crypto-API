from kavenegar import *

api = KavenegarAPI('2F2B647978784631324C39302F6634662F586F70376A694453564A6F5178523167544A4A484D7A436953343D')
def send_notification(message):
    try:
        params = {
            'sender': '1000689696',
            'receiver': '<phoneNumber>',
            'message': message,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
           print(e)
    except HTTPException as e:
        print(e)