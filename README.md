# mkproj

## Usage

```bash
{your alias or different way to run script} -h / --help
```
Show a short help message.

```bash
-{extension of file}
```
Specifies the file extension to be added to the end of the file name.  
If directory creation is enabled and the extension exists in `config.json`, a directory with the corresponding name will also be created.

```bash
-F
```
Disables directory creation. Project files will be created in the directory specified by `projects_dir`.

---

## Settings (in `main.py`)

- `projects_dir` — path to the directory where projects will be stored.  
  If directory creation is disabled, files will be created directly in this directory.  
  Otherwise, a subdirectory based on the extension will be created.

- `config` — path to the `config.json` file.

---

## config.json

Configuration file for mapping file extensions to directories.  
Syntax:

```json
{
  "extension": "name_of_extension_folder"
}
```

**Example:**

```json
{
  "py": "python"
}
```
