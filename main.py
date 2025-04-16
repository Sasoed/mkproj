import sys
import json
import os

args = sys.argv

if args.__len__() < 3 or args[1] == "-h" or args[1] == "--help":
    print("mkproj [options] name_of_project\n-extension (py for example) \n-F to disable making directories for different extensions\nMore on GitHub : ")
    sys.exit()




projects_dir = "/home/seva/projects/"
make_dirs = True
flag = str(args[1])[1:]
config = "/home/seva/projects/python/mkproj/config.json"
file = ""
dir_tc = ""
name = ""



if args.__len__() == 3 and args[2] == "-F":
    make_dirs = False
    name = args[3]


if make_dirs == True:
    name = args[2]
    if os.path.isfile(config) == False:
        with open(config, "w") as file:
            file.write("{}")
    with open(config, "r") as file:
        config = json.load(file)
    if flag in config:
        dir_tc = config[flag]

if dir_tc != "":
    os.makedirs(os.path.join(projects_dir, dir_tc, name), exist_ok=True)
    file = os.path.join(projects_dir, dir_tc,name, name+"."+flag)
else:
    os.makedirs(os.path.join(projects_dir, name))
    file = os.path.join(projects_dir,name, name+"."+flag)

if os.path.exists(file) == False:
    with open(file, "w") as f:
        f.write("")
else:
    print("File exist")
    sys.exit()
print(f"File was created in {file}")
