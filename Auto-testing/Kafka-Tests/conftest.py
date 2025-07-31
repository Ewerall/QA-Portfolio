import pytest
from kafka_utils import create_producer, create_consumer
import time


@pytest.fixture(scope="function")
def producer():
	prod = create_producer() #producer send event to topic
	yield prod
	prod.close()  # close producer after tests
	
@pytest.fixture(scope="function")
def order_consumer():
	consumer = create_consumer("orders", f"test_group_{time.time()}") #unique id for every test
	yield consumer
	consumer.close()  # close consumer after tests