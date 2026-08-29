FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    with open(filepath, "r") as file:
        todos = file.readlines()
        return todos


def write_todos(todo, filepath=FILE_PATH):
    with open(filepath, "w") as file:
        file.writelines(todo)