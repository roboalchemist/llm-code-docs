# Source: https://virustotal.readme.io/reference/file-behaviour-object-files-copied.md

# files_copied

Object that describes a file copy or move.

`files_copied` contains a list of files that were copied from one location to another. It is a list, every item of the list containing the following fields:

* `destination` <*string*> full path of the destination file.
* `source` <*string*> full path of the source file.

```json Copied files
{
    "data": {
        "attributes": {
            "files_copied": [
                {
                    "destination": "<string>",
                    "source": "<string>"
                },...
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "files_copied": [
                {
                    "destination": "C:\\Program Files (x86)\\blablabla\\blablabla.exe",
                    "source": "C:\\Users\\FD1HVy\\Downloads\\blablabla.exe"
                }
            ]
        }
    }
}
```