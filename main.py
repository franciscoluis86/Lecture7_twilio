import base64
import os
from twilio.rest import Client
source_number=''
destination_numbers=['+14386869856','+14386869856','+14386869856']
def twilio_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
 
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    for each_destination_number in destination_numbers:
          message = client.messages.create(
                                        body='Message from twillo Francisco pubsub : ' +pubsub_message,
                                        from_=source_number,
                                        to=each_destination_number
                                   )
 
    print(message.sid)
