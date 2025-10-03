from core.task_manager import TaskManager


def main():
    manager = TaskManager()

    while True:
        print("\n" + "=" * 50)
        print("TASK CLI - Interactive Mode")
        print("=" * 50)
        print(
            "Commands: add, list, update, mark-in-progress, mark-done, delete, help, exit"
        )

        user_input = input("\nEnter command: ").strip().split()

        if not user_input:
            continue

        command = user_input[0]

        try:
            if command == "add" and len(user_input) >= 2:
                text = " ".join(user_input[1:])
                print(manager.create_task(text))

            elif command == "list":
                if len(user_input) >= 2:
                    status = user_input[1]
                    if status in ["todo", "in-progress", "done"]:
                        manager.read_tasks_by_status(status)
                    else:
                        print("Error: Status must be 'todo', 'in-progress', or 'done'")
                else:
                    manager.read_all_tasks()

            elif command == "update" and len(user_input) >= 3:
                task_id = int(user_input[1])
                new_text = " ".join(user_input[2:])
                print(manager.update_task_description(task_id, new_text))

            elif command == "mark-in-progress" and len(user_input) >= 2:
                task_id = int(user_input[1])
                print(manager.change_task_status(task_id, "in-progress"))

            elif command == "mark-done" and len(user_input) >= 2:
                task_id = int(user_input[1])
                print(manager.change_task_status(task_id, "done"))

            elif command == "delete" and len(user_input) >= 2:
                task_id = int(user_input[1])
                print(manager.delete_task(task_id))

            elif command == "help":
                print_help()

            elif command == "exit":
                print("Goodbye!")
                break

            else:
                print("Invalid command. Type 'help' for available commands.")

        except ValueError:
            print("Error: Task ID must be a number")
        except Exception as e:
            print(f"Error: {e}")


def print_help():
    help_text = """
Available Commands:
  add "Task description"          - Add new task
  list                            - List all tasks
  list [todo|in-progress|done]    - List tasks by status
  update <id> "New description"   - Update task description
  mark-in-progress <id>           - Mark task as in progress
  mark-done <id>                  - Mark task as done
  delete <id>                     - Delete task
  help                            - Show this help
  exit                            - Exit the program
"""
    print(help_text)


if __name__ == "__main__":
    main()
