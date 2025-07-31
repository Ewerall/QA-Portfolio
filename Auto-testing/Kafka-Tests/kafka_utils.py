from kafka import KafkaProducer, KafkaConsumer
import time
import json

def create_producer():
    return KafkaProducer(
        bootstrap_servers='localhost:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

def create_consumer(topic, group_id):
    return KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092', #cluster adress
        group_id=group_id,
        auto_offset_reset='earliest', #need to read from topic earliest
        value_deserializer=lambda x: json.loads(x.decode('utf-8')) #auto serialization in sjon
    )

def send_event(producer, topic, event):
    producer.send(topic, event)
    producer.flush() #event from buffer

def consume_event(consumer, timeout=10):
    start_time = time.time()
    while time.time() - start_time < timeout: #timeout 10 sec
        records = consumer.poll(timeout_ms=1000, max_records=1) #only 1 message with timeout 1 sec
        
        for topic_partition, messages in records.items():
            if messages:
                return messages[0].value
        
        # check timeout
        if time.time() - start_time >= timeout:
            return None
    
    return None