# QA Engineer Portfolio

## Обо мне  
QA Engineer. Специализация: комплексное **end-to-end тестирование** веб-приложений, построение процессов тестирования с нуля. Умею совмещать ручные и автоматизированные подходы QA.  

## Технический стек  
| **Категория**       | **Детализация**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| **Тестирование**     | • Ручное (Smoke, Regression, E2E, Usability, functional, nonfunctional) <br>• Автотесты (Pytest, request) |
| **Инструменты**      | • **Jira + XRay:** Полный цикл управления тестированием (test-case, test-run, привязка баг-репортов) <br>• **Postman + Newman**(коллекции, скрипты на JS, CRUD запросы, отчеты) <br>• Chrome DevTools (Elements, Network, Console) <br>• Docker (развертывание Jira/PostgreSQL) <br>• Git/GitHub Actions (CI/CD) <br>• Swagger (Документация API) <br>• Grafana (Логирование) <br>• Testrail (TMS) <br>• Kafka (Микросервис) <br>• Selenium (UI автотесты)
| **Тест-дизайн**      | • Эквивалентное разделение (проверка классов значений) <br>• Анализ граничных значений (тестирование на границах) <br>• Таблицы решений (комбинации действие/результат) <br>• Попарное тестирование (пары параметров) <br>• Предугадывание ошибок (Error Guessing)| 
| **Программирование** | • Python (pytest, requests, etc.) <br>• JavaScript |
| **Базы данных**      | • PostgreSQL <br>• MySQL |
| **Процессы**         | • SDLC/STLC <br>• Agile (Scrum) <br>• REST API <br>• CI/CD основы | 


## Структура репозитория

    QA-Portfolio
    ├── .github
    │   └── workflows
    │       └── api-python.yml
    ├── Auto-testing
    │   ├── API-Tests
    │   │   ├── allure [Allure report directory]
    │   │   ├── allure_report.png
    │   │   ├── conftest.py
    │   │   ├── README.md
    │   │   └── test_reqres.py
    │   └── Unit-Tests
    │       ├── calc_test*.py
    │       ├── README.md
    │       └── Screenshots [3 files]
    ├── Documentation
    │   ├── calc_req.pdf
    │   └── Test-Design
    │       ├── README.md
    │       └── TestDesign.md
    ├── Infrastructure
    │   ├── CI-CD
    │   │   ├── calc_project_cicd.png
    │   │   ├── python-tests.yml
    │   │   └── README.md
    │   └── Jira-Docker
    │       ├── example [5 config files]
    │       ├── Readme.md
    │       └── screenshots [2 files]
    ├── LICENSE
    ├── Manual-testing
    │   ├── Calculator-Project
    │   │   ├── Bug-reports [8 bug reports]
    │   │   ├── Other [10 misc files]
    │   │   ├── README.md
    │   │   ├── Requirements
    │   │   │   └── v1.0 [3 requirement specs]
    │   │   ├── Test-cases
    │   │   │   ├── V1.0 [6 test case categories]
    │   │   │   └── V1.1 [5 test case sets]
    │   │   └── Test-execution
    │   │       ├── V1.0 [7 execution sets]
    │   │       └── V1.1 [9 execution reports]
    │   └── Public-APIs
    │       ├── Collections
    │       │   ├── GitAuth [Postman collection]
    │       │   ├── Jsonplaceholder [Postman collection]
    │       │   └── Petstore-swagger [Postman collection]
    │       ├── README.md
    │       └── Screenshots
    │           ├── GitAuth [6 screenshots]
    │           ├── Jsonplaceholder [9 screenshots]
    │           └── Petstore-Swagger [7 screenshots]
    ├── README.md
    └── SQL
        ├── *.sql [3 SQL scripts]
        ├── README.md
        └── screenshots [4 report screenshots]

## Проекты  

### Развертывание Jira + Xray в Docker  
**Задачи:**  
- Создание инфраструктуры для управления тестированием с нуля  
- Настройка связки Jira Server 8.12 + PostgreSQL в Docker  
- Интегрирование Xray для управления тест-кейсами и Test Execution + Checklist for Jira

**Результат:**  
  Готовое тестовое окружение  
  Единое пространство для проектов с историей тестирования 

**Что такое XRay:**  
  Плагин для Jira, превращающий её в систему управления тестированием (альтернатива TestRail) 
  
**Мои задачи:**  
- Настройка проектов в XRay  
- Создание структурированных тест-кейсов  
- Проведение тест-ранов с фиксацией результатов  
- Связь баг-репортов с тест-кейсами  
**Результат:**  
Единая среда для документации и отчетности по тестированию.

**Технологии:** Docker, PostgreSQL, Jira Server  

[Docker + Jira](https://github.com/Ewerall/QA-Portfolio/tree/main/jira-docker)


### Полный цикл тестирования Python-калькулятора  
**Задачи:**  
- Разработка приложения на Python/Tkinter с преднамеренными дефектами  
- Проведение функционального/нефункционального тестирования  
- Создание тест-кейсов (Xray), обнаружение дефектов и создание bug-репортов  
- Реализация автоматизации проверки расчетов (pytest)

**Техники тест-дизайна:**  
- Таблица решений для проверки комбинаций операций [+, -, ?, ?]  
- Исследовательское тестирование UI 

**Результат:**  
  Документированный процесс тестирования от требований до отчета  
  Шаблон для тренировки техник тест-дизайна, написания тест-кейсов и создания автотестов 

**Технологии:** Python, pytest, Tkinter, Jira + Xray

[Репозиторий](https://github.com/Ewerall/CalcQA)
[Работа с task-менеджером и баг-трекером](https://github.com/Ewerall/QA-Portfolio/tree/main/Calc-Project)


## Актуальные навыки  
| **Осваиваю**                | **Планирую**             |  
|-----------------------------|--------------------------|  
| • Автоматизация UI (Selenium WebDriver) <br>• Автоматизация API (requests, pytest) <br>• CI/CD <br>• Kafka| • Performance testing (k6) <br>• Kubernetes для тестовых сред |  

## Контакты  
-  **Email:** starere@mail.com  
-  **Telegram:** [Rubercore](https://t.me/Rubercore)  
-  **GitHub:** [GitHub](https://github.com/Ewerall)

![Codewars](https://github.r2v.ch/codewars?user=Ewerall&name=true&top_languages=true&stroke=%230000CD&theme=midnight_blue)
