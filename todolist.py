import tkinter as tkin #It imports tkinter module and can be used as tkin and provides GUI in Python.

class ToDoListApp(tkin.Tk):
    def __init__(self, tasks=[]): 
        super().__init__()
        self.tasks = tasks

        self.title("To-Do List")
        self.geometry("400x500")

        tkin.Label(self, text="Add a task:").pack()

        self.task_entry = tkin.Entry(self, width=40)
        self.task_entry.pack()

        add_task_btn = tkin.Button(self, text="Add", command=self.add_task)
        add_task_btn.pack()

        tkin.Label(self, text="Tasks:").pack()

        self.tasks_list = tkin.Listbox(self, width=40, height=10)
        self.update_task_list()
        self.tasks_list.pack()

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append(task)
        self.update_task_list()

    def update_task_list(self):
        self.tasks_list.delete(0, tkin.END)
        for task in self.tasks:
            self.tasks_list.insert(tkin.END, task)

app = ToDoListApp()
app.mainloop()
