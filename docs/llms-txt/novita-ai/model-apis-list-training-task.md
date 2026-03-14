# Source: https://novita.ai/docs/api-reference/model-apis-list-training-task.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# List LoRA Training Task

**This API retrieves information about all the user's training tasks.**

## Request Headers

<ParamField header="Content-Type" type="string" required={true}>
  Enum: `application/json`
</ParamField>

<ParamField header="Authorization" type="string" required={true}>
  Bearer authentication format, for example: Bearer \{\{API Key}}.
</ParamField>

## Query Parameters

<ParamField query="pagination.limit" type="integer" required={false}>
  The number of model records to query per request, within the range (0, 100].
</ParamField>

<ParamField query="pagination.cursor" type="string" required={false}>
  The pagination.cursor parameter specifies the record from which to start returning results. If it is empty, the results will start from the beginning. Generally, the content of the next page is obtained by passing the next\_cursor field value from the response packet.
</ParamField>

## Response

<ResponseField name="tasks" type="object[]" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="task_name" type="string" required={false}>
      The name of the training task.
    </ResponseField>

    <ResponseField name="task_id" type="string" required={false}>
      The unique identifier of the training task, which can be used to query the training status and results.
    </ResponseField>

    <ResponseField name="task_type" type="string" required={false}>
      The type of the training task.
    </ResponseField>

    <ResponseField name="task_status" type="string" required={false}>
      Represents the current status of a task, which is particularly useful for monitoring and managing the progress of training tasks. Each status indicates a specific phase in the task's lifecycle: UNKNOWN - The status of the task is not known or has not been updated yet; QUEUING - The task is in the queue waiting to be processed; TRAINING - The task is currently undergoing training processes; SUCCESS - The task has been completed successfully; CANCELED - The task was canceled before completion; FAILED - The task failed to complete successfully due to an error or issue.<br />
      Enum: `UNKNOWN`, `QUEUING`, `TRAINING`, `SUCCESS`, `CANCELED`, `FAILED`
    </ResponseField>

    <ResponseField name="created_at" type="integer" required={false}>
      The timestamp of when the task was created.
    </ResponseField>

    <ResponseField name="models" type="object[]" required={false}>
      <Expandable title="properties" defaultOpen={false}>
        <ResponseField name="model_name" type="string" required={false}>
          The name of the model.
        </ResponseField>

        <ResponseField name="model_status" type="string" required={false}>
          The status of the model. When the model is being deployed, the status will be `DEPLOYING`, and when the model is serving, the status will be `SERVING`.<br />
          Enum: `DEPLOYING`, `SERVING`
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="pagination" type="object" required={false}>
  <Expandable title="properties" defaultOpen={false}>
    <ResponseField name="next_cursor" type="string" required={false} />
  </Expandable>
</ResponseField>

## Example

In this step, we can obtain all the information about trained models.

```bash  theme={"system"}
curl --location --request GET 'https://api.novita.ai/v3/training?pagination.limit=10&pagination.cursor=c_0' \
--header 'Authorization: Bearer {{API Key}}'
```

`Response:`

```js  theme={"system"}
{
    "tasks": [
        {
            "task_name": "test_01",
            "task_id": "a0c4cc90-0296-4972-a1d8-e6e227daf094",
            "task_type": "subject",
            "task_status": "SUCCESS",
            "created_at": 1699325415,
            "models": [
                {
                    "model_name": "model_1699325939_E83A88DAC5.safetensors",
                    "model_status": "SERVING"
                }
            ]
        },
        {
            "task_name": "test_02",
            "task_id": "51e9bf41-8f7a-464d-b5ad-2fa217a1ec93",
            "task_type": "subject",
            "task_status": "SUCCESS",
            "created_at": 1699267268,
            "models": [
                {
                    "model_name": "model_1699267603_27F0D9C81C.safetensors",
                    "model_status": "SERVING"
                }
            ]
        },
        {
            "task_name": "test_03",
            "task_id": "7bd205ab-63e9-452b-9a66-39c597000eaa",
            "task_type": "subject",
            "task_status": "FAILED",
            "created_at": 1699264338,
            "models": []
        }
    ],
    "pagination": {
        "next_cursor": "c_10"
    }
}
```

* `task_name`: The name of the training task.
* `task_id`: The unique identifier of the training task, which can be used to query the training status and results.
* `task_type`: The type of the training task.
* `task_status`: The status of the training task. Enum: `UNKNOWN`, `QUEUING`, `TRAINING`, `SUCCESS`, `CANCELED`, `FAILED`.
* `created_at`: The timestamp of when the training task was created.
* `models`: The trained models.
* `model_name`: The name of the model.
* `model_status`: The status of the model. Enum: `DEPLOYING`, `SERVING`.


Built with [Mintlify](https://mintlify.com).