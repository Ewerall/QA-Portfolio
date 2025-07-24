# Набор автотестов для API Reqres.in

Данный репозиторий содержит комплекс автоматических тестов для учебного API [Reqres.in](https://reqres.in) - популярного сервиса для тестирования API-взаимодействий. Набор тестов проверяет CRUD-операции и процессы аутентификации с использованием стандартных инструментов.

## Ключевые компоненты

### Реализация тестов
- **`test_reqres.py`**:  
  Содержит тест-кейсы для конечных точек API, включая валидацию CRUD-операций  
  [Просмотр файла](https://github.com/Ewerall/QA-Portfolio/blob/main/Auto-testing/API-Tests/test_reqres.py)

### Инфраструктура тестирования
- **`conftest.py`**:  
  Содержит фикстуры для аутентификации и конфигурации управления сессиями  
  [Просмотр конфигурации](https://github.com/Ewerall/QA-Portfolio/blob/main/Auto-testing/API-Tests/conftest.py)
- **Pytest Framework**: Организация и выполнение тестов
- **Requests Library**: Обработка HTTP-запросов

### Отчётность
- **Allure отчёты**:  
  Детализированные HTML-отчёты, автоматически генерируемые через GitHub Actions  
  [Просмотр директории](https://github.com/Ewerall/QA-Portfolio/tree/main/Auto-testing/API-Tests/allure)
- **Скриншот отчёта**:  
  Пример визуализации вывода Allure  
  ![Allure Report](https://github.com/Ewerall/QA-Portfolio/blob/main/Auto-testing/API-Tests/allure_report.png)

## Покрытие тестами
Набор проверяет:
- Создание пользователей (POST)
- Получение данных пользователей (GET)
- Обновление информации (PUT/PATCH)
- Удаление пользователей (DELETE)
- Сценарии аутентификации
- Валидацию схемы ответов
- Проверку HTTP статус-кодов
