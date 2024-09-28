import sys, platformdirs, configparser
from pathlib import Path
args = sys.argv

VERSION = 0.0

def print_bold(text: str):
    print(f"\033[1m{text}\033[0m")

def read_config():
    config_dir = platformdirs.user_config_dir("tange")
    Path(config_dir).mkdir(parents=True, exist_ok=True)
    config_file = Path(config_dir) / "config.ini"
    # if not config_file.exists():
        # with open(config_file, 'w') as f:
            # f.write(f"[settings]\nversion = {}\n")
    
    parser = configparser.ConfigParser()
    parser.read(config_file)

    with open(config_file, 'w') as file:
        parser.write(file)

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
read_config()

if args[len(args)-1] == "--version":
    print(f"tange version {VERSION}")
    print("https://github.com/panooley/tange")
    quit()

if len(args) == 1:
    show_help_message()
    quit()
else:
    command = args[1]
    match command:
        case "add":
            pass
        case "list":
            pass
        case "remove":
            pass
        case "config":
            pass
        case _:
            print(f'unknown command "{command}"')
            print("\nUsage: tange <command> <subcommand> [flags]")
            print("\nAvailable commands:")
            print("  add\n  list\n  remove\n  config")
