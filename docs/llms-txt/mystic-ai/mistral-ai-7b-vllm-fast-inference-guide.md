# Source: https://docs.mystic.ai/docs/mistral-ai-7b-vllm-fast-inference-guide.md

# Deploy Mistral 7B with vLLM

Mistral 7B is an open source LLM from Mistral AI released in September 2023. This example demonstrates how to achieve faster inference with both the regular and instruct model by using the open source project [vLLM](https://github.com/vllm-project/vllm).

Below is a table outlining the performance of the models (all models are in float16 mode with a single conversation being processed) all tests used up to 25GB of VRAM on an A100 40GB costing $2 /hour on Mystic.

| Batch size | Cost per 1k tokens | Tokens/s |
| :--------- | :----------------- | :------- |
| 1          | $0.0121            | 46       |
| 10         | $0.00139           | 400      |
| 60         | $0.000309          | 1.8k     |

You can also play with the models right now to test out the performance for yourself:

* [Mistral AI 7B](https://www.mystic.ai/mistralai/Mistral-7B-v0.1/play)
* [Mistral AI Instruct 7B](https://www.mystic.ai/mistralai/Mistral-7B-Instruct-v0.1/play)

All of the source code and files for this example can be found in the Pipeline SDK repo [here](https://github.com/mystic-ai/pipeline/tree/ph/just-balls-in-holes/examples/docker/mistral-7b).

If you haven't setup your machine for working with Pipelines yet, please follow the [Getting Started](https://dash.readme.com/project/mystic/v1.1.0/docs/getting-started) guide before doing this tutorial.

# Setup

First we make a directory and then initialize our project:

```shell
mkdir mistral-7b-pipeline && cd mistral-7b-pipeline
pipeline container init
```

This will give us a basic `pipeline.yaml` and `new_pipeline.py` file to start building our pipeline with.

# YAML

We need to make some changes to our YAML file to setup our Pipeline environment. Firstly we add the following container commands, which will make sure `gcc` is installed:

```yaml
container_commands:
    - apt-get update
    - apt-get install -y gcc
```

Next we configure our Python dependencies, we need the following for Mistral:

```yaml
    requirements:
      - "pipeline-ai"
      - "torch==2.0.1"
      - "transformers"
      - "diffusers==0.19.3"
      - "accelerate==0.21.0"
      - "vllm==0.2.1.post1"
```

Mistral is pretty small, it can run on a single A100 with 40GB of VRAM:

```yaml
accelerators: ["nvidia_a100"]
accelerator_memory: null
```

Lastly, you'll want to change `pipeline_name` to have your Mystic username so that we can upload this Pipeline later.

```yaml
pipeline_name: mystic_user/mistral-7b
```

Our final YAML looks like this:

```yaml
runtime:
  container_commands:
    - apt-get update
    - apt-get install -y gcc
  python:
    version: "3.10"
    requirements:
      - "pipeline-ai"
      - "torch==2.0.1"
      - "transformers"
      - "diffusers==0.19.3"
      - "accelerate==0.21.0"
      - "vllm==0.2.1.post1"
    cuda_version: "11.4"
accelerators: ["nvidia_a100"]
accelerator_memory: null
pipeline_graph: new_pipeline:my_pipeline
pipeline_name: mystic_user/mistral-7b

```

# Python Code

Let's start with the imports, we'll be using the `vllm` library to make running our model super easy:

```python
from typing import List

from vllm import LLM, SamplingParams

from pipeline import Pipeline, entity, pipe
from pipeline.objects.graph import InputField, InputSchema, Variable
```

Next we'll define an input schema to wrap up all our inference parameters:

```python
class ModelKwargs(InputSchema):
    do_sample: bool | None = InputField(default=False)
    use_cache: bool | None = InputField(default=True)
    temperature: float | None = InputField(default=0.6)
    top_k: float | None = InputField(default=50)
    top_p: float | None = InputField(default=0.9)
    max_tokens: int | None = InputField(default=100, ge=1, le=4096)
```

Now we'll implement the actual Pipeline. This is fairly straightforward thanks to our use of libraries. Note how we load the model at startup only.

```python
@entity
class Mistral7B:
    @pipe(on_startup=True, run_once=True)
    def load_model(self) -> None:
        self.llm = LLM("mistralai/Mistral-7B-Instruct-v0.2", gpu_memory_utilization=0.5)

    @pipe
    def inference(self, prompts: list, kwargs: ModelKwargs) -> List[str]:
        sampling_params = SamplingParams(
            temperature=kwargs.temperature,
            top_p=kwargs.top_p,
            max_tokens=kwargs.max_tokens,
        )

        result = self.llm.generate(prompts, sampling_params)

        return [t.outputs[0].text for t in result]
```

Our model takes a list of prompts, and outputs a list of results. If you want to learn more about how the actual inference call works, you can take a look at [VLLM](https://pypi.org/project/vllm/).

Finally, let's connect the inputs and outputs of our model and package it:

```python
with Pipeline() as builder:
    prompt = Variable(list, default=["My name is"])
    kwargs = Variable(ModelKwargs)

    _pipeline = Mistral7B()
    _pipeline.load_model()
    out = _pipeline.inference(prompt, kwargs)

    builder.output(out)


my_pipeline = builder.get_pipeline()
```

And that's it!

# Testing

Your Pipeline should now be ready to test. If you want to run it locally, you may need to have a GPU installed. You can run your container locally with `pipeline container up`, or push it to Mystic and run the Pipeline on your dashboard.