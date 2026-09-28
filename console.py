#!/usr/bin/python3
"""Defines the HBNBCommand class, the entry point of the interpreter."""
import cmd
import shlex
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for managing AirBnB clone objects."""

    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "State": State,
               "City": City, "Amenity": Amenity, "Place": Place,
               "Review": Review}

    def _parse(self, arg):
        """Split arg into words, keeping double-quoted text together."""
        try:
            return shlex.split(arg)
        except ValueError:
            return arg.split()

    def _find_key(self, args):
        """Check class name and id; return the storage key or None."""
        if len(args) == 0:
            print("** class name missing **")
            return None
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return None
        if len(args) < 2:
            print("** instance id missing **")
            return None
        key = "{}.{}".format(args[0], args[1])
        if key not in storage.all():
            print("** no instance found **")
            return None
        return key

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance, save it and print its id.
        Usage: create <class name>
        """
        args = self._parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            obj = self.classes[args[0]]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """Print the string representation of an instance.
        Usage: show <class name> <id>
        """
        key = self._find_key(self._parse(arg))
        if key:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """Delete an instance and save the change to the JSON file.
        Usage: destroy <class name> <id>
        """
        key = self._find_key(self._parse(arg))
        if key:
            del storage.all()[key]
            storage.save()

    def do_all(self, arg):
        """Print all instances as a list of strings.
        Usage: all or all <class name>
        """
        args = self._parse(arg)
        if len(args) > 0 and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        result = []
        for key, obj in storage.all().items():
            if len(args) == 0 or key.split(".")[0] == args[0]:
                result.append(str(obj))
        print(result)

    def do_update(self, arg):
        """Add or update one attribute of an instance.
        Usage: update <class name> <id> <attribute name> "<value>"
        """
        args = self._parse(arg)
        key = self._find_key(args)
        if not key:
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        obj = storage.all()[key]
        name = args[2]
        value = args[3]
        if hasattr(obj, name):
            try:
                value = type(getattr(obj, name))(value)
            except (ValueError, TypeError):
                pass
        else:
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass
        setattr(obj, name, value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
