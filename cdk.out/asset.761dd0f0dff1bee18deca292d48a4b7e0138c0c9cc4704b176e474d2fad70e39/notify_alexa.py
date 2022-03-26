import json
import requests

def lambda_handler(event, context):
    message=json.loads(event['Records'][0]['Sns']['Message'])

    body = json.dumps({
        "notification":json.dumps(message),
        "accessCode":"amzn1.ask.account.AEKA2MKAMLAVESKRGP64A4F7ASWEZBKKAH2Q4R6XDOQRVY5OXFWTZBDK5IF4VUWSMMYYHKWUTXZIGTP2L5RAAE4VS2ICTERFQ3YREO7YMAT22O5VVQQVQEIU2GDRSXLF6JWUJLZNJB7EWPPHXVSXIJTP4YZNWYCJDUQOF4267BFRDXLWTYBA2DEOQ55CPIYLG43A46ZJFGIEDJY"})

    requests.post(url='https://api.notifymyecho.com/v1/NotifyMe', data=body)