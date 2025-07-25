# Аналитические SQL-запросы для Jira PostgreSQL

Данный раздел содержит набор SQL-запросов для сбора аналитики из базы данных Jira. Запросы предоставляют ключевую статистику по задачам, дефектам и эффективности процессов разработки.

## Файлы запросов

### 1. Анализ приоритетов и критичности дефектов
- **Файл**: [bug_stats.sql](https://github.com/Ewerall/QA-Portfolio/blob/main/SQL/bug_stats.sql)
- **Назначение**:
  - Анализ распределения багов по приоритетам (Priority)
  - Статистика дефектов по уровню критичности (Severity)
  - Выявление наиболее проблемных областей продукта

### 2. Статистика по задачам проекта
- **Файл**: [jira_issue_stats.sql](https://github.com/Ewerall/QA-Portfolio/blob/main/SQL/jira_issue_stats.sql)
- **Запрос 1**: Статус задач
  - Распределение задач по статусам (To Do, In Progress, Done и др.)
  - Анализ прогресса выполнения работ
- **Запрос 2**: Просроченные задачи
  - Выявление задач, находящихся в работе более 7 дней
  - Определение "узких мест" в процессах

### 3. Анализ активности по задачам
- **Файл**: [live_issues.sql](https://github.com/Ewerall/QA-Portfolio/blob/main/SQL/live_issues.sql)
- **Метрики**:
  - Дата создания задачи
  - Время последнего обновления
  - Период бездействия (дней с последнего обновления)
  - Выявление "зависших" задач

## Результаты выполнения
- **Скриншоты выполнения запросов**:  
  [Просмотр результатов](https://github.com/Ewerall/QA-Portfolio/tree/main/SQL/screenshots)
- Примеры визуализации данных:
  - Диаграммы распределения дефектов
  - Таблицы статусов задач
  - Аналитические отчеты по активности

## Практическое применение
Представленные запросы позволяют:
- Мониторить качество продукта через призму дефектов
- Контролировать прогресс выполнения задач
- Выявлять узкие места в рабочих процессах
- Анализировать эффективность команды
- Принимать данные решения на основе метрик
