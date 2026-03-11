# Source: https://docs.mystic.ai/docs/streaming.md

# Streaming

Get output streams from your pipelines

# Building a streaming pipeline

To return a streaming output from a pipeline you need to use the `Stream` object:

```python
from pipeline.objects.graph import Stream
```

This object should be initialised and returned from a function as shown in the below example:

```python
import time

from pipeline import Pipeline, pipe
from pipeline.objects.graph import Stream, Variable


@pipe
def streamer(input_data: str) -> Stream:
    def iter_output(data):
        for word in data.split():
            time.sleep(0.1)
            yield word + " "

    return Stream(iter_output(input_data))


with Pipeline() as builder:
    in_1 = Variable(str)
    result = streamer(in_1)
    builder.output(result)


my_pipeline = builder.get_pipeline()
```

The `Stream` object takes in an Iterator object. Be careful not to pass in an Iterable, which is very different. For example:

```python
# This is an iterator
my_iterator = i in range(10)
my_stream = Stream(my_iterator)

# This is an iterable and will not work
my_array = [1, 2, 3, 4, 5]
my_stream = Stream(my_array) # This will not work

```

# Performing a run

Performing a streaming run is similar to a regular run, except there is a different endpoint: `/v4/runs/stream`. The input schema is identical, however while the output schema is the same, you will actually receive back a series of run results as they become available, each one separated by a newline.

Errors should be returned by the API in a similar way to the regular run endpoint.

## Using the Python SDK

There is a `stream_pipeline` generator function that can be used to perform a streaming run with the Python SDK. To use it you can do something similar to the [example in the pipeline repo](https://github.com/mystic-ai/pipeline/blob/main/examples/stream.py):

```python
from pipeline.cloud.pipelines import stream_pipeline

pipeline = "pipeline_id_or_pointer"
inputs = ["example input string"]

print("Streaming pipeline:\n")
for result in stream_pipeline(pipeline, *inputs):
    if result.error:
        print(result)
    else:
        print(result.outputs_formatted()[0], flush=True)
```

## Calling the API directly

Here is an example using CURL (note the different endpoint and the use of the `-N` option, which disables  buffering of the output stream, i.e. returns data as it becomes available):

```shell
curl -X POST 'https://www.mystic.ai/v4/runs/stream' \
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
' \
-N
```