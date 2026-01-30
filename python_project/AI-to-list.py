import tkinter as tk
from tkinter import messagebox, simpledialog
import openai
openai.api_key ="axxx---x-xx"
"""
upgraded hte GPT-API 
and version to pip install==0.28"""
class TaskManager:
    def __init__(self):
        self.tasks = []  

    def add_task(self, task_name):
        prompt = f"""
        You are an AI task manager.
        For the task: "{task_name}", suggest:
        1. Category (Work, Personal, Study, Other)
        2. Deadline (format: YYYY-MM-DD)
        3. Priority (High, Medium, Low)
        Give the response in this JSON format:
        {{
            "category": "Category here",
            "deadline": "YYYY-MM-DD",
            "priority": "Priority here"
        }}
        """
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )
            result_text = response.choices[0].message.content.strip()

            # Convert GPT JSON-like text to Python dict
            import json
            result = json.loads(result_text.replace("\n", ""))
        except Exception as e:
            messagebox.showerror("GPT Error", f"Could not get suggestion:\n{e}")
            result = {"category": "Other", "deadline": "N/A", "priority": "Medium"}

        task = {
            "task": task_name,
            "category": result["category"],
            "deadline": result["deadline"],
            "priority": result["priority"]
        }
        self.tasks.append(task)
        return task
class TodoGUI:
    def __init__(self, root, manager):
        self.manager = manager
        self.root = root
        self.root.title("AI To-Do List")
        self.root.geometry("500x400")

       
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        self.task_entry.focus()
        tk.Button(root, text="Add Task", command=self.add_task).pack()
        tk.Button(root, text="Show Tasks", command=self.show_tasks).pack(pady=5)
        self.text_area = tk.Text(root, width=60, height=15)
        self.text_area.pack(pady=10)

    def add_task(self):
        task_name = self.task_entry.get()
        if not task_name:
            messagebox.showwarning("Oops!", "Please enter a task!")
            return
        task = self.manager.add_task(task_name)
        messagebox.showinfo("Task Added", f"Task: {task['task']}\nCategory: {task['category']}\nDeadline: {task['deadline']}\nPriority: {task['priority']}")
        self.task_entry.delete(0, tk.END)

    def show_tasks(self):
        self.text_area.delete(1.0, tk.END)
        if not self.manager.tasks:
            self.text_area.insert(tk.END, "No tasks yet.\n")
            return
        for i, task in enumerate(self.manager.tasks, 1):
            self.text_area.insert(tk.END, f"{i}. {task['task']} | {task['category']} | {task['deadline']} | {task['priority']}\n")
if __name__ == "__main__":
    root = tk.Tk()
    manager = TaskManager()
    app = TodoGUI(root, manager)
    root.mainloop()
