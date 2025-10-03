# Task CLI

A simple command-line task management application for tracking your to-do list.

https://roadmap.sh/projects/task-tracker

## About

This project was created for learning Python programming. It demonstrates basic concepts of CLI application development, file handling, and object-oriented programming.

**Note:** Uses only Python standard library - no external dependencies required.

## Features

- Add, update, and delete tasks
- Mark tasks as todo, in progress, or done
- List all tasks or filter by status
- Interactive mode

## Installation

### Requirements
- Python 3.6 or higher

### Setup:
1. **Clone or download the project**
   ```bash
   git clone <repository-url>
   cd todo_cli
   ```

2. **Run the application**
   ```bash
   python main.py
   ```

The application will create a `tasks.json` file automatically to store your tasks.

## Usage

### Interactive Mode
Run `python main.py` to enter interactive mode:

```
Commands: add, list, update, mark-in-progress, mark-done, delete, help, exit
```

### Examples

```bash
# Adding a new task
add "Buy groceries"

# Listing tasks
list
list done
list todo
list in-progress

# Updating tasks
update 1 "Buy groceries and cook dinner"
mark-in-progress 1
mark-done 1

# Deleting tasks
delete 1
```

## Project Structure

```
todo_cli/
├── main.py              # Entry point
├── core/
│   └── task_manager.py  # Task management logic
└── utils/
    └── storage.py       # JSON file operations
```

## Learning Objectives

- Python basics and OOP
- File I/O operations
- CLI application development
- JSON data handling
- Error handling
- Code organization
