import tkinter as tk
from tkinter import messagebox, ttk
from ttkthemes import ThemedStyle
import json
import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ToDo App")
        self.root.geometry("500x400")

        style = ThemedStyle(root)
        style.set_theme("arc")

        self.tasks = []
        self.load_tasks()

        self.frame = ttk.Frame(self.root)
        self.frame.pack(pady=20)

        self.task_entry = ttk.Entry(self.frame, width=40)
        self.task_entry.pack(side=tk.LEFT, padx=10)

        self.add_task_btn = ttk.Button(self.frame, text="Add Task", command=self.add_task)
        self.add_task_btn.pack(side=tk.LEFT)

        self.tasks_frame = ttk.Frame(self.root)
        self.tasks_frame.pack(pady=10)

        self.show_tasks()

        self.save_tasks_btn = ttk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_tasks_btn.pack(pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False, "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
            self.task_entry.delete(0, tk.END)
            self.show_tasks()
        else:
            messagebox.showwarning("Warning", "You must enter a task.")

    def remove_task(self, task_index):
        del self.tasks[task_index]
        self.show_tasks()

    def complete_task(self, task_index):
        self.tasks[task_index]['completed'] = not self.tasks[task_index]['completed']
        self.show_tasks()

    def show_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()

        for index, task in enumerate(self.tasks):
            task_frame = ttk.Frame(self.tasks_frame)
            task_frame.pack(fill="x", pady=5)

            task_text = task['task']
            if task['completed']:
                task_text += " (Completed)"
                task_label = ttk.Label(task_frame, text=task_text, style="Completed.TLabel", width=50, anchor="w")
            else:
                task_label = ttk.Label(task_frame, text=task_text, style="Pending.TLabel", width=50, anchor="w")
            task_label.pack(side=tk.LEFT)

            complete_btn = ttk.Button(task_frame, text="Complete", command=lambda idx=index: self.complete_task(idx))
            complete_btn.pack(side=tk.LEFT, padx=5)

            remove_btn = ttk.Button(task_frame, text="Remove", command=lambda idx=index: self.remove_task(idx))
            remove_btn.pack(side=tk.LEFT)

        self.root.after(500, self.update_tasks)

    def save_tasks(self):
        with open("tasks.json", "w") as f:
            json.dump(self.tasks, f, indent=4)
        messagebox.showinfo("Info", "Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            self.tasks = []

    def update_tasks(self):
        for widget in self.tasks_frame.winfo_children():
            widget.destroy()
        self.show_tasks()

if __name__ == "__main__":
    root = tk.Tk()


    style = ttk.Style(root)
    style.configure("Completed.TLabel", foreground="green")
    style.configure("Pending.TLabel", foreground="black")

    app = TodoApp(root)
    root.mainloop()
