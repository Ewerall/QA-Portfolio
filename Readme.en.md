# QA Engineer Portfolio

[![RU](https://img.shields.io/badge/RU-русский-0066CC?logo=russia&logoColor=white)](https://github.com/Ewerall/QA-Portfolio/blob/main/README.md)

[![Jira](https://img.shields.io/badge/Jira-0052CC?logo=jira&logoColor=white)](https://www.atlassian.com/software/jira)
[![Git](https://img.shields.io/badge/Git-F05032?logo=git&logoColor=white)](https://git-scm.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)](https://docs.pytest.org/)
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
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?logo=githubactions&logoColor=white)](https://github.com/features/actions)
[![Charles Proxy](https://img.shields.io/badge/Charles_Proxy-8FBCBB?logo=charles&logoColor=black)](https://www.charlesproxy.com/)
[![Playwright](https://img.shields.io/badge/Playwright-2EAD33?logo=playwright&logoColor=white)](https://playwright.dev/)

## About Me  
I am a 22-year-old aspiring QA Engineer. I independently study materials, documentation, and articles while creating pet projects for practice and building this portfolio. My goal is to develop and enhance professional skills in the QA field.  
All projects in this portfolio are educational – they help me solidify knowledge and develop testing skills. While I don't have commercial QA experience yet, I'm actively growing and striving for new achievements in this domain.

## Technical Stack  
| **Category**         | **Details**                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **Testing**          | • Manual (Smoke, Regression, E2E, Usability, Functional, Non-functional) <br>• Automation (pytest, requests, Allure, Faker, Selenium, Playwright, design patterns) |
| **Tools**            | • **Jira + Xray Test Management:** Task and test management (test cases, test runs, bug report linking) <br>• **Postman + Newman** (collections, JS scripts, CRUD requests, reports) <br>• Chrome DevTools (Elements, Network, Console) <br>• Docker (Jira/PostgreSQL deployment) <br>• Git/GitHub Actions (CI/CD) <br>• Swagger (API documentation) <br>• Grafana (Metrics visualization and monitoring) <br>• Prometheus (Metrics storage) <br>• TestRail (TMS) <br>• Apache Kafka (Microservices) <br>• Selenium (UI web automation) <br>• Playwright (UI web automation) |
| **Test Design**      | • Equivalence Partitioning (value class verification) <br>• Boundary Value Analysis (edge case testing) <br>• Decision Tables (action/result combinations) <br>• Pairwise Testing (parameter pairs) <br>• Error Guessing | 
| **Programming**      | • Python <br>• JavaScript |
| **Databases**        | • PostgreSQL <br>• MySQL |
| **Processes**        | • SDLC/STLC <br>• Agile (Scrum) <br>• REST API <br>• CI/CD Fundamentals | 

## Selected Projects
- **Playwright-POM** automation for **Demoblaze** web app + **GitHub Actions** + **Allure** + **GitHub Pages** [Details](https://github.com/Ewerall/PlaywrightDemoblaze)
  - <video src='https://github.com/user-attachments/assets/1c503fa2-f8ec-4cfc-a1f5-7eefd5123ff6' width=180/>

- **Selenium** automation using **Page Object Model (POM)** for **SauceDemo** web app [Details](https://github.com/Ewerall/QA-Portfolio/tree/main/Auto-testing/UI-Tests "UI-Tests")
  - ![allure_report.png](https://github.com/Ewerall/QA-Portfolio/blob/main/Auto-testing/UI-Tests/allure_report.png "Allure Report")

- Manual testing of a custom "Calculator" desktop app. Created test cases, executed tests, filed bug reports using self-hosted **Jira Server** [Details](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Calculator-Project "Calculator-Project")
  - ![test_plan_regress.png](https://github.com/Ewerall/QA-Portfolio/blob/main/Manual-testing/Calculator-Project/Other/test_plan_regress.png "Regression Test Plan")

- Implemented **Grafana** and **Prometheus** for **Jira Server** monitoring [Details](https://github.com/Ewerall/QA-Portfolio/tree/main/Infrastructure/Jira-Docker/Grafana_Prometheus "Grafana_Prometheus")
  - ![grafana_metrics.png](https://github.com/Ewerall/QA-Portfolio/blob/main/Infrastructure/Jira-Docker/Grafana_Prometheus/grafana_metrics.png "Grafana Metrics")

**More projects in the repository!**

## Repository Structure

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
    │   └── UI-Tests [Selenium + Allure] 
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
            ├── easy [16 screenshots]
            ├── medium [17+ screenshots]
            ├── hard [3+ screenshots]
            └── README.md

## Pet Projects  

### **Jira Server** Deployment via **Docker Compose** + **Grafana** 
**Tasks:**  
- Create testing management infrastructure from scratch  
- Configure Jira Server 8.12 + PostgreSQL in Docker  
- Integrate Xray for test management + Checklist for Jira  

**Results:**  
  Ready-to-use testing environment  
  Unified workspace with testing history  

**What is XRay:**  
  Jira plugin that transforms it into a test management system (TestRail alternative)  
  
**My Responsibilities:**  
- Configure XRay projects  
- Create structured test cases  
- Execute test runs with results tracking  
- Link bug reports to test cases  

**Technologies:** Docker, PostgreSQL, Jira Server, **Grafana**, **Prometheus**

[Docker + Jira](https://github.com/Ewerall/QA-Portfolio/tree/main/jira-docker)

**UPD**: Added Grafana and Prometheus containers for metrics storage and visualization. Details in [Jira-Docker/Grafana_Prometheus](https://github.com/Ewerall/QA-Portfolio/tree/main/Infrastructure/Jira-Docker/Grafana_Prometheus "Grafana_Prometheus")

### Full Testing Cycle for Python Calculator  
**Tasks:**  
- Develop Python/Tkinter app with intentional defects  
- Conduct functional/non-functional testing  
- Create test cases (Xray), detect defects, file bug reports  
- Implement calculation verification automation (pytest)

**Results:**  
  Documented testing process from requirements to report  
  Template for practicing test design techniques and automation  

**Technologies:** Python (pytest, requests, Allure - automation; Tkinter - UI), Jira + Xray (task/test management)

[Repository](https://github.com/Ewerall/CalcQA)
[Jira + Test Management](https://github.com/Ewerall/QA-Portfolio/tree/main/Calc-Project)

## Other Projects

- API Automation for Reqres.in [Auto-testing/API-Tests](https://github.com/Ewerall/QA-Portfolio/tree/main/Auto-testing/API-Tests "API-Tests")
- Apache Kafka Event-Driven Testing [Auto-testing/Kafka-Tests](https://github.com/Ewerall/QA-Portfolio/tree/main/Auto-testing/Kafka-Tests "Kafka-Tests")
- Unit Testing for "Calculator" Logic [Auto-testing/Unit-tests](https://github.com/Ewerall/QA-Portfolio/tree/main/Auto-testing/Unit-Tests "Unit-Tests")
- 16 Test Cases for Online Audio Converter [Documentation/Test-Design](https://github.com/Ewerall/QA-Portfolio/tree/main/Documentation/Test-Design "Test-Design")
- CI/CD Setup with GitHub Actions [Infrastructure/CI-CD](https://github.com/Ewerall/QA-Portfolio/tree/main/Infrastructure/CI-CD "CI-CD")
- Apache Kafka Docker Deployment [Infrastructure/Kafka-Docker](https://github.com/Ewerall/QA-Portfolio/tree/main/Infrastructure/Kafka-Docker "Kafka-Docker")
- Public API Testing with Postman/Newman [Public-APIs](https://github.com/Ewerall/QA-Portfolio/tree/main/Manual-testing/Public-APIs "Public-APIs")
- PostgreSQL for Jira Statistics [SQL/PostgreSQL_Jira](https://github.com/Ewerall/QA-Portfolio/tree/main/SQL/PostgreSQL_Jira "PostgreSQL_Jira")
- SQL Practice (sql-practice.com) [SQL/SQL-practice](https://github.com/Ewerall/QA-Portfolio/tree/main/SQL/SQL-practice "SQL-practice")

## Skills Development  
| **Mastering**                          | **Learning**                     | **Goals**                     | 
|----------------------------------------|----------------------------------|-------------------------------|  
| • UI Automation (Selenium, Playwright) <br>• API Automation (requests, mureq) <br>• CI/CD (GitHub Actions, Jenkins) <br>• Apache Kafka <br>• SQL (PostgreSQL, MySQL) <br>• Design Patterns (Factory, Builder, POM) <br>• Test Design Techniques | • Performance Testing (k6) <br>• Kubernetes <br>• Charles Proxy | • Gain commercial QA experience <br>• Deepen technical expertise

## Contact  
-  **Email:** starere@mail.com  
-  **Telegram:** [@Rubercore](https://t.me/Rubercore)  
-  **GitHub:** [https://github.com/Ewerall](https://github.com/Ewerall)

![Codewars](https://github.r2v.ch/codewars?user=Ewerall&name=true&top_languages=true&stroke=%230000CD&theme=midnight_blue)
