# QA Engineer Portfolio

[![Jira](https://img.shields.io/badge/Jira-0052CC?logo=jira&logoColor=white)](https://www.atlassian.com/software/jira)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![Postman](https://img.shields.io/badge/Postman-FF6C37?logo=postman&logoColor=white)](https://www.postman.com/)
[![Newman](https://img.shields.io/badge/Newman-FF6C37?logo=postman&logoColor=white)](https://learning.postman.com/docs/running-collections/using-newman-cli/command-line-integration-with-newman/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Swagger](https://img.shields.io/badge/Swagger-85EA2D?logo=swagger&logoColor=black)](https://swagger.io/)
[![Grafana](https://img.shields.io/badge/Grafana-F46800?logo=grafana&logoColor=white)](https://grafana.com/)
[![Kafka](https://img.shields.io/badge/Kafka-231F20?logo=apachekafka&logoColor=white)](https://kafka.apache.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?logo=prometheus&logoColor=white)](https://prometheus.io/)
[![Chrome DevTools](https://img.shields.io/badge/Chrome_DevTools-4285F4?logo=googlechrome&logoColor=white)](https://developer.chrome.com/docs/devtools/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white)](https://github.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)
## Обо мне   
Самостоятельно изучая материалы, документацию, статьи - создал портфолио и учебные проекты, для изучения полного цикла тестирования. Совмещаю ручные и автоматизированные подходы QA. Для лучшего понимания моих навыков, советую просмотреть этот репозиторий.

## Технический стек  
| **Категория**       | **Детализация**                                                                 |
|----------------------|---------------------------------------------------------------------------------|
| **Тестирование**     | • Ручное (Smoke, Regression, E2E, Usability, functional, nonfunctional) <br>• Автотесты (Pytest, request) |
| **Инструменты**      | • **Jira + XRay:** Полный цикл управления тестированием (test-case, test-run, привязка баг-репортов) <br>• **Postman + Newman**(коллекции, скрипты на JS, CRUD запросы, отчеты) <br>• Chrome DevTools (Elements, Network, Console) <br>• Docker (развертывание Jira/PostgreSQL) <br>• Git/GitHub Actions (CI/CD) <br>• Swagger (Документация API) <br>• Grafana (Отображение метрик и мониторинг) <br>• Prometheus (Хранение метрик) <br>• Testrail (TMS) <br>• Kafka (Микросервисы) <br>• Selenium (UI web автотест)
| **Тест-дизайн**      | • Эквивалентное разделение (проверка классов значений) <br>• Анализ граничных значений (тестирование на границах) <br>• Таблицы решений (комбинации действие/результат) <br>• Попарное тестирование (пары параметров) <br>• Предугадывание ошибок (Error Guessing)| 
| **Программирование** | • Python (pytest, requests, etc.) <br>• JavaScript |
| **Базы данных**      | • PostgreSQL <br>• MySQL |
| **Процессы**         | • SDLC/STLC <br>• Agile (Scrum) <br>• REST API <br>• CI/CD основы | 

## Примеры некоторых работ
- Работа с **Selenium** и использование паттерна проектирования **Page object model (POM)** для автотестирования web-приложения **SauceDemo**. [Подробнее](https://github.com/Ewerall/QA-Portfolio/tree/main/Auto-testing/UI-Tests "UI-Tests")
  - ![allure_report.png](https://github.com/Ewerall/QA-Portfolio/blob/main/Auto-testing/UI-Tests/allure_report.png "allure_report.png")

- Ручное тестирование собственного desktop-приложения "Калькулятор". Создание тест-кейсов, их выполнение, создание баг-репортов и все это на собственном **Jira-Server**.  [Подробнее](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Calculator-Project "Calculator-Project")
  - ![test_plan_regress.png](https://github.com/Ewerall/QA-Portfolio/blob/main/Manual-testing/Calculator-Project/Other/test_plan_regress.png "test_plan_regress.png")

- Внедрение **Grafana** и **Prometheus** для своего **Jira Server** для отслеживания показателей работы и других метрик. [Подробнее](https://github.com/Ewerall/QA-Portfolio/tree/main/Infrastructure/Jira-Docker/Grafana_Prometheus "Grafana_Prometheus")
  - ![grafana_metrics.png](https://github.com/Ewerall/QA-Portfolio/blob/main/Infrastructure/Jira-Docker/Grafana_Prometheus/grafana_metrics.png "grafana_metrics.png")

 **Остальные работы в репозитории!** (Их много)

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
    │   ├── Unit-Tests
    │   │   ├── calc_test*.py
    │   │    ├── README.md
    │   │    └── Screenshots [3 files]
    │   └── UI-Tests [Selenium + allure report] 
    │       └── *.py [4 page objects (POM) + tests + fixtures]
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
    │       ├── Grafana_Prometheus [config files and readme]
    │       ├── example [5 config files]
    │       ├── Readme.md
    │       └── screenshots [2 files]
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
    └── SQL
        ├── PostgreSQL_Jira
        │    ├── *.sql [3 SQL scripts]
        │    ├── README.md
        │    └── screenshots [4 report screenshots]
        └── SQL-practice
            ├── easy [16 screenshots[
            ├── medium [17+ screenshots]
            ├── hard [3+ screenshots]
            └── README.md

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

**Технологии:** Docker, PostgreSQL, Jira Server, **Grafana**, **Prometheus**

[Docker + Jira](https://github.com/Ewerall/QA-Portfolio/tree/main/jira-docker)

**UPD**: Были добавлены контейнеры Grafana и Prometheus для хранения и отображения метрик и логирования. Подробнее в [Jira-Docker/Grafana_Prometheus](https://github.com/Ewerall/QA-Portfolio/tree/main/Infrastructure/Jira-Docker/Grafana_Prometheus "Grafana_Prometheus")


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

**Технологии:** Python(pytest, request, allure - для автотестов, Tkinter - UI), Jira + Xray (для task и test менеджмента)

[Репозиторий](https://github.com/Ewerall/CalcQA)
[Работа с task-менеджером и баг-трекером](https://github.com/Ewerall/QA-Portfolio/tree/main/Calc-Project)


## Актуальные навыки  
| **Осваиваю и улучшаю**   | **Планирую и изучаю**  | **Цели** | 
|-----------------------------|--------------------------|  --------------------------|  
| • Автоматизация UI (Selenium WebDriver) <br>• Автоматизация API (requests, pytest) <br>• CI/CD (Github Actions) <br>• Kafka (Для работы с микросервисами)| • Performance testing (k6) <br>• Kubernetes для тестовых сред | • Получить первый коммерческий опыт в QA <br>• Углубить знания в автоматизации тестирования

## Контакты  
-  **Email:** starere@mail.com  
-  **Telegram:** [@Rubercore](https://t.me/Rubercore)  
-  **GitHub:** [GitHub](https://github.com/Ewerall)

![Codewars](https://github.r2v.ch/codewars?user=Ewerall&name=true&top_languages=true&stroke=%230000CD&theme=midnight_blue)

