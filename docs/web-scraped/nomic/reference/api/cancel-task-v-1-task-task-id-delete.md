# Cancel a task

Source: https://docs.nomic.ai/reference/api/cancel-task-v-1-task-task-id-delete

# Cancel a task

```
DELETE /v1/task/:task_id
```

## /v1/task/:task_id

Cancel a task.

## Request​

### Path Parameters

Path Parameters

## Responses​

- 204
- 403
- 422
- 501
The task was successfully cancelled.

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

An attempt was made to cancel a task that is not a parse task.

- application/json
- Schema
- Example (from schema)
- Example
Schema

any

```
{  "status_code": 501,  "detail": "Cancellation only implemented for parse tasks."}
```

```
{  "status_code": 501,  "detail": "Cancellation only implemented for parse tasks."}
```

