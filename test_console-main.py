#!/usr/bin/python3
import inspect
import io
import sys
import cmd
import shutil
import os
import console

# Clean up file storage
file_path = "file.json"
if not os.path.exists(file_path):
    try:
        from models.engine.file_storage import FileStorage
        file_path = FileStorage._FileStorage__file_path
    except ImportError:
        pass

if os.path.exists(file_path):
    os.remove(file_path)

# Backup console file
tmp_console_file = "tmp_console_main.py"
if os.path.exists(tmp_console_file):
    shutil.copy(tmp_console_file, "console.py")
shutil.copy("console.py", tmp_console_file)

# Backup models/__init__.py file
tmp_init_file = "models/tmp__init__.py"
if os.path.exists(tmp_init_file):
    shutil.copy(tmp_init_file, "models/__init__.py")
shutil.copy("models/__init__.py", tmp_init_file)

# Overwrite models/__init__.py file with switch_to_file_storage.py
switch_file = "switch_to_file_storage.py"
if os.path.exists(switch_file):
    shutil.copy(switch_file, "models/__init__.py")

# Update console to remove "__main__"
with open(tmp_console_file, "r") as file_i:
    console_lines = file_i.readlines()
    with open("console.py", "w") as file_o:
        in_main = False
        for line in console_lines:
            if "__main__" in line:
                in_main = True
            elif in_main:
                if "cmdloop" not in line:
                    file_o.write(line.lstrip("    "))
            else:
                file_o.write(line)

# Create console object
console_obj = "HBNBCommand"
for name, obj in inspect.getmembers(console):
    if inspect.isclass(obj) and issubclass(obj, cmd.Cmd):
        console_obj = obj

my_console = console_obj(
    stdout=io.StringIO(),
    stdin=io.StringIO()
)
my_console.use_rawinput = False


# Execute command function
def exec_command(my_console, the_command, last_lines=1):
    my_console.stdout = io.StringIO()
    real_stdout = sys.stdout
    sys.stdout = my_console.stdout
    my_console.onecmd(the_command)
    sys.stdout = real_stdout
    lines = my_console.stdout.getvalue().split("\n")
    return "\n".join(lines[(-1 * (last_lines + 1)):-1])


# Tests
state_name = "California"
result = exec_command(my_console, f"create State name=\"{state_name}\"")
if not result:
    print("FAIL: No ID retrieved")

state_id = result

city_name = "San Francisco is super cool"
city_name = city_name.replace(' ', '_')
result = exec_command(
    my_console,
    f"create City state_id=\"{state_id}\" name=\"{city_name}\""
)
if not result:
    print("FAIL: No ID retrieved")

city_id = result

user_email = "my@me.com"
user_pwd = "pwd"
user_fn = "FN"
user_ln = "LN"
result = exec_command(
    my_console,
    f"create User email=\"{user_email}\" password=\"{user_pwd}\" "
    f"first_name=\"{user_fn}\" last_name=\"{user_ln}\""
)
if not result:
    print("FAIL: No ID retrieved")

user_id = result

place_name = "My house"
place_desc = "no description yet"
place_nb_rooms = 4
place_nb_bath = 0
place_max_guests = -3
place_price = 100
place_lat = -120.12
place_lon = 0.41921928
place_name = place_name.replace(' ', '_')
place_desc = place_desc.replace(' ', '_')
result = exec_command(
    my_console,
    f"create Place city_id=\"{city_id}\" user_id=\"{user_id}\" "
    f"name=\"{place_name}\" description=\"{place_desc}\" "
    f"number_rooms={place_nb_rooms} number_bathrooms={place_nb_bath} "
    f"max_guest={place_max_guests} price_by_night={place_price} "
    f"latitude={place_lat} longitude={place_lon}"

)
if not result:
    print("FAIL: No ID retrieved")

place_id = result

result = exec_command(my_console, f"show Place {place_id}")
if not result:
    print("FAIL: empty output")

if "[Place]" not in result or place_id not in result:
    print(f"FAIL: wrong output format: \"{result}\"")

if "city_id" not in result or city_id not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "user_id" not in result or user_id not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "name" not in result or place_name not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "description" not in result or place_desc not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "number_rooms" not in result or str(place_nb_rooms) not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "number_bathrooms" not in result or str(place_nb_bath) not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "max_guest" not in result or str(place_max_guests) not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "price_by_night" not in result or str(place_price) not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "latitude" not in result or str(place_lat) not in result:
    print(f"FAIL: missing new information: \"{result}\"")

if "longitude" not in result or str(place_lon) not in result:
    print(f"FAIL: missing new information: \"{result}\"")

print("OK", end="")
