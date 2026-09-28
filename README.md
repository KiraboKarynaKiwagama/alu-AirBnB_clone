# AirBnB Clone - The Console

## Description
This is the first step of an AirBnB clone project: a command interpreter
to manage AirBnB objects (BaseModel, User, and later State, City, Place,
etc.). It lets you create, store, and manipulate them through a custom
shell. Objects are saved to a JSON file (`file.json`) so they persist
between runs.

## Command Interpreter

### How to start it
Interactive mode:

    $ ./console.py
    (hbnb)

Non-interactive mode:

    $ echo "help" | ./console.py

### How to use it
Type a command at the `(hbnb)` prompt. Available classes: `BaseModel`, `User`, `State`, `City`, `Amenity`, `Place`, `Review`.

| Command | Description |
|---------|-------------|
| `help` | Lists all commands, or `help <command>` for details on one |
| `create <class>` | Creates a new instance, saves it, and prints its id |
| `show <class> <id>` | Prints the string representation of an instance |
| `destroy <class> <id>` | Deletes an instance and saves the change |
| `all [class]` | Prints all instances, or all instances of one class |
| `update <class> <id> <attr> "<value>"` | Updates one attribute of an instance |
| `quit` | Exits the program |
| `EOF` | Exits the program (Ctrl+D) |

If something is wrong, the console prints one of these messages:
`** class name missing **`, `** class doesn't exist **`,
`** instance id missing **`, `** no instance found **`,
`** attribute name missing **`, `** value missing **`.

### Examples
Show the commands:

    $ ./console.py
    (hbnb) help

    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

    (hbnb) quit
    $

Create, show, update, and destroy a User:

    (hbnb) create User
    38f22813-2753-4d42-b37c-57a17f1e4f88
    (hbnb) show User 38f22813-2753-4d42-b37c-57a17f1e4f88
    [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {...}
    (hbnb) update User 38f22813-2753-4d42-b37c-57a17f1e4f88 first_name "Betty"
    (hbnb) all User
    ["[User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {...}"]
    (hbnb) destroy User 38f22813-2753-4d42-b37c-57a17f1e4f88
    (hbnb) show User 38f22813-2753-4d42-b37c-57a17f1e4f88
    ** no instance found **
    (hbnb) quit

## File Structure
- `console.py`: the command interpreter
- `models/base_model.py`: the BaseModel parent class
- `models/user.py`: the User class
- `models/engine/file_storage.py`: saves and loads objects as JSON
- `tests/`: unit tests

## Authors
See the AUTHORS file.