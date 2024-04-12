#!/usr/bin/python3
"""HBNB Console

This module implements the command line interface for the HBNB project,
which allows users to interact with the application's data models.
"""

import cmd
from datetime import datetime
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex  # for splitting the line along spaces except in double quotes

# Dictionary mapping class names to their corresponding model classes
classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNB Command Line Interface

    This class provides the command line interface for interacting
    with the HBNB project's data models.
    """

    prompt = '(hbnb) '  # Command prompt for the console

    def do_EOF(self, arg):
        """EOF command to exit the console"""
        return True

    def emptyline(self):
        """ Overwriting the emptyline method """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def _parse_value(self, value):
        """Parse value to proper type"""
        if value[0] == value[-1] == '"':
            return value[1:-1].replace('_', ' ')
        elif '.' in value:
            try:
                return float(value)
            except ValueError:
                return value
        else:
            try:
                return int(value)
            except ValueError:
                return value

    def _parse_param(self, param):
        """Parse parameter to key-value pair"""
        if '=' in param:
            key, value = param.split('=', 1)
            return key, self._parse_value(value)
        else:
            return None, None

    def do_create(self, arg):
        """Creates a new instance of a class with given parameters"""
        try:
            args = shlex.split(arg)
            if not args:
                raise SyntaxError("** class name missing **")
            class_name = args[0]
            if class_name not in classes:
                raise NameError("** class doesn't exist **")

            kwargs = {}
            for param in args[1:]:
                key, value = self._parse_param(param)
                if key is not None and value is not None:
                    kwargs[key] = value

            instance = classes[class_name](**kwargs)
            instance.save()
            print(instance.id)

        except Exception as e:
            print(e)

    def do_show(self, arg):
        """Prints an instance as a string based on the class and id"""
        try:
            args = shlex.split(arg)
            if not args:
                raise SyntaxError("** class name missing **")
            class_name = args[0]
            if class_name not in classes:
                raise NameError("** class doesn't exist **")
            if len(args) < 2:
                raise IndexError("** instance id missing **")
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key in models.storage.all():
                print(models.storage.all()[key])
            else:
                raise KeyError("** no instance found **")

        except Exception as e:
            print(e)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        try:
            args = shlex.split(arg)
            if not args:
                raise SyntaxError("** class name missing **")
            class_name = args[0]
            if class_name not in classes:
                raise NameError("** class doesn't exist **")
            if len(args) < 2:
                raise IndexError("** instance id missing **")
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key in models.storage.all():
                del models.storage.all()[key]
                models.storage.save()
            else:
                raise KeyError("** no instance found **")

        except Exception as e:
            print(e)

    def do_all(self, arg):
        """Prints string representations of instances"""
        try:
            args = shlex.split(arg)
            obj_list = []

            if not args:
                obj_dict = models.storage.all()
            else:
                class_name = args[0]
                if class_name not in classes:
                    raise NameError("** class doesn't exist **")
                obj_dict = models.storage.all(classes[class_name])

            for key in obj_dict:
                obj_list.append(str(obj_dict[key]))

            print("[{}]".format(", ".join(obj_list)))

        except Exception as e:
            print(e)

    def do_update(self, arg):
        """Update an instance based on the class name, id, attribute & value"""
        try:
            args = shlex.split(arg)
            if not args:
                raise SyntaxError("** class name missing **")
            class_name = args[0]
            if class_name not in classes:
                raise NameError("** class doesn't exist **")
            if len(args) < 2:
                raise IndexError("** instance id missing **")
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            if key not in models.storage.all():
                raise KeyError("** no instance found **")
            if len(args) < 3:
                raise AttributeError("** attribute name missing **")
            if len(args) < 4:
                raise ValueError("** value missing **")

            attribute_name = args[2]
            new_value = self._parse_value(args[3])
            setattr(models.storage.all()[key], attribute_name, new_value)
            models.storage.all()[key].save()

        except Exception as e:
            print(e)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
