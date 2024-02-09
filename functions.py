FILEPATH = "todos.txt"
def get_todos(filepath=FILEPATH):
    """ Read a text file and return the list of to_do
    """
    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


# print(help(get_todos)) comments in the code use """"""
def write_todos(todos_arg, filepath=FILEPATH, ):
    """Write the to_do items list in the text file."""
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

#print(__name__)
if __name__ == "__main__":
    print("Hello from functions")
    print(get_todos())
