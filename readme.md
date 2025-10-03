# Task CLI

A simple command-line task management application for tracking your to-do list.

Простое консольное приложение для управления задачами и списком дел.

https://roadmap.sh/projects/task-tracker

## About / О проекте

This project was created for learning Python programming. It demonstrates basic concepts of CLI application development, file handling, and object-oriented programming.

Этот проект создан для изучения программирования на Python. Он демонстрирует основные концепции разработки CLI-приложений, работы с файлами и объектно-ориентированного программирования.

**Note:** This project uses only Python standard library - no external dependencies required.

**Примечание:** В проекте используются только стандартные библиотеки Python - внешние зависимости не требуются.

## Features / Возможности

- ✅ Add, update, and delete tasks / Добавлять, обновлять и удалять задачи
- ✅ Mark tasks as todo, in progress, or done / Отмечать задачи как ожидающие, в процессе или выполненные
- ✅ List all tasks or filter by status / Показывать все задачи или фильтровать по статусу
- ✅ Interactive mode / Интерактивный режим

## Installation & Setup / Установка и настройка

### Prerequisites / Требования
- Python 3.6 or higher / Python 3.6 или выше

### Steps / Шаги:

1. **Clone or download the project** / Клонируйте или скачайте проект
   ```bash
   # If using git / Если используете git
   git clone <repository-url>
   cd todo_cli
   ```

2. **Run the application** / Запустите приложение
   ```bash
   python main.py
   ```

The application will create a `tasks.json` file automatically to store your tasks.

Приложение автоматически создаст файл `tasks.json` для хранения ваших задач.

## Usage / Использование

### Interactive Mode / Интерактивный режим
Run `python main.py` to enter interactive mode where you can use commands:

Запустите `python main.py` для входа в интерактивный режим, где можно использовать команды:

```
Commands: add, list, update, mark-in-progress, mark-done, delete, help, exit
```

### Examples / Примеры

```bash
# Adding a new task / Добавление новой задачи
add "Buy groceries"

# Listing tasks / Просмотр задач
list
list done
list todo
list in-progress

# Updating tasks / Обновление задач
update 1 "Buy groceries and cook dinner"
mark-in-progress 1
mark-done 1

# Deleting tasks / Удаление задач
delete 1
```

## Project Structure / Структура проекта

```
todo_cli/
├── main.py              # Entry point / Точка входа
├── core/
│   └── task_manager.py  # Task management logic / Логика управления задачами
└── utils/
    └── storage.py       # JSON file operations / Операции с JSON файлами
```

## Learning Objectives / Цели обучения

- Python basics and OOP / Основы Python и ООП
- File I/O operations / Операции ввода-вывода с файлами
- CLI application development / Разработка CLI-приложений
- JSON data handling / Работа с JSON данными
- Error handling / Обработка ошибок
- Code organization / Организация кода
