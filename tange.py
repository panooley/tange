import sys, configparser, re
from pathlib import Path
args = sys.argv

VERSION = 0.0
TODOS = []
DATA_DIR = ""
TODOS_FILE = ""

def print_bold(text: str, end="\n"):
    print(f"\033[1m{text}\033[0m", end=end)

def read_data():
    global DATA_DIR, TODOS, TODOS_FILE
    DATA_DIR = Path(Path.home()) / ".tange"
    Path(DATA_DIR).mkdir(parents=True, exist_ok=True)
    config_file = Path(DATA_DIR) / "config.ini"
    TODOS_FILE = Path(DATA_DIR) / "todos.txt"

    parser = configparser.ConfigParser()
    parser.read(config_file)

    with open(TODOS_FILE, 'r') as todos:
        for line in todos:
            TODOS.append(line.strip())

    with open(config_file, 'w') as file:
        parser.write(file)

def add_todo(arg: str):
    global TODOS_FILE
    if len(arg) == 0:
        print("Usage: tange add <content>")
        return
    
    content = " ".join(arg)

    if re.search(r'[\n\r]', content):
        print("Todo content cannot contain newline characters.")
        return

    if content in TODOS:
        print("todo already present")
        return
    else:
        with open(TODOS_FILE, "a") as file:
            if len(TODOS) > 0:
                file.write("\n" + content)
            else:
                file.write(content)
def list_todos(arg: str):
    if len(arg) == 0:
        print("Usage: tange list <number|all>")
        return
    
    if arg[0] == "all":
        length = len(TODOS)
    elif arg[0].isnumeric():
        length = min(int(arg[0]), len(TODOS))
    else:
        print("Usage: tange list <number|all>")
        return

    if len(TODOS) == 0:
        print("No todos present")

    for i in range(length):
        print(f"{i+1}) {TODOS[i]}")

def remove_todo(arg: str):
    if len(arg) == 0:
        arg.append("")
    if arg[0] == "0" or not (arg[0].isnumeric() or arg[0] == "all"):
        print("Usage: tange remove <index>|all")
        return
    if arg[0] == "all":
        print_bold("REMOVING ALL TODOS")
        option = input("Are you sure? (y/N): ")
        if option == "":
            option = "n"
        if option not in "yn":
            print("Abort.")
            return
        TODOS = []
    else:
        index = int(arg[0])
        if index > len(TODOS):
            print("index too big")
            return
        todo = TODOS[index-1]
        print_bold("REMOVING: ", "")
        print(todo)
        option = input("Are you sure? (y/N): ")
        if option == "":
            option = "n"
        if option not in "yn":
            print("Abort.")
            return
        TODOS.remove(todo)
    
    with open(TODOS_FILE, "w") as file:
        for i, t in enumerate(TODOS):
            if i < len(TODOS)-1:
                file.write(t + "\n")
            else:
                file.write(t)


    


def show_help_message():
    print("Simple todo app in the command line")
    print_bold("\nUSAGE")
    print("  tange <command> <subcommand> [flags]")
    print_bold("\nCORE COMMANDS")
    print("  add:       Create a new todo item\n  list:      See the todo list\n  remove:    Remove a todo item\n  config:    Show config directory")
    print_bold("\nFLAGS")
    print("  --version  Show tange version")
    print_bold("\nEXAMPLES")
    print("  $ tange add Finish project report")
    print("  $ tange remove 1")
    print("  $ tange list all")

read_data()

if args[len(args)-1] == "--version":
    print(f"tange version {VERSION}")
    print("https://github.com/panooley/tange")
    sys.exit()

if len(args) == 1:
    show_help_message()
    sys.exit()
else:
    command = args[1]
    match command:
        case "add":
            add_todo(args[2:])
        case "list":
            list_todos(args[2:])
        case "remove":
            remove_todo(args[2:])
        case "config":
            print(DATA_DIR)
        case _:
            print(f'unknown command "{command}"')
            print("\nUsage: tange <command> <subcommand> [flags]")
            print("\nAvailable commands:")
            print("  add\n  list\n  remove\n  config")
