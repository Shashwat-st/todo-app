import functions
import time

now = time.strftime("%d %b, %Y %H:%M:%S")
print('It is', now)

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = functions.get_todos()

            todos[number - 1] = input("Enter the new todo: ") + '\n'

            functions.write_todos(todos)

        except ValueError:
            print("Your Command is not Valid!")
            continue

    elif user_action.startswith('complete'):
        try:
            todos = functions.get_todos()

            number = int(user_action[9:])
            index = number - 1
            removed_todo = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos)

            print(f"Todo {removed_todo} was removed from the list!")
        except IndexError:
            print("There is No Item with that number!")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("Command is not Valid!")

print("Bye!")
