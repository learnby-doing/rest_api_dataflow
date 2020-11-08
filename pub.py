import os
import time
import apache_beam as beam
from google.cloud import pubsub_v1

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'C:\\Users\\ASHISH\\Downloads\\dhamu-gcp-learn-pubsub.json'

publisher = pubsub_v1.PublisherClient()

topic_path = publisher.topic_path('dhamu-gcp-learn', 'first_topic')


futures = dict()

# def get_callback(f, data):
#     def callback(f):
#         try:
#             print(f.result())
#             futures.pop(data)
#         except:
#             print("Please Handle {} for {} ".format(f.exeception(), data))
#     return callback

data_list = ['ashish4','vikas4','virender4']

for i in data_list:
    data = i

    # futures.update({data: None})

    publisher.publish(topic_path, data = data.encode("utf-8"))

    # futures[data] = future
    # future.add_done_callback(get_callback(future,data))

while futures:
    time.sleep(2)

print("Pubslish message with error handeler")
