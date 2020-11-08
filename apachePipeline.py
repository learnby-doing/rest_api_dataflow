import apache_beam as beam

import time
import apache_beam as beam
from google.cloud import pubsub_v1
import os


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\\Users\\ASHISH\\Downloads\\dhamu-gcp-learn-pubsub.json'
project_id = 'dhamu-gcp-learn'
subscription_id = 'projects/dhamu-gcp-learn/subscriptions/first_subs'

publisher = pubsub_v1.PublisherClient()

topic_path = 'projects/dhamu-gcp-learn/topics/second_topic'

options = PipelineOptions()
options.view_as(StandardOptions).streaming = True

p = beam.Pipeline(options=options)

def print_func(elem):
    print('printing function returns values')
    print(elem)
    return elem
writeToPubsub = (
    p
    | 'read from Pubsub' >> beam.io.ReadFromPubSub(subscription=subscription_id)
    #| beam.Create([1,2,3,4])
    | beam.Map(print_func)
    | beam.io.WriteToPubSub(topic_path)
)

result = p.run()
result.wait_until_finish()
