# Source: https://docs.curator.interworks.com/curator_api/api_docs/integration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Integration

> Integration API endpoints for managing commands and custom integrations

## /integration/commands

Returns a list of all commands

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": [
            {
                "id": 1,
                "name": "Test Command",
                "description": "This command refreshes extracts",
                "type": "tabcmd",
                "arguments": "",
                "schedule": "",
                "created": {
                    "date": "2017-08-17 21:08:02.000000",
                    "timezone_type": 3,
                    "timezone": "UTC"
                },
                "updated": {
                    "date": "2017-08-17 21:08:02.000000",
                    "timezone_type": 3,
                    "timezone": "UTC"
                }
            }
        ]
    }
```

## /integration/runCommand

Runs the specified command and returns its output.

**Parameters:**

**id**
Identifier of the command to run.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": "Status not provided by command"
    }
```

## /integration/runScript

Runs the specified script and returns its output.

**Parameters:**

**id**
Identifier of the script to run.

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": "Status not provided by script"
    }
```

## /integration/scripts

Returns a list of all scripts

**Returns:**

array

**Example Response:**

```JSON  theme={null}
    {
        "result": "Success",
        "msg": [
            {
                "id": 1,
                "name": "Test Script",
                "description": "This Script Does a Thing",
                "language": "python",
                "arguments": "",
                "schedule": "",
                "created": {
                    "date": "2017-08-17 21:11:44.000000",
                    "timezone_type": 3,
                    "timezone": "UTC"
                },
                "updated": {
                    "date": "2017-08-17 21:11:44.000000",
                    "timezone_type": 3,
                    "timezone": "UTC"
                }
            }
        ]
    }
```

## /integration/apiRelay

Kicks off an API relay request

**Returns:**

array
