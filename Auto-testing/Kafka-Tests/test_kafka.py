import pytest
import allure
import time
from kafka_utils import create_consumer, send_event, consume_event

# Test data
ORDER_EVENT = {
    "order_id": "12345",
    "user_id": "user_678",
    "items": [
        {"product_id": "prod_1", "quantity": 2},
        {"product_id": "prod_2", "quantity": 1}
    ],
    "total": 99.99
}

@allure.epic("Тестирование Кафка")
@allure.feature("Event-Driven архитектура")
class TestKafkaIntegration:
    
    @allure.story("Отправка события о создании заказа")
    @allure.title("Проверка доставки события создания заказа")
    def test_order_creation_event(self, producer, order_consumer):
        with allure.step("Отправка события в топик orders"):
            send_event(producer, "orders", ORDER_EVENT)
        
        with allure.step("Получение события из топика orders"):
            received_event = consume_event(order_consumer, timeout=15)
        
        with allure.step("Проверка содержимого события"):
            assert received_event == ORDER_EVENT, "Событие не соответствует ожидаемому"

    
    @allure.story("Тестирование обработки больших объемов данных")
    @allure.title("Проверка пропускной способности")
    def test_throughput(self, producer):
        group_id = f"load_test_group_{time.time()}"
        consumer = create_consumer("load_test", group_id)
        
        with allure.step("Отправка 100 тестовых событий"):
            for i in range(100):
                send_event(producer, "load_test", {"message_num": i})
        
        with allure.step("Подтверждение доставки всех сообщений"):
            received_count = 0
            start_time = time.time()
            
            #check with timeout
            while received_count < 100 and time.time() - start_time < 30:
                messages = consumer.poll(timeout_ms=1000, max_records=100)
                for records in messages.values():
                    received_count += len(records)
            
            assert received_count == 100, f"Получено {received_count}/100 сообщений"

        consumer.close()