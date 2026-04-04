# Source: https://docs.mystic.ai/docs/running-a-pipeline.md

# Inference

Different options for running your pipeline

## Running a pipeline using the Python SDK

The SDK provides a way to run your pipeline directly in Python by using the `run_pipeline` function:

```python
from pipeline.cloud.pipelines import run_pipeline

pointer = "my_user/my_pipeline:v1"

input_data = ["my_input_string", 5]

result = run_pipeline(pointer, *input_data)

print(result.outputs_formatted())
```

The format of the `input_data` argument will vary depending on what inputs your pipeline expects.

## Calling the API directly

You can also run your pipeline by calling the Mystic API directly with a tool like [curl](https://curl.se/):

```shell shell
curl -X POST 'https://www.mystic.ai/v4/runs' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
	"pipeline": "my_user/my_pipeline:v1",
	"inputs": 
		[
			{"type":"string","value":"my_input_string"},
			{"type":"integer","value":5}
		]
	}
'
```

## Asynchronous runs

By default, running a pipeline is a synchronous operation, i.e. it will wait until the API returns a result. If your pipeline takes a while to run, you may find it more convenient to execute runs asynchronously. This means, you can submit a run request and get a run ID back immediately. You can then query the API to check the status of the run.

Here's how you would do this using the Python SDK:

```python
from pipeline.cloud.pipelines import run_pipeline
from pipeline.cloud.runs import get_run
from pipeline.cloud.schemas.runs import RunState

pointer = "my_pipeline_id"
input_data = ["my input string"]

initial_result = run_pipeline(pointer, *input_data, async_run=True)
run_id = initial_result.id

# wait for 10s and check status of run
time.sleep(10)
result = get_run(run_id)
print(f"State = {result.state}")
```

You can see we call `run_pipeline()` with `async_run=True`.

The Python SDK also has a `poll_for_run_completion` helper function to poll the run until it completes. Here's an example of how you can use it:

```python
from pipeline.cloud.pipelines import run_pipeline
from pipeline.cloud.runs import poll_for_run_completion
from pipeline.cloud.schemas.runs import RunState

pointer = "my_pipeline_id"
input_data = ["my input string"]

initial_result = run_pipeline(pointer, *input_data, async_run=True)
run_id = initial_result.id

result = poll_for_run_completion(run_id, timeout_secs=5 * 60, interval_secs=10)

if result.state != RunState.completed:
    print(f"Run id: {result.id}, state: {result.state}")
    if result.error:
        print(f"Error: {result.error.json(indent=2)}")
else:
    print(f"Run id: {result.id}, result: {result.outputs_formatted()}")
```

If you want to make an async run using the API you can do something like the following:

```curl
# Make an async run
curl -X POST 'https://www.mystic.ai/v4/runs' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json' \
--data '{
	"pipeline": "my_user/my_pipeline:v1",
	"inputs": 
		[
			{"type":"string","value":"my_input_string"},
			{"type":"integer","value":5}
		],
    "async_run": true
	}
'

# Fetch run details (replace YOUR_RUN_ID with run id from previous API call output)
curl 'https://www.mystic.ai/v4/runs/YOUR_RUN_ID' \
--header 'Authorization: Bearer YOUR_TOKEN' \
--header 'Content-Type: application/json' \
```

### Queue position

When performing async runs there's also a queue position returned in the run schema. You can view this field in the source [here](https://github.com/mystic-ai/pipeline/blob/f8b5ec409cd3e6da0e2505ae5d4cf3198cf4ed4e/pipeline/cloud/schemas/runs.py#L275). The run schema will look something like this:

```json
{
  "id": "run_123455",
  
  "...": "...",
  
  "queue_position": 1
}
```

The `queue_position` has the following behaviour:

* It is only non-null (an integer) when the run state is `queued`
* It's 0-indexed meaning that a `queue_position` of `0` means that it's at the front of the queue and will be assigned to the next resource available
* The `queue_position` on rare occasions may increase which means the run is being retried - this is exceptionally rare

## Waiting for pipeline to start up

Mystic scales pipelines up and down based on traffic. If a particular pipeline has not been used for a while it will be scaled down. This means the next time a run is made against that pipeline, you will get a 503 error, which signifies there are no compute resources to satisfy the request. In the background, your pipeline will be scaled up, so you should be able to use it again within a few minutes (the time it takes for a pipeline to become ready depends on a few factors such as the hardware it's running on and the time your pipeline takes to run any startup functions).

If you'd rather wait until the pipeline is ready to handle the request, rather than fail early, you can pass in `wait_for_resources=True` to `run_pipeline()`:

```python
result = run_pipeline(pointer, *input_data, wait_for_resources=True)
```

If using the API directly you would just add `"wait_for_resources": true` to the JSON input data.

Some important things to note:

* If the pipeline takes longer than 5 minutes to become available (including the machine booting up and the pipeline starting), you will still receive a 503 (No resources available). In this case it might be worth trying again. If it still doesn't work, then it's likely there was an issue with the pipeline starting up.
* For async runs, this behaviour is the default (to wait for the pipeline to be ready). If you would rather it fail early, you need to explicitly set `wait_for_resources` to false.
* You can check how many instances there are of a particular pipeline running by using the `/v4/pipelines/<pipeline_id>/scaling` endpoint.

## Failure modes

There's a few reasons why a run might fail, here's a chart of what can happen and what the response state will be:

| Error                  | run state                | more info                                                                                                                           |
| :--------------------- | :----------------------- | :---------------------------------------------------------------------------------------------------------------------------------- |
| Incorrect inputs       | `failed`                 | An exception will be returned saying that the inputs are incorrect                                                                  |
| Run execution error    | `failed`                 | The pipeline might raise an error due to an exception at run time, this exception will be returned in the error field               |
| Preemption             | `node_preempted`         | This means that the run was executing on a spot machine that was recalled by the cloud provider. You can send the run request again |
| Timeout                | `no_resources_available` | Used when `wait_for_resources=True` and no resource has been come alive after the timeout period (5 minutes)\*                      |
| No resources available | `no_resources_available` | Used when `wait_for_resources=False (default)` and no resource is alive - scaling is not awaited\*                                  |

*\*Read more about this above [Waiting for a pipeline to startup](#waiting-for-pipeline-to-start-up).*

## Streaming

To perform streaming runs, refer to the guide on [streaming](https://docs.mystic.ai/docs/streaming)

## Run Concurrency Limits

To ensure fair usage and optimal performance, our platform enforces run concurrency limits based on your team's account tier. These limits define the maximum number of concurrent runs your team can have at any given time. The limits are as follows:

* Basic Tier: Teams on the Basic tier can have up to 3 concurrent runs.
* Starter Tier: Teams on the Starter tier can have up to 5 concurrent runs.
* Pro Tier: Teams on the Pro tier can have up to 12 concurrent runs.
* Startup/BYOC Tier: Teams on the Startup tier have an uncapped concurrency limit, allowing for an unlimited number of concurrent runs.

### How Concurrency Limits Work

Concurrency limits are enforced by tracking the number of active runs within a specified lookback period. Only runs that are in non-terminal states (e.g., running, queued) are counted towards the concurrency limit. Runs that have completed, failed, or are in other terminal states do not count towards the limit.

If your team reaches the concurrency limit, any additional run requests will be rejected until the number of active runs falls below the limit. This ensures that all teams have fair access to computational resources and helps maintain the stability and performance of the platform.