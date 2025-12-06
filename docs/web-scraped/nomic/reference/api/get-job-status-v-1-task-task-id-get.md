# Get the status of a task

Source: https://docs.nomic.ai/reference/api/get-job-status-v-1-task-task-id-get

# Get the status of a task

```
GET /v1/task/:task_id
```

## /v1/task/:task_id

Get the status of a task (parsing, extraction).

## Request​

### Path Parameters

Path Parameters

## Responses​

- 200
- 403
- 422
The status of the task.

- application/json
- Schema
- Example (from schema)
Schema

Possible values: [COMPLETED, FAILED, BUILDING, WAITING]

```
COMPLETED
```

```
FAILED
```

```
BUILDING
```

```
WAITING
```

The status of the task.

error

object

An error message if the task failed.

anyOf

- MOD1
string

result

object

The result of the task.

anyOf

- CompletedTaskResponse
The ID of the task.

The time taken to complete the task, in seconds.

A URL to access the results (e.g., parsed file, extracted information).

```
{  "status": "COMPLETED",  "error": "string",  "result": {}}
```

The user is not authorized to perform this action.

- application/json
- Schema
- Example (from schema)
- Example
Schema

any

```
{  "status_code": 403,  "detail": "The user is not authorized to perform this action."}
```

```
{  "status_code": 403,  "detail": "The user is not authorized to perform this action."}
```

Validation Error

- application/json
- Schema
- Example (from schema)
Schema

detail

object[]

- Array [
Array [

loc

object[]

required

- Array [
Array [

anyOf

- MOD1
- MOD2
string

integer

- ]
]

- ]
]

```
{  "detail": [    {      "loc": [        "string",        0      ],      "msg": "string",      "type": "string"    }  ]}
```

