import threading
import logging
import time
import json
from kafka import KafkaConsumer, KafkaProducer

# Set the proper configuration
server='10.10.22.12:9092'
topic='alllooo'

class Producer(threading.Thread):
    daemon = True
    def run(self):
        producer = KafkaProducer(bootstrap_servers=server,
                                 key_serializer=lambda v: json.dumps(v).encode('utf-8'),
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))
        ctd = 0
        while True:
            ctd += 1
            producer.send(topic, key={"atualizacao":"NF"}, value={"dataObjectID": ctd})
            ctd += 1
            producer.send(topic, key={"atualizacao":"XML"}, value={"dataObjectID": ctd})
            time.sleep(1)

class Consumer(threading.Thread):
    daemon = True
    def run(self):
        consumer = KafkaConsumer(bootstrap_servers=server,
                                 auto_offset_reset='earliest',
                                 key_deserializer=lambda m: json.loads(m.decode('utf-8')),
                                 value_deserializer=lambda m: json.loads(m.decode('utf-8')))
        consumer.subscribe([topic])
        for message in consumer:
            print (message.key, message.value)

def main():
    threads = [
        Producer(),
        Consumer()
    ]
    for t in threads:
        t.start()
    time.sleep(10)
if __name__ == "__main__":
    # logging.basicConfig(
    #     format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:' +
    #            '%(levelname)s:%(process)d:%(message)s',
    #     level=logging.INFO
    # )
    main()