from kafka import KafkaProducer
from faker import Faker
import json
import time

fake = Faker()

producer = KafkaProducer(
    bootstrap_servers=['kafka1:9092', 'kafka2:9093', 'kafka3:9094'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_event():
    return {
        'user_id': fake.uuid4(),
        'event_time': fake.iso8601(),
        'event_type': fake.random_element(elements=('click', 'view', 'purchase')),
        'product_id': fake.uuid4(),
        'price': round(fake.random_number(digits=2), 2)
    }

if __name__ == "__main__":
    while True:
        event = generate_event()
        producer.send('events', event)
        print(f"Pushed event: {event}")
        time.sleep(1)
