import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")

        self.tasks = []

        # Campo de entrada
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.bind("<Return>", self.add_task)  # permitir añadir tarea con Enter

        # Botón para añadir tareas
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Botón para marcar como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tareas
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Vincular doble clic a la tarea
        self.task_listbox.bind("<Double-1>", self.complete_task)

    def add_task(self, event=None):
        task_name = self.entry.get()
        if task_name:
            self.tasks.append(task_name)
            self.update_task_listbox()
            self.entry.delete(0, tk.END)  # Limpiar campo después de añadir
        else:
            messagebox.showwarning("Advertencia", "Por favor, introduce una tarea.")

    def complete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task_name = self.tasks[selected_index]
            self.tasks[selected_index] = f"{task_name} (Completada)"
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_listbox()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Limpiar la lista
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)  # Insertar tareas en la lista

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()