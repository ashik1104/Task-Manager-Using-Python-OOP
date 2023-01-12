import uuid
import datetime


class Task:
    all_task = {}

    unchanged_tasks = {}
    updated_tasks = {}

    incomplete_tasks = {}
    completed_tasks = {}

    def __init__(self, tsk_name):
        self.task_name = tsk_name
        self.created_time = datetime.datetime.now().isoformat(' ', 'seconds')
        self.updated_time = 'NA'
        self.completed_time = 'NA'
        self.task_done = False
        self.id = uuid.uuid4()

    def update_task(self, task_obj, new_name):
        task_obj.task_name = new_name
        task_obj.updated_time = datetime.datetime.now().isoformat(' ', 'seconds')

    def complete_task(self, task_obj):
        task_obj.completed_time = datetime.datetime.now().isoformat(' ', 'seconds')
        task_obj.task_done = True

    @staticmethod
    def show_all_tasks():
        for key, value in Task.all_task.items():
            print(f'ID - {value.id}')
            print(f'Task - {value.task_name}')
            print(f'Created time - {value.created_time}')
            print(f'Updated time - {value.updated_time}')
            print(f'Completed - {value.task_done}')
            print(f'Completed time - {value.completed_time}')
            print()

    @staticmethod
    def show_incomplete_tasks():
        for key, value in Task.incomplete_tasks.items():
            print(f'ID - {value.id}')
            print(f'Task - {value.task_name}')
            print(f'Created time - {value.created_time}')
            print(f'Updated time - {value.updated_time}')
            print(f'Completed - {value.task_done}')
            print(f'Completed time - {value.completed_time}')
            print()

    @staticmethod
    def show_completed_tasks():
        for key, value in Task.completed_tasks.items():
            print(f'ID - {value.id}')
            print(f'Task - {value.task_name}')
            print(f'Created time - {value.created_time}')
            print(f'Updated time - {value.updated_time}')
            print(f'Completed - {value.task_done}')
            print(f'Completed time - {value.completed_time}')
            print()


i = 1

while True:
    print('1. Add New Task')
    print('2. Show All Task')
    print('3. Show Incomplete Tasks')
    print('4. Show Completed Tasks')
    print('5. Update Task')
    print('6. Mark A Task Completed')

    option = int(input('Enter Option : '))

    if option == 1:
        task_name = input('Enter New Task : ')
        print()
        task = Task(task_name)
        Task.all_task[i] = task
        Task.incomplete_tasks[i] = task
        Task.unchanged_tasks[i] = task
        i += 1
        print('Task Created Successfully')
        print()
    elif option == 2:
        print()
        Task.show_all_tasks()
    elif option == 3:
        print()
        if len(Task.incomplete_tasks) == 0:
            print('No incomplete task')
            print()
        else:
            Task.show_incomplete_tasks()
    elif option == 4:
        print()
        if len(Task.completed_tasks) == 0:
            print('No Completed Task')
            print()
        else:
            Task.show_completed_tasks()
    elif option == 5:
        print()
        if len(Task.unchanged_tasks) == 0:
            print('No task to update')
            print()
        else:
            print('Select Which Task To Update')
            print()
            for key, value in Task.unchanged_tasks.items():
                print(f'Task No - {key}')
                print(f'ID - {value.id}')
                print(f'Task - {value.task_name}')
                print(f'Created time - {value.created_time}')
                print(f'Updated time - {value.updated_time}')
                print(f'Completed - {value.task_done}')
                print(f'Completed time - {value.completed_time}')
                print()

            task_no = int(input('Enter Task No : '))
            nw_name = input('Enter new name : ')
            Task.unchanged_tasks[task_no].update_task(Task.unchanged_tasks[task_no], nw_name)
            Task.updated_tasks[task_no] = Task.unchanged_tasks[task_no]
            Task.unchanged_tasks.pop(task_no)

            print()
            print('Task Updated Successfully')
            print()
    elif option == 6:
        print()
        if len(Task.incomplete_tasks) == 0:
            print('No Task To Complete')
            print()
        else:
            print('Select Which Task To Complete')
            print()
            for key, value in Task.incomplete_tasks.items():
                print(f'Task No - {key}')
                print(f'ID - {value.id}')
                print(f'Task - {value.task_name}')
                print(f'Created time - {value.created_time}')
                print(f'Updated time - {value.updated_time}')
                print(f'Completed - {value.task_done}')
                print(f'Completed time - {value.completed_time}')
                print()

            task_no = int(input('Enter Task No : '))
            Task.incomplete_tasks[task_no].complete_task(Task.all_task[task_no])
            Task.completed_tasks[task_no] = Task.incomplete_tasks[task_no]
            Task.incomplete_tasks.pop(task_no)

            print()
            print('Task Completed Successfully')
            print()
