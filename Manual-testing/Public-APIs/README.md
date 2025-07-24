# Комплексное тестирование публичных API через Postman

Данный раздел содержит коллекции Postman для тестирования трёх различных API-сервисов. Каждая коллекция включает набор запросов, покрывающих ключевые функциональные сценарии.

## Коллекция: GitHub API (OAuth-авторизация)

### Описание
- **Расположение**: [GitAuth](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Public-APIs/Collections/GitAuth)
- **Тестируемые функции**:
  - Авторизация через OAuth приложение GitHub
  - Создание и удаление Gist
  - Получение данных пользователя
  - Управление аутентифицированными сессиями
- **Результаты выполнения**:  
  [Скриншоты тестовых прогонов](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Public-APIs/Screenshots/GitAuth)

---

## Коллекция: JSONPlaceholder API

### Описание
- **Расположение**: [Jsonplaceholder](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Public-APIs/Collections/Jsonplaceholder)
- **Тестируемые функции**:
  - CRUD операции с постами (создание, чтение, обновление, удаление)
  - Получение данных пользователей
  - Обработка JSON-ответов через Postman-скрипты
  - Валидация ответов на невалидные запросы
- **Тестируемый ресурс**: [JSONPlaceholder](https://jsonplaceholder.typicode.com)
- **Результаты выполнения**:  
  [Скриншоты тестовых прогонов](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Public-APIs/Screenshots/Jsonplaceholder)

---

## Коллекция: Swagger Petstore API

### Описание
- **Расположение**: [Petstore-swagger](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Public-APIs/Collections/Petstore-swagger)
- **Тестируемые функции**:
  - Полный жизненный цикл сущности Pet (создание, чтение, обновление, удаление)
  - Обработка некорректных запросов
  - Валидация кодов ответов и структур данных
  - Тестирование граничных значений
- **Тестируемый ресурс**: [Swagger Petstore](https://petstore.swagger.io)
- **Результаты выполнения**:  
  [Скриншоты тестовых прогонов](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Public-APIs/Screenshots/Petstore-Swagger)

---

## Ключевые аспекты тестирования
Во всех коллекциях особое внимание уделялось:
- Проверке корректности HTTP-статусов
- Валидации структур ответов
- Тестированию граничных условий
- Обработке ошибочных сценариев
- Автоматизации проверок через Postman-скрипты
- Документированию результатов тестирования
