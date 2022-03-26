import json
import requests

def lambda_handler(event, context):
    print("Received event: "+json.dumps(event, indent=2))

    body = json.dumps({
        "notification":event['notification'],
        "accessCode":event['access_code']})

    requests.post(url=event['alexa_notification_api'], data=body)