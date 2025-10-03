import time
from utils.storage import read_json, save_json


class TaskManager:

    def __init__(self):
        self.tasks = read_json()

    def create_task(self, description, status="todo"):

        if len(self.tasks) == 0:
            id = 1
        else:
            id = self.tasks[-1]["id"] + 1

        task = {
            "id": id,
            "description": description,
            "status": status,
            "createdAt": time.ctime(),
            "updatedAt": time.ctime(),
        }

        self.tasks.append(task)

        save_json(self.tasks)
        return f"Task created with id {id}"

    def read_all_tasks(self):

        if len(self.tasks) == 0:
            print(f"Task list is empty")
        else:
            for task in self.tasks:
                print(
                    f"id: {task['id']} | description: {task['description']} | status: {task['status']} | createdAt: {task['createdAt']} | updatedAt: {task['updatedAt']}"
                )

    def read_tasks_by_status(self, status):

        if len(self.tasks) == 0:
            print(f"Task list is empty")
        else:
            for task in self.tasks:
                if task.get("status") == status:
                    print(
                        f"id: {task['id']} | description: {task['description']} | status: {task['status']} | createdAt: {task['createdAt']} | updatedAt: {task['updatedAt']}"
                    )

    def change_task_status(self, id, status):

        for i in range(len(self.tasks)):
            if self.tasks[i].get("id") == id:
                self.tasks[i]["status"] = status
                save_json(self.tasks)
                return f"Task with id: {id} changed status to {status}"
        else:
            return f"Task with this id not found"

    def update_task_description(self, id, description):

        for i in range(len(self.tasks)):
            if self.tasks[i].get("id") == id:
                self.tasks[i]["description"] = description
                self.tasks[i]["updatedAt"] = time.ctime()
                save_json(self.tasks)
                return f"Task with id: {id} updated"
        else:
            return f"Task with this id not found"

    def delete_task(self, id):

        for i in range(len(self.tasks)):
            if self.tasks[i].get("id") == id:
                del self.tasks[i]
                save_json(self.tasks)
                return f"Task with id: {id} deleted!"
        else:
            return f"Task with this id not found"
