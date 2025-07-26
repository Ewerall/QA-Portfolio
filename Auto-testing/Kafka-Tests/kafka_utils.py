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
        bootstrap_servers='localhost:9092',
        group_id=group_id,
        auto_offset_reset='earliest',
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )

def send_event(producer, topic, event):
    producer.send(topic, event)
    producer.flush()

def consume_event(consumer, timeout=10):
    """Получает одно сообщение с таймаутом"""
    start_time = time.time()
    while time.time() - start_time < timeout:
        # Read massages
        records = consumer.poll(timeout_ms=1000, max_records=1)
        
        for topic_partition, messages in records.items():
            if messages:
                return messages[0].value
        
        # Check timeout
        if time.time() - start_time >= timeout:
            return None
    
    return None