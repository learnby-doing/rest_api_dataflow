import time
import apache_beam as beam
from google.cloud import pubsub_v1
import os
from concurrent.futures import TimeoutError

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\\Users\\ASHISH\\Downloads\\dhamu-gcp-learn-pubsub.json'
project_id = 'dhamu-gcp-learn'
subscription_id = 'projects/dhamu-gcp-learn/subscriptions/first_subs'

def callback(message):
    print(f'Fomatting message:{message}')
    message.ack()

subscriber_path = subscription_id

subscriber = pubsub_v1.SubscriberClient()

subscriber.subscribe(subscriber_path, callback=callback)

while True:
    time.sleep(60)
