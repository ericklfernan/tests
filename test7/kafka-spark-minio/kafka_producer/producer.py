from kafka import KafkaProducer
from faker import Faker
import json
import time

producer = KafkaProducer(
    bootstrap_servers=['kafka:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

faker = Faker()

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
