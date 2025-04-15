# mkproj
Usage: {your alias or different way to run script} -h / --help to small help
                                                   -{extension of file} extenssion of file, that will be add in end of name of file and if making directories True and this exstension exist in config.json also make directory with name from config.json
                                                   -F disable making directories, your projects will be in your projects directory
Setting (some variables in main.py): projects_dir -- path to yours directory for projectts, if making directories disabled files will be create in this directory, else directory of extension will be create in this directory
                                     config -- path to config.json file
Conffig.json: file to do directoriess for extensions, sintacsis --  "extension":"name_of_extension_folder" for example -- "py":"python"
