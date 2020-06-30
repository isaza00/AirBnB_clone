#!/usr/bin/python3
"""
Write a program called console.py
that contains the entry point of the command interpreter:

    You must use the module cmd
    Your class definition must be: class HBNBCommand(cmd.Cmd):
    Your command interpreter should implement:
        quit and EOF to exit the program
        help (this action is provided by default by
        cmd but you should keep it updated and documented
        as you work through tasks)
        a custom prompt: (hbnb)
        an empty line + ENTER shouldn’t execute anything
    Your code should not be executed when imported
"""

import cmd
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """ class for console """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """End of file"""
        return True

    def do_create(self, line):
        """
        create: Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        If the class name is missing,
        print ** class name missing ** (ex: $ create)
        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ create MyModel)
        """
        lista = line.split()
        classes = ["User", "State", "City", "Place",
                   "Amenity", "Review", "BaseModel"]

        if not lista:
            print("** class name missing **")
        else:
            if lista[0] in classes:
                new_model = eval(lista[0] + "()")
                new_model.save()
                print(new_model.id)
            else:
                print("** class doesn't exist **")

    def do_show(self, line):
        """
        show: Prints the string representation of
        an instance based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234.

        If the class name is missing,
        print ** class name missing ** (ex: $ show)

        If the class name doesn’t exist,
        print ** class doesn't exist ** (ex: $ show MyModel)

        If the id is missing,
        print ** instance id missing ** (ex: $ show BaseModel)

        If the instance of the class name doesn’t exist for the id,
        print ** no instance found ** (ex: $ show BaseModel 121212)
        """
        found = 0
        dics = (storage.all())
        lista = line.split()

        if not lista:
            print("** class name missing **")
        else:
            for key in dics:
                for sub_key in dics[key]:
                    if sub_key == "__class__":
                        if dics[key][sub_key] == lista[0]:
                            found = 1

            if found == 0:
                print("** class doesn't exist **")
            else:
                if len(lista) == 1:
                    print("** instance id missing **")
                elif len(lista) > 1:
                    found = 0
                    for key in dics:
                        for sub_key in dics[key]:
                            if sub_key == "id":
                                if dics[key][sub_key] == lista[1]:
                                    found = 1
                    if found == 0:
                        print("** no instance found **")
                    else:
                        key = lista[0] + "." + lista[1]
                        if key in dics:
                            dic_model = (dics[key])
                            model = eval(lista[0]+"(**dic_model)")
                            print(model)

    def do_destroy(self, line):
        """
            destroy: Deletes an instance based on the class name and id
            (save the change into the JSON file).
            Ex: $ destroy BaseModel 1234-1234-1234.
            If the class name is missing, print ** class name missing **
            (ex: $ destroy)
            If the class name doesn’t exist, print ** class doesn't exist **
            (ex:$ destroy MyModel)
            If the id is missing, print ** instance id missing **
            (ex: $ destroy BaseModel)
            If the instance of the class name doesn’t exist for the id, print
            ** no instance found ** (ex: $ destroy BaseModel 121212)
        """
        found = 0
        dics = (storage.all())
        lista = line.split()

        if not lista:
            print("** class name missing **")
        else:
            for key in dics:
                for sub_key in dics[key]:
                    if sub_key == "__class__":
                        if dics[key][sub_key] == lista[0]:
                            found = 1

            if found == 0:
                print("** class doesn't exist **")
            else:
                if len(lista) == 1:
                    print("** instance id missing **")
                elif len(lista) > 1:
                    found = 0
                    for key in dics:
                        for sub_key in dics[key]:
                            if sub_key == "id":
                                if dics[key][sub_key] == lista[1]:
                                    found = 1
                    if found == 0:
                        print("** no instance found **")
                    else:
                        key = lista[0] + "." + lista[1]
                        if key in dics:
                            dics.pop(key, None)
                            with open(FileStorage._FileStorage__file_path,
                                      mode="w", encoding='utf-8') as file:
                                json.dump(dics, file)

    def do_all(self, line):
        """
            all: Prints all string representation of
            all instances based or not on the class name.
            Ex: $ all BaseModel or $ all.
            The printed result must be a list of strings
            (like the example below)
            If the class name doesn’t exist,
            print ** class doesn't exist ** (ex: $ all MyModel)
        """
        found = 0
        dics = (storage.all())
        lista = line.split()
        new_list = []

        if len(lista) > 0:
            for key in dics:
                for sub_key in dics[key]:
                    if sub_key == "__class__":
                        if dics[key][sub_key] == lista[0]:
                            found = 1

        if len(lista) == 0:
            for key in dics:
                dic_model = (dics[key])
                model = eval(key.split(".")[0]+"(**dic_model)")
                new_list.append(model.__str__())
            print(new_list)

        elif found == 1:
            for key in dics:
                dic_model = (dics[key])
                if key.split(".")[0] == lista[0]:
                    model = eval(lista[0]+"(**dic_model)")
                    new_list.append(model.__str__())
            print(new_list)

        elif found == 0 and len(lista) > 0:
            print("** class doesn't exist **")

    def do_update(self, line):
        """
            update: Updates an instance based on the class name and
            id by adding or updating attribute
            (save the change into the JSON file).
            Ex: $ update BaseModel 1234-1234-1234
            email "aibnb@holbertonschool.com".

            Usage: update <class name> <id>
            <attribute name> "<attribute value>"
            Only one attribute can be updated at the time

            You can assume the attribute name is valid
            (exists for this model)

            The attribute value must be casted to the attribute type

            All other arguments should not be used
            (Ex: $ update BaseModel 1234-1234-1234
            email "aibnb@holbertonschool.com"
            first_name "Betty" = $ update BaseModel 1234-1234-1234
            email "aibnb@holbertonschool.com")
            id, created_at and updated_at cant’ be updated.
            You can assume they won’t be passed in the update command

            Only “simple” arguments can be updated: string, integer and float.
            You can assume nobody will try to update list of ids or datetime
        """
        found = 0
        dics = (storage.all())
        lista = line.split()

        if not lista:
            print("** class name missing **")
        else:
            for key in dics:
                for sub_key in dics[key]:
                    if sub_key == "__class__":
                        if dics[key][sub_key] == lista[0]:
                            found = 1

            if found == 0:
                print("** class doesn't exist **")
            else:
                if len(lista) == 1:
                    print("** instance id missing **")
                elif len(lista) > 1:
                    found = 0
                    for key in dics:
                        for sub_key in dics[key]:
                            if sub_key == "id":
                                if dics[key][sub_key] == lista[1]:
                                    found = 1
                    if found == 0:
                        print("** no instance found **")
                    else:
                        if len(lista) == 2:
                            print("** attribute name missing **")
                        elif len(lista) == 3:
                            print("** value missing **")
                        else:
                            key = lista[0] + "." + lista[1]
                            dic_model = dics[key]
                            dics.pop(key, None)
                            modelo = eval(lista[0]+"(**dic_model)")
                            value = lista[3][1:-1]
                            if type(getattr(modelo, lista[2])) == int:
                                value = int(lista[3][1:-1])
                            elif type(getattr(modelo, lista[2])) == float:
                                value = float(lista[3][1:-1])
                            setattr(modelo, lista[2], value)
                            modelo.save()

    def default(self, line):
        cmds = {"create": self.do_create, "show": self.do_show,
                "all": self.do_all, "destroy": self.do_destroy,
                "update": self.do_update}
        lista = line.split(".", 1)
        modelo = lista[0]
        semi_cmd = lista[1].split("(", 1)
        cmd = semi_cmd[0]
        args = semi_cmd[1].split(", ")

        if cmd in cmds:
            if len(args) >= 3:
                linea = modelo + " " + args[0][1:-1] +
                " " + args[1][1:-1] + " " + args[2][0:-1]
            elif len(args) == 2:
                linea = modelo + " " + args[0][1:-1] + " " + args[1][1:-1]
            elif len(args) == 1:
                linea = modelo + " " + args[0][1:-2]
            print(linea)
            cmds[cmd](linea)
        else:
            print("*** Unknown syntax:", line)


if __name__ == "__main__":
    """To use the file as
    the console itself"""
    HBNBCommand().cmdloop()
