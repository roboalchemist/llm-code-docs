# Source: https://virustotal.readme.io/reference/process.md

# processes_tree

Created processes during the execution of a given file.

`processes_tree` contains al list of **created processes structured in a recursive way allowing to build a process tree.**.

It is a list, every item of the list containing the following attributes:

* `children`: <*list of dictionaries*> contains processes created by a given process. Every subfield contains the same fields (`children`, `name`, `process_id` and `time_offset`) allowing to build a recursive process tree.
* `name`: <*string*> process name.
* `process_id`: <*string*> ID of the process.
* `time_offset`: <*integer*> first observed. Seconds since execution start.

```json Process tree
{
    "data": {
        "attributes": {
            "processes_tree": [
                {
                    "children": [
                        {
                            "children": [...],
                            "name": "<string>",
                            "process_id": "<string>",
                            "time_offset": <int>
                        },...
                    ],
                    "name": "<string>",
                    "process_id": "<string>",
                    "time_offset": <int>
                }
            ]
        }
    }
}
```
```json Example
{
    "data": {
        "attributes": {
            "processes_tree": [
                {
                    "children": [
                        {
                            "name": "com.blabla.blabla",
                            "process_id": "15530"
                        },
                        {
                            "name": "com.blabla.blabla",
                            "process_id": "15623"
                        }
                    ],
                    "name": "blabla",
                    "process_id": "8145"
                }
            ]
        }
    }
}
```