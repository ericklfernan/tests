from kafka import KafkaProducer
from faker import Faker
import json
import time

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=['kafka1:9092', 'kafka2:9093', 'kafka3:9094'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

faker = Faker()

# Send fake data to Kafka topic
for _ in range(20):
    data = {
        'name': faker.name(),
        'address': faker.address(),
        'created_at': str(faker.date_time())
    }
    producer.send('events', value=data)
    print(f"Sent: {data}")
    time.sleep(1)

producer.flush()
