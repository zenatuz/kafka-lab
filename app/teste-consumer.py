# from kafka import KafkaConsumer,TopicPartition
# consumer = KafkaConsumer(bootstrap_servers='kafka:9092')

# consumer.assign([TopicPartition('sample', 0)])

# for message in consumer:
#     print (message)

from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

consumer = KafkaConsumer(
    'numtest',
     bootstrap_servers=['kafka:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

client = MongoClient('localhost:27017')
collection = client.numtest.numtest

for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))