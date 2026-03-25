# Source: https://docs.mystic.ai/docs/pipeline-building.md

# Pipeline building

Learn how to build pipelines

> 📘 You need some things installed
>
> You will need the following things installed:
>
> * Docker
> * Our python SDK: `pip install -U pipeline-ai`
> * Optional: Docker daemon setup with the nvidia-toolkit for running on GPUs locally

# Setup

Building and running a pipeline always starts with the same few simple steps:

1. Create a clean directory and navigate to it: `mkdir test_pipeline && cd test_pipeline` *(You don't have to create an empty directory - the next step can be done in a populated directory if you're wrapping an existing code base)*
2. Run `pipeline container init` and follow the instructions. This will generate three files:
   1. `new_pipeline.py` - The main python file that you can run your code in
   2. `pipeline.yaml` - A configuration file for the pipeline and its environment
   3. `README.md` - A readme containing information about your pipeline that will be sent on upload to Mystic, read more here: [Using the README.md](https://docs.mystic.ai/docs/using-the-readmemd).
3. Run `pipeline container build` to build the container
4. `pipeline container up -d` will start the container in development mode with hot reloading and create a micro dashboard for you to run the pipeline, you can see this dashboard by going to a browser and visiting: <http://localhost:14300>.

# Creating a pipeline in python

The main file you will be operating in is `new_pipeline.py` which is populated with a basic template code that can be run out of the box. You can rename this file and point to the new name in `pipeline.yaml` under the field `pipeline_graph`.

A basic pipeline can be built using the `Pipeline` context manager, the `pipe` decorator and the `Variable` class:

```python Python
from pipeline import Pipeline, Variable, pipe


@pipe
def add_numbers(a: int, b: int) -> int:
    return a + b


with Pipeline() as builder:
    a = Variable(int)
    b = Variable(int)
    c = add_numbers(a, b)
    builder.output(c)
    
pipeline_graph = builder.get_pipeline()
```

The `@pipe` decorator tells the context manager not to execute the function yet and use it's python typing to create a node in the compute graph that can be executed later.

> 📘 Output types are inferred at runtime
>
> The `builder.output(...)` function in the code example above tells the context manager what variables to output, the exact output types are inferred at runtime. This means it's possible to define a `str` return type from a function but actually return an `int` for example and the pipeline will not convert to a `str`  but return an `int`. This is bad practice however and you should always use the correct typing.

## Input and output types

There are 10 types of IO variables used across all Mystic services ([source](https://github.com/mystic-ai/pipeline/blob/3372a21d8281c10732c0e5e173216f44f712609f/pipeline/cloud/schemas/runs.py#L91)):

* Integer - `integer` (python primitive `int`)
* String - `string` (python primitive `str`)
* Floating point - `fp` (python primitive `float`)
* Dictionary - `dictionary` (python primitive `dict`)
* Boolean - `boolean` (python primitive `bool`)
* None/null - `none` (python primitive `None`)
* Array - `array` (python primitive `list`)
* Pickle\* (*Soon to be deprecated*) - `pkl`
* File - `file` (imported by `from pipeline import File`)
* Stream\* - `stream`  (imported by `from pipeline import Stream`)

***\*Output only***

These types can be referenced as shown below in functions:

```python
from pipeline import File, Stream, Pipeline, Variable, pipe

# How to use `integer`, `fp` and `boolean`
@pipe
def numbers_check(a: int, b: float) -> bool:
	return a > b

# How to use `string` and `stream`
@pipe 
def string_stream(my_string: str) -> Stream:
  my_iterator = c for c in my_string
  
  return my_iterator

# How to use `dictionary`
@pipe
def key_check(my_dict: dict) -> str:
  return my_dict.get("my_key", "Not found!")

# Return the size of the file
@pipe
def file_check(my_file: File) -> int:
  return my_file.path.stat().st_size
```

These types can be defined as inputs to a pipeline then passed to the functions by using their types as shown above:

```python
from pipeline import File, Stream, Pipeline, Variable

...

with Pipeline() as builder:
  var_1 = Variable(int)
  var_2 = Variable(str)
  var_3 = Variable(float)
  var_4 = Variable(dict)
  var_5 = Variable(bool)
  var_6 = Variable(list)
  var_7 = Variable(File)
  
...
```

You can learn about using the more complicated `File` and `Stream` types in their respective document pages:

* File - [Files](https://docs.mystic.ai/docs/files-and-directories)
* Stream - [Streaming](https://docs.mystic.ai/docs/streaming) and [Stream Run](https://docs.mystic.ai/reference/stream_run_v4_runs_stream_post)

# Configuring the runtime and environment

The `pipeline.yaml` file present in the working directory for a pipeline defines everything you'll need to set for your pipeline's container, including:

* Python dependencies & versio
* System commands (like `apt-get install ...`)
* GPUs to use on upload

Here's a typical config file:

```yaml
runtime:
  container_commands:
    - apt-get update
    - apt-get install ffmpeg libsm6 libxext6  -y
  python:
    version: "3.10"
    requirements:
      - pipeline-ai
      - invisible_watermark
      - transformers
      - accelerate
      - safetensors
      - torch
      - diffusers
accelerators: ["nvidia_a100"]
pipeline_graph: new_pipeline:my_new_pipeline
pipeline_name: stable-diffusion
readme: README.md
extras: {}
```

The container commands and python fields are self explanatory, and you can read more about the other fields in their respective documents:

* accelerators: [GPUs and accelerators](https://docs.mystic.ai/docs/gpus-and-accelerators)
* readme: [Using the README.md](https://docs.mystic.ai/docs/using-the-readmemd)

Two fields that are important to understand that do not have separate documentation:

* `pipeline_graph` - This is a reference to where the output of the `Pipeline` context manager is in the `file_name:variable_name` format. For example `new_pipeline:my_new_pipeline` would mean that theres a `new_pipeline.py` file in the current directory and the pipeline variable is `my_new_pipeline = builder.get_pipeline()` after the context manager.
* `pipeline_name` - This is used when building the container and uploading to Mystic. It will be used as the main image name locally, and can optionally include your username as a prefix: `paulh/mistral-7b` for example. If your username is not included it will be prepended on upload to Mystic.

Once you have completed this configuration file you're able to build and run the pipeline, you can do this doing the following commands in your terminal in the pipeline directory:

```shell
pipeline container build
pipeline container up -d
```

This will startup a micro dashboard that you can use to test the pipeline, you can visit it by going to \<http\://localhost:14300>.

# Uploading

Once you have completed the previous steps you can upload your pipeline to Mystic (assuming you've [authenticated](https://docs.mystic.ai/docs/login)) :

```shell
pipeline container push
```

If you want to include some additional pointers to the pipeline on upload (more on [Pointers here](https://docs.mystic.ai/docs/pointers-1)) you can pass in several `-p` arguments:

```shell
pipeline container push -p paulh/demo-pipeline:production -p paulh/demo-pipeline:staging
```

# Custom dockerfiles and pipeline files

As of pipeline-ai version `2.1.11` you can specify extra custom options during pipeline operations.

## Custom dockerfile

If you'd like to use a custom dockerfile, or modify and use the autogenerated dockerfile, you can do so by specifying a path to the dockerfile with the `-d` option, like so:

`pipeline container build -d my-custom.dockerfile`

Note that pipeline won't auto-generate the dockerfile as normal. We recommend running the build command once without `-d`, copying and editing the dockerfile, and then using `-d` to build with the customized file.

## Custom pipeline file

By default, any `pipeline container` command will use the file at `./pipeline.yaml`. The `-f` option allows pointing to a custom filepath like so:

`pipeline container -f my-custom-pipeline.yaml push`

This command can be combined with the above: `pipeline container -f staging.yaml build -d my-custom.dockerfile`

# Deleting

You can delete a pipeline once it's uploaded in one of two ways:

* CLI - `pipeline delete pl PIPELINE_ID`
* Dashboard - You can delete a pipeline on its settings page, scroll down to dangerzone and click delete.