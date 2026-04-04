# Source: https://docs.mystic.ai/docs/files-and-directories.md

# Files

When working with ML you will often need to use one or several files in your workflow. These will typically be inputs or outputs to a pipeline. It's also possible to send a large image or video (file) as part of a run request. The Pipeline SDK has a useful object to make this easier:

* `File`- An object that references a local file and allows it to be used remotely

The `File` class represents a file that can be used as a variable in the pipeline. You can create these objects programatically or in the CLI, and also as part of the pipeline definition or directly in a Run.

These file objects are typically used as Run time inputs or outputs, where the files are generally different each time the pipeline is run. For instance, when passing in an image to do some processing on it, transcribing a large audio file, or when an image/video is generated and outputted from the pipeline.

If you need to include files generally in your pipeline, you can simply copy them into your pipeline directory. Anything in the directory is automatically copied into the docker image, where you can reference them as you would in a local filesystem.

During the lifecycle of the run, all output files are saved to our hosted storage and a url for each outputted file will be returned to you when the run is complete. For a given run, the urls for all input and output files can be obtained from the response of the `GET /v4/runs/{run_id}` endpoint, once the run has completed.

# Run time input

To use a file in a run, pass in the `File` class to the `Variable` type:

```python
from pipeline import File, Pipeline, Variable, pipe

@pipe
def my_func(my_file: File) -> str:
    return my_file.path.read_text()


with Pipeline() as builder:
    var_1 = Variable(File)

    output = my_func(var_1)

    builder.output(output)

my_pl = builder.get_pipeline()


```

## API requests for `File` objects

A standard cURL request for a run looks something like this:

```shell
curl --request POST \
  --url https://www.mystic.ai/v4/runs \
  --header 'Authorization: Bearer API_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
	"pipeline": "meta/llama-2-70B:latest",
	"inputs": [
		{
			"type": "string",
			"value": "Hellow my name is Paul, I like to"
		},
		{
			"type": "dictionary",
			"value": {
				"max_new_tokens": 20,
			}
		}
	]
}'
```

And when an input file is expected due to the previously defined `File` variable:

```shell
curl --request POST \
  --url https://www.mystic.ai/v4/runs \
  --header 'Authorization: Bearer API_TOKEN' \
  --header 'Content-Type: application/json' \
  --data '{
	"pipeline": "paulh/read-my-file:v1",
	"inputs": [
		{
			"type": "file",
			"value": null,
      "file_url": "https://storage.mystic.ai/run_files/88/49/88494144-b5d2-426a-82a5-acc3c2ee3daa/image-0.jpg"
		}
	]
}'
```

The assumption here is that the file can be downloaded from the url defined by `file_url`.

To upload the file via HTTP see the following cURL request that can then be used with the above:

```shell
curl --request POST \
  --url https://www.mystic.ai/v4/files \
  --header 'Authorization: Bearer API_TOKEN' \
	--form 'pfile=@/Users/paul/Desktop/my_file.txt'
```

The response contains both `file_name` and `file_url` for use in the run above.

# Run time output

There are two ways files can be returned from a Run, a single `File` output variable, or an array of `File` objects. You must use the standard typing procedure in python to do this:

```python
@pipe
def get_file() -> File:
  local_file_path = "/tmp/image.jpg"
  output_image = File(path=file_path, allow_out_of_context_creation=True)
  return output_image

# OR for an array

from typing import List

@pipe
def get_file() -> List[File]:
  local_file_path = "/tmp/image.jpg"
  local_file_path_2 = "/tmp/image2.jpg"
  output_image = File(path=file_path, allow_out_of_context_creation=True)
  output_image_2 = File(path=file_path_2, allow_out_of_context_creation=True)
  return [output_image, output_image_2]
```

When a `File` object is returned from a `pipe` a run request returns a URL to that file along with other meta data. The file specific variable object looks like the following in a response:

```shell
{
  "type": "file",
  "value": null,
  "file": {
    "name": "image-0.jpg",
    "path": "run_files/31/7e/317e304d-e816-4036-86b2-7ad82b208b70/image-0.jpg",
    "url": "https://storage.mystic.ai/run_files/31/7e/317e304d-e816-4036-86b2-7ad82b208b70/image-0.jpg",
    "size": 22241
  }
}
```

For a list/array of `File` objects the `array` variable is used as the root variable:

```shell
{
  "type": "array",
  "value": [
    {
      "type": "file",
      "value": null,
      "file": {
        "name": "image-0.jpg",
        "path": "run_files/31/7e/317e304d-e816-4036-86b2-7ad82b208b70/image-0.jpg",
        "url": "https://storage.mystic.ai/run_files/31/7e/317e304d-e816-4036-86b2-7ad82b208b70/image-0.jpg",
        "size": 22241
      }
    },
    {
      "type": "file",
      "value": null,
      "file": {
        "name": "image-1.jpg",
        "path": "run_files/45/2a/452a3204-beba-4ccc-949c-1af4e2fcd88c/image-1.jpg",
        "url": "https://storage.mystic.ai/run_files/45/2a/452a3204-beba-4ccc-949c-1af4e2fcd88c/image-1.jpg",
        "size": 16608
      }
    }
  ],
  "file": null
}
```